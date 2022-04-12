# 10000 users, spawn rate=1 request , time =1m , without ui
# locust -f getAllNews.py -u 10000 -r 100 -t 1m --headless
from locust import HttpUser,constant,task

class MyReqRes(HttpUser):
    # host="https://beta.connect2d.ca"
    host="http://127.0.0.1:3000"
    wait_time=constant(2)

    @task
    def get(self):
        query="""
            query getAllNews ($limit: String,$skip: String) {
                getAllNews (limit: $limit, skip: $skip) {
                    success
                    message
                    data
                }
            }
        """
        response=self.client.post(
            "http://127.0.0.1:3000/guru/v1.0/",
            # "https://beta.connect2d.ca/guru/v1.0/",
            headers={
                "Accept": "application/graphql",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI2MWYwMTUxNDlhZWI0MmM2NDU3YjQxYWQiLCJpYXQiOjE2NDkxNjE4MjN9.1jfbW1gWIYTTy0YkF9kn7xmL3H4lIoIuE3K4nVMAizY"
            },
            json={"query":query,"variables":{
  "limit": "5",
   "skip":"2"
}}
        )
        jsonResponse=response.json()
        print(jsonResponse)
