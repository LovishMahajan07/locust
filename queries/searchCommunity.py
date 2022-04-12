# 10000 users, spawn rate=1 request , time =1m , without ui
# locust -f searchCommunity.py -u 10000 -r 1 -t 1m --headless
from locust import HttpUser,constant,task

class MyReqRes(HttpUser):
    # host="https://beta.connect2d.ca"
    host="http://127.0.0.1:3000"
    wait_time=constant(2)

    @task
    def get(self):
        query="""
            query searchCommunity($nameToSearch: String) { 
                searchCommunity( nameToSearch:$nameToSearch ){ 
                    success 
                    message 
                    communityList{ 
                        _id 
                        communityDigitId 
                        name 
                        description
                        # memberNumber
                        photoUrl
                        launchStatus 
                        upvoteCount 
                        isMember
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
            json={"query":query,"variables":{"nameToSearch": "bit"}}
        )
        jsonResponse=response.json()
        print(jsonResponse)
