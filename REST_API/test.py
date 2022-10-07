from urllib import response
import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "video/1", {"likes" : 10, "name":"Tim","views":100000}) #get becuase that is the name of the function
# response = requests.post(BASE + "helloworld/pramod/21") #get becuase that is the name of the function
print(response.json())
input()
response = requests.get(BASE + "video/1") #get becuase that is the name of the function
print(response.json())