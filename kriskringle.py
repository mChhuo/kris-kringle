import smtplib
import random
import re

from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'christkringle7@gmail.com'
PASSWORD = input("Please enter your password:\n")

# Returns two lists one of names and one of email addresses
# Gets read from a file
def get_emails(file):
    names = []
    email = []
    with open(file, "r") as contacts:
        for person in contacts:
            names.append(person.split()[0])
            email.append(person.split()[1])
    return names, email

# Returns the body of the email
def read_message(file):
    with open(file, "r", encoding="utf-8") as message:
        message_template = message.read()
    return Template(message_template)

# Hardest part is working out a suitable derangement
# One person cannot give a gift to himself
def randomise(length):
    receiver = list(range(length))
    while(True):
        random.shuffle(receiver)
        if check_derangement(receiver):
            break
    return receiver

def check_derangement(nums):
    for elm, index in enumerate(nums):
        if elm == index:
            return False
    return True

def write_results(names, receivers):
    with open('results.txt', 'w') as results:
        for index, name in enumerate(names):
            results.write("{} is getting {} a present\n".format(name, names[receiver[index]]))

if __name__ == '__main__':
    names = []
    emails = []
    names, emails = get_emails("contacts.txt")
    message_template = read_message("message.txt")
    receiver = randomise(len(names))
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    write_results(names, receiver)
    for index, (name, email) in enumerate(zip(names, emails)):
        body = MIMEMultipart() # Generates a message for email
        message = message_template.substitute(PERSON_NAME=name.title(), RECEIVER=names[receiver[index]].title())
        # print(message)
        body['From']=MY_ADDRESS
        body['To']=email
        body['Subject']="Kris Kringle"
        
        body.attach(MIMEText(message, 'plain'))
        s.send_message(body)
        del body
    s.quit()