import time
from datetime import datetime
import smtplib
from twilio.rest import Client
from gtts import gTTS
import os


language = 'en'
users = ['hemanth']
pins = ['1234']
balance = 100000
available_balance = 0


print("****************************************************************************")
print("*************************                       ****************************")
print("********************  WELCOME TO NO MONEY ATM SYSTEM ***********************")
print("*************************                       ****************************")
print("****************************************************************************")

def user_name():
  text="please enter your user name"
  voice_output(text)
  time.sleep(2)
  user = input('\nENTER USER NAME: ')
  user = user.lower()
  print("WELCOME" + ' ' + user)
  text= "hello"+ user +"welcome to atm"
  voice_output(text)
  time.sleep(2)
  if user in users:
    user_login()
  else:
    print('----------------')
    print('****************')
    print('INVALID USERNAME')
    print('****************')
    print('----------------')
    text = "please enter valid user name"
    voice_output(text)
    time.sleep(2)

def user_login():
  text = "please enter your pin"
  voice_output(text)
  time.sleep(2)
  pin = input('PLEASE ENTER PIN: ')
  if pin in pins:
    print('-------------------------')
    print('*************************')
    print('LOGIN SUCCESFUL, CONTINUE')
    print('*************************')
    print('-------------------------')
    menu()
  else:
    if len(pin) < 4:
      print('------------------------')
      print('************************')
      print('PIN CONSISTS OF 4 DIGITS')
      print('************************')
      print('------------------------')
      user_name()
    else:
      print('PLEASE VERIFY PIN AND TRY AGAIN')
      user_name()

def menu():
  text = "please select the menu options"
  voice_output(text)
  time.sleep(3)
  response = input('SELECT FROM FOLLOWING OPTIONS: \nStatement__(S) \nWithdraw___(W) \nView Balance__(B) \nChange PIN_(P)  \nQuit_______(Q) \nType The Letter Of Your Choices: ')
  response = response.lower()
  if response == 's':
    generate_statement()
  if response == 'w':
    withdraw_amount()
  if response == 'b':
    view_balance()
  if response == 'p':
    change_pin()
  if response == 'q':
    user_name()
  else:
    print('------------------')
    print('******************')
    print('RESPONSE NOT VALID')
    print('******************')
    print('------------------')
    text = "invalid response"
    voice_output(text)
    time.sleep(3)
    user_name()

def generate_statement():
  print("*********************")
  print("PLEASE WAIT TO GENERATE THE STATEMENT")
  time.sleep(5)
  statement()

def statement():
  print("*********************")
  print("BANK STATEMENT")
  time = datetime.now()
  print(time)
  print(users[0])
  print("BALANCE:")
  print(balance)
  print("*********************")
  time.sleep(2)
  text = "please collect the statement"
  voice_output(text)
  user_name()

def withdraw_amount():
  amount = int(input('ENTER THE AMOUNT:'))
  if amount > balance:
    print('-----------------------------')
    print('*****************************')
    print('YOU HAVE INSUFFICIENT BALANCE')
    print('*****************************')
    print('-----------------------------')
    user_name()
  else:
    language = 'en'
    available_balance = balance - amount
    print("YOUR BALANCE IS:" )
    print(available_balance)
    send_mail(available_balance)
    send_text_message(available_balance,amount)
    user_name()

def send_mail(available_balance):
  user_name = 'emaildemo094@gmail.com'
  password = 'TestSmtpPython'
  to_address = 'hemanthgalam123@gmail.com'
  body = 'Transaction Successful' + ' \n' + 'Your available balance is: ' + str(available_balance)
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login(user_name, password)
  server.sendmail(user_name, to_address, body)
  print('Mail Sent')

def send_text_message(available_balance,amount):
  account_sid = 'AC90a1feec7261bca6c217505d58524d53'
  auth_token = 'ff40d8c681ce7678cc5fe606ebc1aea4'
  client = Client(account_sid, auth_token)
  body = 'Transaction Successful'+' \n' +'Your account is debited with:' + str(amount) + '\n'  +'your available balance is:' + str(available_balance)
  message = client.messages.create(
    messaging_service_sid='MG1a7308a270002af501f453c8cbcab3c4',
    body=body,
    to='+918885601437'
  )
  print(message.sid)

def voice_output(text):
  mytext = text
  myobj = gTTS(text=mytext, lang=language, slow=False)
  myobj.save("welcome.mp3")
  os.system("start welcome.mp3")

def change_pin():
  print("ARE YOU SURE! DO YOU WANT TO CHANGE THE PIN")
  response = input('YES(Y) \n NO(N) \n')
  response = response.lower()
  if response == 'y':
    new_pin = input("PLEASE ENTER NEW PIN:")
    old_pin = input("PLEASE ENTER OLD PIN:")
    if len(new_pin) < 4 or old_pin == new_pin:
      print('-------------------------------------')
      print('*************************************')
      print('   NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')
      print('*************************************')
      print('-------------------------------------')
      menu()
    elif old_pin in pins:
      pins.append(new_pin)
      pins.remove(old_pin)
      print("*****************  YOUR PIN HAS BEEN CHANGED SUCCESSFULLY   ********************")
      user_name()
  else:
    user_login()

def view_balance():
  print("YOUR BALANCE IS:")
  print(balance)

user_name()
