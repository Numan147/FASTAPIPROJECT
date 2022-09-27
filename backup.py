class PerformanceTests(HttpUser):
    host = 'http://127.0.0.1:8000/Customer_details/in'
    wait_time = between(1, 3)

    @task(1)
    def testFastApi(self):    
      
        host = "http://127.0.0.1:8000/Customer_details/in"
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
        response = requests.post(url=host, headers=HEADERS, data=json_data)      
        print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))