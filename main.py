#To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib

# Set your email and password
MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

# Get today's date
today = datetime.now()
today_tuple = (today.month, today.day)

# Read the birthday data from the CSV file
data = pandas.read_csv("birthdays.csv")
# Create a dictionary of birthdays keyed by month and day
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# If there's a birthday today
if today_tuple in birthdays_dict:
    # Get the data for the birthday person
    birthday_person = birthdays_dict[today_tuple]
    # Choose a random letter template
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    # Replace the placeholder with the person's name in the letter template
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    # Connect to the SMTP server and log in to the email account
    with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        # Send the birthday email with the letter contents as the message body
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
