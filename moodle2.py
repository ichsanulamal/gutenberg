import requests  
import json  
  
session = requests.Session()  
url= 'http://localhost/moodle'  
username = 'admin'  
password = 'ijQgmjjPDC2xHrXyM2!'
  
# API call 1 : getting wstoken to access moodle mobile app API  
payload = {'username': username, 'password': password, 'service': 'moodle_mobile_app'}  
response = session.post(url + '/login/token.php?', data=payload)  
  
response_j = json.loads(response.content.decode('utf-8'))  
web_token = response_j['token']
  
# API call 2 : getting courses from mobile app  
payload = {'wsfunction': 'core_course_get_courses', 'wstoken': web_token, 'moodlewsrestformat': 'json'}  
response = session.post(url + '/webservice/rest/server.php?', data=payload)  
response_j = json.loads(response.content.decode('utf-8'))
course_ids = [course['id'] for course in response_j]

# get all feedback
for course_id in course_ids:
    payload = {'wsfunction': 'mod_feedback_get_feedbacks_by_courses', 'courseids[0]': course_id, 'wstoken': web_token, 'moodlewsrestformat': 'json'}  
    response = session.post(url + '/webservice/rest/server.php?', data=payload)  
    response_j = json.loads(response.content.decode('utf-8'))
    for feedback in response_j['feedbacks']:        
        payload = {'wsfunction': 'mod_feedback_get_responses_analysis', 'feedbackid': feedback['id'], 'wstoken': web_token, 'moodlewsrestformat': 'json'}
        response = session.post(url + '/webservice/rest/server.php?', data=payload)
        response_j = json.loads(response.content.decode('utf-8'))
        print(response_j)
        for attempt in response_j['attempts']:
            print(attempt)
    #     response_j = json.loads(response.content.decode('utf-8'))
    # print(response_j)

