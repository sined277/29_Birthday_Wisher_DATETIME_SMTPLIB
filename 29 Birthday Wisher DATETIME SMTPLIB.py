import  datetime as dt
import  random
import smtplib

# Get the current date and time
now = dt.datetime.now()

# If today is the 5th day of the month
if now.day == 5:
    # Read quotes from the quotes.txt file
    with open('quotes.txt') as data_file:
        data = data_file.readlines()
        # Choose a random quote from the list
        random_choice = random.choice(data)
        print(random_choice)

    # Set up the email parameters
    my_email = "YOUR EMAIL"
    password = "YOUR PASSWORD"

    # Connect to the SMTP server and log in to the email account
    with smtplib.SMTP("smtp.gmail.com") as conection:
        conection.starttls()
        conection.login(email=my_email, password=password)
        # Send the email with the random quote as the message body
        conection.sendmail(from_addr=my_email, to_addrs='denchikmoney@gmail.com', msg=f"Subject: Monday motivation fuckin freak\n\n {random_choice}")
