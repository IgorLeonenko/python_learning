##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes.

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import pandas, smtplib
import datetime as dt
import random

file = pandas.read_csv("birthdays.csv")
day_today = dt.datetime.now()

birthdays_dict = file.to_dict(orient="records")
birthday_object = [el for el in birthdays_dict if el["month"] == day_today.month and el["day"] == day_today.day][0]
my_mail = "icovers88@gmail.com"

if bool(birthday_object):
  file_nr = random.randrange(1,3)
  with open(f"./letter_templates/letter_{file_nr}.txt", "r") as file:
    file_content = file.read()
    letter_content = file_content.replace("[NAME]", birthday_object['name'])
  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_mail, password="bcgrvlstuyongvwv")
    connection.sendmail(from_addr=my_mail, to_addrs=birthday_object["email"], msg=letter_content)
