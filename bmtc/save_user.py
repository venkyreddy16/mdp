#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import mysql.connector
#import Adafruit_CharLCD as LCD

db = mysql.connector.connect(
    host = "localhost",
    user="admin",
    passwd="bmtc",
    database="bmtc"
)

#stop = ["A", "B", "C", "D"]

GPIO.setwarnings(False)
cursor = db.cursor()
reader = SimpleMFRC522()
#lcd = LCD.Adafruit_CharLCD(4, 24, 23, 17, 18, 22, 16, 2, 4);
#try:
  	#while True:
  		#lcd.clear()
  		#lcd.message('Place Card to \n register')
print('Place your card to register\n')
id, bal = reader.read()
print(id)
id = id % 100 
#print(name)
name=""
cursor.execute("SELECT id FROM user WHERE id ="+ str(id))
cursor.fetchone()
if cursor.rowcount < 1:
	name = input("Enter name : ")
	print("Balance updated : Rs. 50")
	bal = 50
	n=0
	print("Journey started\n\n")
	sql_insert = "INSERT INTO user (id, name, balance, check_in) VALUES (%s, %s, %s, %s)"
	cursor.execute(sql_insert,(id,name,bal, 1))
	db.commit()
else:
	cursor = db.cursor()
	cursor.execute("SELECT check_in FROM user WHERE id ="+str(id))
	flag = int(cursor.fetchone()[0])
	if flag == 1:
		#print("Check out!!")
		cursor.execute("SELECT balance,name FROM user WHERE id ="+str(id))
		result = cursor.fetchone()
		bal = int(result[0])
		name =  result[1]
		print("DESTINATIONS:")
		print("1: Indiranagar")
		print("2: Halasuru")
		print("3: Trinity")
		print("4: MG Road")
		print("5: Cubbon Park")
		d = input("Enter destination: ")
		cursor.execute("UPDATE user set check_in = %s WHERE id = %s",(0,id))
		#cursor.execute("update user SET balance = %s WHERE id = %s",(bal-10,id))
		cursor.execute("update user SET balance = %s WHERE id = %s",(bal-(10*int(d)),id))
		print("Name : ",name)
		print("Remaining Balance : ",bal-(10*int(d)))
		print("Journey ended\n\n")
	elif flag == 0:
		#print("Journey started!")
		cursor = db.cursor()
		cursor.execute("Select  balance from user where id = "+str(id))
		bal = int(cursor.fetchone()[0])
		if bal <= 30:
			print("Not Enough balance!\n\n")
		else:
			cursor.execute("Update user SET check_in = %s  WHERE id = %s",(1,id))
			print("Journey started!\n\n")
db.commit()
	
	#cursor = db.cursor()
	#cursor.execute("SELECT balance from  user where id = %s),(id))
	#bal = int(cursor.fetchone())
	#cursor.execute("UPDATE TABLE user SET balance = (%s) WHERE id = (%s)",(bal-10, id))
	#db.commit()

		#lcd.clear()
		#lcd.message('Enter name: ')
		#name = input("Enter name")
#name = input("Enter name")
#cursor.execute("INSERT INTO user (id, name, balance) VALUES (%s, %s, %s)", (id, name, bal))
#db.commit()
        	#lcd.clear()
		#lcd.message("User "+name+" saved")
cursor=db.cursor()
cursor.execute("SELECT balance FROM user where id = "+str(id))
bal = cursor.fetchone()
#print(bal) 
#update_bal= int(bal[0]) - 10
reader.write(str(bal[0]))
#print("User "+name+"\nBalance updated "+str(bal[0]))
#finally:
  #GPIO.cleanup()
