
import datetime
import pytz
import wikipedia
import pyjokes
import math
import numpy as np
import random
import os
from PyDictionary import PyDictionary
import GoogleNews
import pyttsx3
import pywhatkit


list1 =['Google' , 'search' , 'Search' , 'Search on google' , 'search on google']
user = str(input("Hello  Sir/Mam ,\n If you dont mind , I can have your name ? :  " ))
print("\n\nHello , " + user, "I am ChatBot")
print("\n\n You can ask me many  stuff like\n  - Todays date\n  - General facts\n  - calculator\n  - You can play songs\n  - You can Search\n  - use Dictionary\n   - read Jokes\n  - can browse your pc\n  - and daily stuff\n  - as well you can help me to update, By giving your Suggesions to my inventor YASH\n  His e-mail id is yashthavkar3@gmail.com")
while True:
    chat = input(" \nAny HELP!!!  from my side  :  \n             or\n If you have done Just type Exit \n -->")

    if (chat=="stop" or chat=="exit"):
        print("Thank you" , user, "it was nice time , hope going to meet soon")
        break


    elif "made you" in chat:
        print("\nIt's Yash , who made me ")
        
    elif 'your name' in chat:
        print("\nMy Name is  Robo  " )
        
    elif 'my name' in chat:
        print("\nHey , you have told me , its " + user)
        
    elif  'date'  in chat:
        current_time = datetime.datetime.now()
        print("\n\nCurrent Date and Time in your country is :   " +  str(current_time ))
        
    elif 'your friend'  in chat :
        print("\nI have only one friend , who is Yash  by the way I have new friend ,  whose name is"  + user )

   
    elif  'play' in chat :
        song = chat.replace('play', ' ')
        print("Playing",song)
        pywhatkit.playonyt(song)

    elif 'search' in chat :
        word = chat.replace('list', ' ')
        print("Searching" , word)
        pywhatkit.search(word)

    elif   'joke'   in chat:
            My_joke = pyjokes.get_joke()
            print(My_joke)

    elif 'calculator' in chat:
        
        while True:
            user2 =int(input(" \nWhich arithmetic you want to  work with \n1.  Addition  \n2.  Substraction \n3.  Multiplication  \n4.  Division \n5.  Additional Arithmatic \n0. Exit\n Enter the number\n:->"))
            
            if  user2==1:
                num1=int(input("Enter 1st  number : ->  "))
                num2=int(input("Enter 2nd  number : ->  "))
                num = num1+num2
                print( "\nYour answer is " + str(num) +"\n")
            elif user2==2:
                num1=int(input("Enter 1st  number : ->  "))
                num2=int(input("Enter 2nd  number : ->  "))
                num = num1 -num2
                print("\nYour answer is " +str(num) +"\n")

            elif user2==3:
                num1=int(input("Enter 1st  number : ->  "))
                num2=int(input("Enter 2nd  number : ->  "))
                num = num1*num2
                print("\nYour answer is " + str(num) +"\n")

            elif user2==4:
                num1=int(input("Enter 1st  number : ->  "))
                num2=int(input("Enter 2nd  number : ->  "))
                num = num1/num2
                print("\nYour answer is " + str(num) +"\n")

            elif user2==5:
                while True:
                    user3=int(input("6.  Square of number \n7.  Square Root \n8.  Cube of number \n9.  Cube Root \n10.  HCF of  Two numbers  \n11 LCM of Two number\n0. Exit \n Enter the number\n :->"))
                    if user3==6:
                        num1=int(input("Enter your  number : ->  "))
                        square = num1*num1
                        print("\nYour answer is " + str(square) +"\n")

                    elif user3==7:
                        num1=int(input("Enter your number : ->  "))
                        sqrt = np.sqrt(num1)
                        print("\nYour answer is " + str(sqrt) + "\n")
                            
                    elif user3==8:
                        num1=int(input("Enter your number :->  "))
                        cube = num1**num1
                        print("\nYour answer is " +str(cube) +"\n")

                    elif user3==9:
                        num1= int(input("Enter your number :->  "))
                        cbrt =np.cbrt(num1)
                        print("\nYour answer is " +str(cbrt) +"\n")


                    elif user3==10:
                        num1=int(input("\nEnter 1st  number : ->  "))
                        num2=int(input("\nEnter 2nd  number : ->  "))
                        x = num1
                        y =num2
                        while x != y :
                            if  x>y:
                                x= x-y
                            else :
                                y= y-x
                        print("HCF of  " , num1 , "and " , num2 , "is " , x , "\n")

                    elif user3==11:
                        num1=int(input("\nEnter 1st  number : ->  "))
                        num2=int(input("\nEnter 2nd  number : ->  "))
                        if num1>num2:
                            max =num1
                        else :
                            max =num2
                        while True:
                            if max%num1==0 and max%num2==0:
                                print(max)
                                break
                            max =max+1
                    
                    else :
                            print("Exit")
                            break
            else :
                print("Exit")
                break

    elif  "dictionary" in chat:
        while True:
            word = int(input("\n1.  Meaning \n0.  Exit\n-->"))
            if word==1:
                word1 =input("\nEnter the word  \n -->")
                from PyDictionary import PyDictionary
                dict = PyDictionary()
                meaning =dict.meaning(word1)
                print(meaning)

            elif word==0:
                break

            else:
                print("Invalid Input")
                
        

    elif 'facts' in chat:
            list = ["Turtles have no teeth.","Prehistoric turtles may have weighed as much as 5,000 pounds.","Only one out of a thousand baby sea turtles survives after hatching.", " Sea turtles absorb a lot of salt from the sea water in which they live. They excreteexcess salt from their eyes, so it often looks as though they'recrying.","Helium is a colourless, odourless, tasteless inert gas at room temperature and makes upabout 0.0005% of the air we breathe.","Helium Balloon Gas makes balloons float. Helium is lighter than air and just as theheaviest things will tend to fall to the bottom, the lightest thingswill rise to the top.",'Helium Balloon Gas makes balloons float. Helium is lighter than air and just as theheaviest things will tend to fall to the bottom, the lightest thingswill rise to the top.','Camels can spit.','An ostrich can run 43 miles per hour (70 kilometers per hour).' ,'Pigs are the fourth most intelligent animal in the world.' ,'Dinosaurs didnt eat grass? There was no grass in the days of the dinosaurs.', 'India has the most post offices in the world', 'Navigation is derived from the Sanskrit word NAVGATIH',' The word navy is also derived from the Sanskrit word Nou.',' Until 1896, India was the only source for diamonds to the world', 'The place value system and the  decimal system were developed in 100 BC in India.', 'A snail can sleep for 3 years.', 'The names of the continents all end with the same letter with which they start.', 'Twenty-Four- Karat Gold is not pure gold since there is a small amount of copper init. Absolutely pure gold is so soft that it can be molded with thehands.','Paris, France has more dogs than people.','New Zealand is home to 70 million sheep and only 40 million people.','A frog named Santjie, who was in a frog derby in South Africa jumped 33 feet 5.5inches.','The longest life span of a frog was 40 years.','The eyes of a frog flatten down when it swallows its prey.', 'The name India is derived from the River Indus.','The Persian invaders converted it into Hindu','The name Hindustan combines Sindhuand Hindu and thus refers to the land of the Hindus.',' Chess was invented in India.', 'The place value system and the decimal system were developed in 100 BC in India.', 'The game of snakes & ladders was created by the 13th century poet saint Gyandev. Itwas originally called Mokshapat.',' The ladders in the game represented virtues and the snakes indicated vices.']
            print(random.choice(list))
            
    elif 'my pc' in chat:
        # Python program to create
