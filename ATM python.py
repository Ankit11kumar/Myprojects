# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 12:09:04 2018

@author: ANKIT
"""

import os
import sys
import time
import math

# This is a code for ATM transaction

print("Welcome to SBI ATM\n")
print("Please insert your card\nCard inserted succesfully\n")

#  USER DETAILS----
card=True
# PIN=2580
Av_balance=10000

if(not card):
    print("Please insert your card properly\n")
else:
    i=0
    j=0
    pin=int(input("Enter your PIN\n"))
    while(i<2 and j==0):                        # For 3 incorrect attempts
        if(pin!=2580):
            print("PIN is wrong\n")
            pin=int(input("Please re-enter your pin\n"))
            i+=1;
        else:
            j=1;
    
    if(i==2):  
        print("Sorry! You have reached maximum number of incorrect attempts\n")
    else:
        print("Choose the options\n")
    
    trans=0
    while(trans!=5):
        
        print("1- Cash Withdrawl\n")               # After pin entered correctly
        print("2- Cash deposit\n")
        print("3- Check balance\n")
        print("4- Change pin\n")
        print("5- Quit\n")
    
        trans=int(input("Choose an action number from above\n"))
    
        if(trans==1):
            With_amount=int(input("Enter the amount you want to withdraw\n"))
            if(With_amount < Av_balance):
                Av_balance = Av_balance - With_amount
                print("Please collect your cash\nThank you for using SBI ATM\n")
                continue
            else:
                print("Sorry, You do not have enough balance\n")
                continue
    
        if(trans==2):
            Dep_amount=int(input("Enter the amount you want to deposit\n"))
            if(Dep_amount>0):
                Av_balance = Av_balance + Dep_amount
                print("Entered amount has been deposited to your account\nThank you for using SBI ATM\n")
                continue
            else:
                print("Sorry, Entered amount is invalid\n")
                continue
            
            
        if(trans==3):
            print("Available balance in your account is--\n",Av_balance,"\nThank you for using SBI ATM\n")
            continue
        
        if(trans==4):
            curr_pin = int(input("Enter your current pin\n"))
            if(curr_pin==pin):
                changed_pin1 = int(input("Enter the new pin\n"))
                changed_pin2 = int(input("Re-enter the new pin\n"))
                if(changed_pin1==changed_pin2):
                    pin=changed_pin1
                    print("Congratulations!! Your PIN has been changed successfully\n")
                    continue
                else:
                    print("Sorry! PIN is not confirmed\n")
                    continue
            else:
                print("Wrong PIN, Sorry!\n")
                continue
        
        if(trans==5):
            continue
    
    print("Thank you!!")
    
    