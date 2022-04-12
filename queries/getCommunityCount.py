# 10000 users, spawn rate=1 request , time =1m , without ui
# locust -f getCommunityCount.py -u 10000 -r 100 -t 1m --headless
from locust import HttpUser,constant,task

class MyReqRes(HttpUser):
    # host="https://beta.connect2d.ca"
    host="http://127.0.0.1:3000"
    wait_time=constant(2)

    @task
    def get(self):
        query="""
            query getCommunityCount ($launchStatus: [String], $needAllPublic: Boolean, $needPrivate: Boolean) {
                getCommunityCount (launchStatus: $launchStatus, needAllPublic: $needAllPublic, needPrivate: $needPrivate) {
                    success
                    message
                    count
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
  "launchStatus": [
    ""
  ],
  "needAllPublic": true,
  "needPrivate": true
}}
        )
        jsonResponse=response.json()
        print(jsonResponse)