# a file explorer in Tkinter
  
# import all components
# from the tkinter library
        from tkinter import *
  
# import filedialog module
        from tkinter import filedialog
  
# Function for opening the
# file explorer window
        def browseFiles():
            filename = filedialog.askopenfilename(initialdir = "/",
                                              title = "Select a File",
                                              filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
      
    # Change label contents
            label_file_explorer.configure(text="File Opened: "+filename)
      
      
                                                                                                  
# Create the root window
        window = Tk()
  
# Set window title
        window.title('File Explorer')
  
# Set window size
        window.geometry("500x500")
  
#Set window background color
        window.config(background = "white")
  
# Create a File Explorer label
        label_file_explorer = Label(window,
                                        text = "File Explorer using Tkinter",
                                        width = 100, height = 4,
                                        fg = "blue")
  
      
        button_explore = Button(window,
                                    text = "Browse Files",
                                    command = browseFiles)
  
        button_exit = Button(window,
                     text = "Exit",
                     command = exit)
  
# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
        label_file_explorer.grid(column = 1, row = 1)
  
        button_explore.grid(column = 1, row = 2)
  
        button_exit.grid(column = 1,row = 3)
  
# Let the window wait for any events
        window.mainloop()

   
        
    else :
        print("\n\nI haven't get it, \n if you want to stay type Yes or type Exit")
        chat = input("->")

                   
            
        
