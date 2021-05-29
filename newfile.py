print("Access banks \n 1> Check balance\n 2>Transfer\n 3>Airtime \n 4>Others services\n 5>Access money\n 6>Diamond xtra\n 7>XtraCash loan\n 8>Mobile wallet")
pin = 1111
x=int(input("enter a number\n"))
if x == 1:
	print("\n" * 10)
	value = int(input("Enter your pin"))
	if value ==pin:
		print("your balance will be sent shortly")
	else:
		print("wrong pin try again")
elif x == 2:
	print("\n" * 10)
	amount =int(input("Enter amount \n"))
	if amount > 0:
		account = int(input("enter account number\n"))
elif x ==3:
	print("\n" *10)
	print("Buy airtime\n  1> self\n  2>third party")
	value = int(input(""))
	if value == 1:
		int(input("Enter amount\n"))
		print("sucess you will recieve sms notification soon")
	elif value ==2:
		int(input("Enter amount\n"))
		value= int(input("Enter your pin\n"))
		if value ==pin:
			print("sucess you will recieve sms notification soon")

elif x ==4:
		print("1>pay bills\n 2>access pay\n 3>payday loan\n 4>Enquiry services\n 5>Reset Pin\n 6>cardless withdrawal\n 7>Referral scheme\n 8>update Info\n 9>Opt out\n")
elif x ==5:
 	    print("sorry this service is currently not available")
elif x ==6:
 	    print("1>open a Dimond xtra Account\n 2>View prizes\n 3>Qualifying Criteria\n 4>View Tickets\n")
elif x ==7:
 	    print("sorry this service is currently not available")
elif x ==8:
 	    print("1>send money\n 2>Get a Loan\n 3>pay Bills\n 4>Accesspay\n 5>Withdraw Money\n")
 	    


