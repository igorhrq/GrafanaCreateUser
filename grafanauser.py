# Author: Igor Andrade
# 03-02-22 v1.0
# Creates a grafana user on our Grafana
# A Random password will be generated
#
# Thank you Jesus, for bless me!
##################################################################################################
import requests
import re
import json
import random
import string

regexUser = re.compile(r'[A-Za-z]+ [A-Za-z]+')
regexMail = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
regexLogin = re.compile(r'^[a-z]{3,20}$')
regexPass = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')

#API
url='https://youruser:yourpassword@grafana.yourgrafanaurl.com/api/admin/users'

data = dict()

passwd = ''.join(random.choice(string.ascii_letters) for i in range(8))

def isValidUser(user):
    if re.fullmatch(regexUser, user):
      return "Valid Name and Surname pattern...continuing"
    else:
      return None

def isValidMail(email):
    if re.fullmatch(regexMail, email):
      return "Valid email pattern...continuing"
    else:
      return None

def isValidLogin(login):
    if re.fullmatch(regexLogin, login):
      return "Valid Login pattern...continuing"
    else:
      return None

def isValidPasswd(passwd):
    if re.fullmatch(regexPass, passwd):
      return "Valid password pattern...continuing"
    else:
      return None

headers={"Content-Type": 'application/json'}

data['URL'] = "https://grafana.yourgrafanaurl.com/"

## Name type and validate
count=0
while True:
  if count >= 10:
    print("you have entered input in wrong format many times...exiting")
    exit(1)
  users = input(">> Please enter a Name and Surname: as 'Ronaldo Andrade' \n")
  resultado = isValidUser(users)
  if not resultado:
    print("This is not a valid name sir")
    count += 1
    continue
  else:
    print(resultado)
    data['name'] = users
    break

## Mail type and validate
count=0
while True:
  if count >= 10:
    print("you have entered input in wrong format many times...exiting")
    exit(1)
  emails = input("Please enter a email example: opa@YourURL.com:\n")
  resultado = isValidMail(emails)
  if not resultado:
    print("This is not a valid mail sir")
    count += 1
    continue
  else:
    print(resultado)
    data['email'] = emails
    break

## Login type and validate
count=0
while True:
  if count >= 10:
    print("you have entered input in wrong format many times...exiting")
    exit(1)
  logins = input("Please enter a login example: randrade:\n")
  resultado = isValidLogin(logins)
  if not resultado:
    print("This is not a valid Login sir")
    count += 1
    continue
  else:
    print(resultado)
    data['login'] = logins
    break

## Password type and validate
## generate password auto with random and string

data['password'] = passwd

data2 = json.dumps(data)
print(data2) 
count=0
while True:
  accept = ['yes', 'y']
  logins = input("\nDo you want create this user in Grafana: Type: yes or y:\n")
  if logins.lower() not in accept:
    if count >= 10:
      print("too many times...exiting")
      exit(1)
    else:
      print("Wrong Asnwer, type yes or Ctrl + D to leave")
      count += 1
  else:
    response = requests.post(url, data=data2,headers=headers)
    print (response.text)
    print (f"\nGrafanaURL: {data['URL']}\nNome: {data['name']}\nEmail: {data['email']}\nLogin: {data['login']}\nSenha: {data['password']}")
    break
