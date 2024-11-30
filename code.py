import re
from collections import defaultdict

# Function to read log data from a text file
def read_log_file(file_path):
    with open(file_path, 'r') as file:
        log_data = file.read()
    return log_data

# Function to parse the log data
def parse_log(log):
    entries = log.strip().split('\n')
    employee_activity = defaultdict(list)

    for entry in entries:
        parts = entry.split()
        timestamp = parts[0] + " " + parts[1]
        ip_address = parts[2]
        username = re.search(r'(\w+)\s+(\w+)', ' '.join(parts)).group(0) if len(parts) > 9 else "Unknown"
        action_url = parts[8] if len(parts) > 8 else "N/A"

        employee_activity[username].append((timestamp, ip_address, action_url))

    return employee_activity

# Function to identify suspicious activity
def identify_suspicious_activity(employee_activity):
    suspicious_users = []
    suspicious_keywords = ["embed-api.ddhq.io", "dev.ebikestore.com", "login"]

    for user, activities in employee_activity.items():
        for _, _, url in activities:
            if any(keyword in url for keyword in suspicious_keywords):
                suspicious_users.append(user)
                break

    return set(suspicious_users)

# Main execution
if _name_ == "_main_":
    # Specify the path to your log file here
    log_file_path = 'hackathondata.txt'  # Change this to the path of your log file
    log_data = read_log_file(log_file_path)
    
    employee_activity = parse_log(log_data)
    suspicious_users = identify_suspicious_activity(employee_activity)

    print("Suspicious Users Detected:")
    for user in suspicious_users:
        print(user)