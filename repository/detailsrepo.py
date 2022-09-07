from database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
import  models
from fastapi import Depends, Response,status, HTTPException, Request
#from routers.detailsrouter import delete
import schemas

def create(request, db:Session):
    test=models.Cdetails(first_name=request.first_name, 
                        last_name=request.last_name, 
                        mobile_no=request.mobile_no,
                        email=request.email,
                        company_name=request.company_name,
                        city=request.city)
    db.add(test)
    db.commit()
    db.refresh(test)

    dic={
        "status":"success",
        "msg":test
        }
    return dic

def showing_details(db:Session=Depends(get_db)):
    details=db.query(models.Cdetails).all()
    return details

def updated_details(insert_id, request: schemas.customer, db:Session=Depends(get_db)):
    insert = db.query(models.Cdetails).filter(models.Cdetails.id==insert_id)
    if not insert.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f"Details not found.")
    insert.update(request.dict())
    db.commit()
    return {f'Record with ID. {insert_id} has been updated'}

def delete_details(give_id, db: Session=Depends(get_db)):

    des_details = db.query(models.Cdetails).filter(models.Cdetails.id==give_id)
    if not des_details.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f"Details for id {give_id} not found.")
    des_details.delete(synchronize_session=False)
    db.commit()
    return{f'Record with ID {give_id} has been deleted successfully.'}