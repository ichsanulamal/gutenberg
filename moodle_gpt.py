import requests
import json

class MoodleAPI:
    def __init__(self, url, username, password, service):
        self.url = url
        self.session = requests.Session()
        self.token = self.get_token(username, password, service)

    def get_token(self, username, password, service):
        payload = {'username': username, 'password': password, 'service': service}
        response = self.session.post(self.url + '/login/token.php?', data=payload)
        response_j = json.loads(response.content.decode('utf-8'))
        return response_j['token']

    def call_api(self, function, params):
        payload = {'wsfunction': function, 'wstoken': self.token, 'moodlewsrestformat': 'json', **params}
        response = self.session.post(self.url + '/webservice/rest/server.php?', data=payload)
        response_j = json.loads(response.content.decode('utf-8'))
        return response_j

    def get_courses(self):
        response_j = self.call_api('core_course_get_courses', {})
        return [course['id'] for course in response_j]

    def get_feedback_activities(self, course_id):
        params = {'courseids[0]': course_id}
        response_j = self.call_api('mod_feedback_get_feedbacks_by_courses', params)
        return response_j['feedbacks']

    def get_feedback_responses(self, feedback_id):
        params = {'feedbackid': feedback_id}
        response_j = self.call_api('mod_feedback_get_responses_analysis', params)
        return response_j['attempts']

# Example usage
url = 'http://localhost/moodle'
username = 'admin'
password = 'ijQgmjjPDC2xHrXyM2!'
service = 'moodle_mobile_app'

moodle_api = MoodleAPI(url, username, password, service)
course_ids = moodle_api.get_courses()

for course_id in course_ids:
    feedback_activities = moodle_api.get_feedback_activities(course_id)
    for feedback_activity in feedback_activities:
        feedback_id = feedback_activity['id']
        feedback_name = feedback_activity['name']
        feedback_responses = moodle_api.get_feedback_responses(feedback_id)
        print(f"Feedback activity: {feedback_name} (ID: {feedback_id})")
        for response in feedback_responses:
            response_id = response['id']
            response_value = response['values']
            print(f"Response ID: {response_id}, Response value: {response_value}")