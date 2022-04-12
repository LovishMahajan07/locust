# 10000 users, spawn rate=1 request , time =1m , without ui
# locust -f getCommunityTwitterTimeline.py -u 10000 -r 1 -t 1m --headless
from locust import HttpUser,constant,task

class MyReqRes(HttpUser):
    # host="https://beta.connect2d.ca"
    host="http://127.0.0.1:3000"
    wait_time=constant(2)

    @task
    def get(self):
        query="""
            query getCommunityTwitterTimeline($communityId: String!) { 
                getCommunityTwitterTimeline( communityId:$communityId ){ 
                    success 
                    message 
                    twitterTimeline {
                        id
                        text
                    }
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
	"communityId": "61bb53fd572b3345466965ee"
}}
        )
        jsonResponse=response.json()
        print(jsonResponse)
