import requests  
import json  
  
session = requests.Session()  
url = 'http://localhost/moodle'  
username = 'admin'  
password = 'ijQgmjjPDC2xHrXyM2!'  
  
# API call 1 : getting wstoken to access moodle mobile app API  
payload = {'username': username, 'password': password, 'service': 'moodle_mobile_app'}  
response = session.post(url + '/login/token.php?', data=payload)  
  
response_j = json.loads(response.content.decode('utf-8'))  
web_token = response_j['token']  
  
# API call 2 : getting userid from mobile app  
payload = {'wsfunction': 'core_course_get_courses', 'wstoken': web_token, 'moodlewsrestformat': 'json'}  
response = session.post(url + '/webservice/rest/server.php?', data=payload)  
response = json.loads(response.content.decode('utf-8'))
for course in response:
    print(course['id'])
    
  
session.close() 
