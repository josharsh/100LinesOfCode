import random
import requests
import json

email_endings = ['@gmail.com', '@yahoo.com', '@hotmail.com', '@outlook.com', '@icloud.com']

random_data_generator_url = "https://random-data-api.com/api/v2/users?size=1&is_xml=true"
response = requests.get(random_data_generator_url)
data = json.loads(response.text)

#Name
first_name = data['first_name']
last_name = data['last_name']

#Email
email = data['email'].split("@")
email_numbering = [str(random.randint(1, 1000)), ""]
email = email[0] + random.choice(email_numbering) + random.choice(email_endings)
dot_or_underscore = random.choice([0, 1])
if dot_or_underscore == 1:
    email = email.replace(".", "_")

#Phone
phone_number = data['phone_number']
if phone_number.count("x") != 0:
    phone_number = phone_number.split("x", 1)[0]

#City
city = data['address']['city']

#Street Name
street_name = data['address']['street_name']

#Street Address
street_address = data['address']['street_address']

#Zip code
zip_code = data['address']['zip_code']

#State
state = data['address']['state']

#Country
country = data['address']['country']

#Job Title
job_title = data['employment']['title']

#years of experience
years_of_experience = random.choice(['1', '2', '3', '4', '5+'])

#Salary
salary = random.randrange(50000, 250000, 500)

data = (first_name, last_name, email, phone_number, city, street_name, street_address, zip_code, state, country, job_title, years_of_experience, salary)
print(data)