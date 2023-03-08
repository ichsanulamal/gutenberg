import requests
import json

# Moodle API URL and token
url = 'http://localhost/moodle/webservice/rest/server.php'
token = '48231b3e5a9d5562fe362556c0d5b5e2'

# Headers and data for API requests
headers = {'content-type': 'application/json'}
data = {'wstoken': token}

# Function to get all feedback responses for a given feedback activity
def get_feedback_responses(feedback_id):
    function = 'mod_feedback_get_responses'
    params = {'feedbackid': feedback_id}
    response = requests.post(url, headers=headers, data=json.dumps({'wsfunction': function, 'arguments': params, **data}))
    response_data = json.loads(response.text)
    return response_data

# Function to get all feedback activities for a list of courses
def get_feedback_activities(course_ids):
    function = 'mod_feedback_get_feedbacks_by_courses'
    params = {'courseids': course_ids}
    response = requests.post(url, headers=headers, data=json.dumps({'wsfunction': function, 'arguments': params, **data}))
    response_data = json.loads(response.text)
    return response_data

# Example usage
course_ids = [1, 2, 3] # List of course IDs
feedback_activities = get_feedback_activities(course_ids)

for feedback_activity in feedback_activities:
    feedback_id = feedback_activity['id']
    feedback_name = feedback_activity['name']
    feedback_responses = get_feedback_responses(feedback_id)
    print(f"Feedback activity: {feedback_name} (ID: {feedback_id})")
    for response in feedback_responses:
        response_id = response['id']
        response_value = response['values']
        print(f"Response ID: {response_id}, Response value: {response_value}")
