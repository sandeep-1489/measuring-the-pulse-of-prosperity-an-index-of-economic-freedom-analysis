import requests
from requests.auth import HTTPBasicAuth

# ServiceNow credentials and instance info
instance = 'your_instance_name'  # e.g., 'dev12345'
user = 'your_username'
password = 'your_password'

# Base URL
url = f'https://{instance}.service-now.com/api/now/table/incident'

# Headers
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Payload: New incident details
payload = {
    "short_description": "Student unable to access the learning portal",
    "description": "Student John Doe reports an issue accessing https://eduportal.edu. Error: 403 Forbidden",
    "category": "software",
    "caller_id": "john.doe@edu.org",
    "urgency": "2",
    "impact": "2"
}

# Make the POST request to create the incident
response = requests.post(url, auth=HTTPBasicAuth(user, password), headers=headers, json=payload)

# Output result
if response.status_code == 201:
    result = response.json()
    print("Incident created successfully!")
    print("Incident Number:", result['result']['number'])
else:
    print("Failed to create incident.")
    print("Status Code:", response.status_code)
    print("Response:", response.text)