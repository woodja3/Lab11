import requests
import json
from requests.auth import HTTPBasicAuth
from getpass import getpass

username = input("enter your username: ")
password = getpass("enter your password: ")


authurl = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"


payload={}
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}


token = requests.request("POST", authurl, headers=headers, data=payload)


payload1={}
headers1 = {
  'X-Auth-Token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MGVjNGU0ZjRjYTdmOTIyMmM4MmRhNjYiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVlOGU4OTZlNGQ0YWRkMDBjYTJiNjQ4ZSJdLCJ0ZW5hbnRJZCI6IjVlOGU4OTZlNGQ0YWRkMDBjYTJiNjQ4NyIsImV4cCI6MTYzNjY1Mjk2OCwiaWF0IjoxNjM2NjQ5MzY4LCJqdGkiOiIzMWVhNmRjNC0zMzEyLTRkZDktODQ5Ni1jYTllNjk0MWU4OGYiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.R8h0VGzMJe62tQu6gOCzOSvxKpFMOTLMl_tOHYMvcheMgB2paLKOoegx5wMeudnAFq2TpTGfQZ0rLQr1FymeVfh9I_r0uYhogYtPc0453zE5y29gug072041HL5N31H1fFjILYQvEcxvN5uzQsfOicuo4lwpQG7q5Pxn7TBtIbg6UGiLC22i0-12kpG2Gavf6sLaO51yy_TT1BLMzSZDSvexNgTO64y3mhdOOmgOe39NViJQj8sL3tT9IWxux6XYJHHRh30mQZY8-GyCLlYK-K_JcVErC64PvdcqjQNE6_34oh1DXW8rcHpwKF9l_oeyETwD-w3QNyOKnQxSK2yBPA',
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}
list = requests.request("GET", url, headers=headers1, data=payload1)

print(list.text)
