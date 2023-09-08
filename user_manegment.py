import csv
import os
csv_file = 'user_data.csv'


def save_user_data(user_id, username, first_name, last_name):
    # Check if the CSV file exists, and create it if not
    if not os.path.exists(csv_file):
        with open(csv_file, 'w', newline='') as file:
            csv_writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
            # Write the header row
            csv_writer.writerow(["User ID", "Username", "First Name", "Last Name"])

    # Append the user's data to the CSV file with double quotes
    with open(csv_file, 'a', newline='') as file:
        csv_writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([user_id, username, first_name, last_name])

def user_exists(user_id):
    # Check if the CSV file exists
    if not os.path.exists(csv_file):
        return False

    # Check if the user ID exists in the CSV file
    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            if row and int(row[0]) == user_id:
                return True
    return False
