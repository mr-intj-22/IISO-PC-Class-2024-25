# Variables in Python
first_name = 'Malek'
last_name = 'Shefat'
country = 'Japan'
city = 'Tokyo'
age = 250
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname': 'Malek',
    'lastname': 'Shefat',
    'country': 'Japan',
    'city': 'Tokyo',
    'skills': ['HTML', 'CSS', 'JS', 'React', 'Python']
}

# Printing the values stored in the variables
print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line
first_name, last_name, country, age, is_married = 'Malek', 'Shefat', 'Helsink', 250, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
