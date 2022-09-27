import imp
from urllib import request
from locust import User, TaskSet, HttpUser
from locust import User, task, between, constant
from locust import HttpUser, task
import json
import models
from fastapi import responses, Response
import requests

'''
def mytask1(user):
    print("login")
def mytask2(user2):
    print("logout")
class MyUser(User):
    @task(1)
    def mytask1(user):
        print("login")
    @task(2)
    def mytask2(user2):
        print("logout")
    wait_time = constant(2)
'''

class PerformanceTests(HttpUser):
    wait_time = between(1, 3)

    @task(1)
    def testFastApi(self):    
      
        host = 'http://127.0.0.1:8000/Customer_details/in'
        HEADERS = {
        "Content-Type": "application/json"
        }
        data = {
                "first_name": "Numan",
                "last_name": "Shaikh",
                "mobile_no": "8329975829",
                "email": "nooooo@gmail.com",
                "company_name": "Tradecom",
                "city": "VASAI"
            }
        json_data = json.dumps(data).encode('utf8')
        response = self.client.post(url=host, headers=HEADERS, data=json_data) 
        print(response)     
        
        
