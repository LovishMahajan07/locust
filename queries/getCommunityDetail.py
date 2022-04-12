# 10000 users, spawn rate=1 request , time =1m , without ui
# locust -f getCommunityDetail.py -u 10000 -r 1 -t 1m --headless
from locust import HttpUser,constant,task

class MyReqRes(HttpUser):
    # host="https://beta.connect2d.ca"
    host="http://127.0.0.1:3000"
    wait_time=constant(2)

    @task
    def get(self):
        query="""
            query getCommunityDetail ($communityId:String, $requiredField:[String], $reqPreviousMemberCount:Boolean,  $reqIsMember:Boolean, $membersLimit:Int, $membersOffset:Int) {
                getCommunityDetail (communityId: $communityId, requiredField: $requiredField, reqPreviousMemberCount: $reqPreviousMemberCount, reqIsMember:$reqIsMember, membersLimit: $membersLimit, membersOffset: $membersOffset ) {
                    success
                    message
                    community {
                        _id
                        communityDigitId
                        name
                        description
                        creator
                        visibility
                        photoUrl
                        contractAddress
                        whitePaper {
                            type
                            value
                            fileName
                            _id
                        }
                        launchStatus
                        presaleDate
                        launchDate
                        website
                        tokenomics {
                            type
                            value
                            fileName
                            _id
                        }
                    
                        notes
                        links {
                            name
                            url
                            _id
                        }
                        members {
                            userId
                            role
                            status
                            muted
                            _id
                            firstname
                            lastname
                            profileImageUrl
                            bookmarks{_id text description}
                        }
                        # memberNumber
                        bannedUsers
                        upvoteCount
                        _id
                        subredditName
                        channels { _id channelName channelType channelMembers{_id} }
                        }
                    previousMemberCount
                    ownerPhotoUrl
                    isMember
                    crypto{ _id coinId name symbol currentPrice priceChangePercentage  }
                    creator{_id,firstname,lastname,profileImageUrl}
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
    "communityId": "61f01d101d3f825f5518078d",
    "requiredField": ["_id", "communityDigitId", "name", "description", "visibility", "memberNumber", "memberCountHistory", "launchStatus","members","channels", "photoUrl", "upvoteCount", "website","tokenomics", "bscScan", "pooCoin","dexTool", "notes","contractAddress", "whitePaper", "presaleDate" ,"launchDate", "links","bannedUsers", "goal", "blockchain","creator"],
    "reqPreviousMemberCount": true,
    "reqIsMember": true,
	"membersLimit": 5,
	"membersOffset": 0
}}
        )
        jsonResponse=response.json()
        print(jsonResponse)
