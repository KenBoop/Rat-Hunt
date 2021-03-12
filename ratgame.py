# Intro Sequence
import colorama #colored text
from colorama import Fore
print (Fore.WHITE)
import sys,time,random
import random
import replit
replit.clear()


print('Hello! What is your name?')
myName = input()
time.sleep(0.5)

print('' + myName + '... Hmmm...')
time.sleep(2)

print('... Ah! You are right on time! Welcome ' + myName + '!')

#space between text
print('')
time.sleep(2) 

#decision making time. shall the player view the tutorial or not
Yes = "y"
No = "n"
answer = input("Would you perhaps like a refresher on why you are here? (y/n) ")

#Yes
if answer == Yes:
  replit.clear()
  time.sleep(0.5) 
  print('Ah alright '+myName+ ', your job is to estinguish a rabid rat that is hiding in some boxes.')
  print('')
  time.sleep(3)

  print('These six boxes to be exact!')
  time.sleep(1)

    #Box Color Fun ########################################
  print (Fore.RED)
  print('☐ 1')
  time.sleep(1)

  print (Fore.BLUE)
  print('☐ 2')
  time.sleep(1)

  print (Fore.YELLOW)
  print('☐ 3')
  time.sleep(1)

  print (Fore.GREEN)
  print('☐ 4')
  time.sleep(1)
  
  print (Fore.MAGENTA)
  print('☐ 5')
  time.sleep(1)

  print (Fore.WHITE)
  print('☐ 6')
  time.sleep(1)
#################
  #########################################################

  print('')
  time.sleep(1) 

  print('Just choose the between (1-6) to indicate which box to shoot.')
  print('')
  time.sleep(2) 

  print('But be careful! The rat can change between the four boxes to hide in, and you only have 3 shots. ')
  print('')
  time.sleep(3)

  print('Worry not '+myName+'! Im sure you wont let us down!')
  print('')
  time.sleep(2)
#No
if answer == No:
    time.sleep(0.5) 
    print('Hmm alright '+myName+ ', thats what I like to hear!')
    print('')
    time.sleep(2) 

#Decision Time 2 
answer = input('So '+myName+', are you ready to get to work? (y/n) ')

#No 
if answer == No:
  print('')
  time.sleep(0.5) 
  print('Well, thats too bad '+myName+', we cant let this rat bite anyone! We must get rid of it as quickly as possible!')
  print('')
  time.sleep(4) 

#Yeah 
if answer == Yes:
  print('')
  time.sleep(0.5) 
  print('Thats the spirit '+myName+'! Let get on with it!')
  print('')
  time.sleep(2) 

  #Clear screen
replit.clear()

################GAME STARTS HERE###########################
#######BOXES########
print (Fore.RED)
print('☐ 1')
time.sleep(0.5)

print (Fore.BLUE)
print('☐ 2')
time.sleep(0.5)

print (Fore.YELLOW)
print('☐ 3')
time.sleep(0.5)

print (Fore.GREEN)
print('☐ 4')
time.sleep(0.5)

print (Fore.MAGENTA)
print('☐ 5')
time.sleep(0.5)

print (Fore.WHITE)
print('☐ 6')
print('')
time.sleep(0.5)

ratBox = random.randint(1,6)
guess=int(input("Choose a box (1-6): "))
if guess==ratBox:
  print('')
  print("You got the rat!")
else:
  guess=int(input("Nope, you have two shots left! "))

if guess==ratBox:
    print('')
    print("You got the rat!")
else:
    guess=int(input("Nope, last shot! Make it count! "))

if guess==ratBox:
    print('')
    print("You got the rat!")
    time.sleep(2) 

    replit.clear()
    print (Fore.GREEN)
    print("Congrats! You have done the world good by ridding it of that rat!")
    print (Fore.WHITE)
    time.sleep(2) 

    print('')
    print(":)")
else:
    replit.clear()

    print (Fore.RED)
    print("The box the rat was in was box", ratBox)
    print('')
    time.sleep(2) 
    
    print('Not only did you proceed to get fired after this but the store owner was bitten and is now dead. Game Over.')
    time.sleep(2) 
    print (Fore.WHITE)

    time.sleep(2) 
    print('')
    print(":(")