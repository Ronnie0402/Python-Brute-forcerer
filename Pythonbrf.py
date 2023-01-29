
import random
import pyautogui
character="0123456789abcdefghijklmnopqrstuvwxyz"
character_list=list(character)

password=pyautogui.password( "Hello Raunak , please enter your password  ")

guess_password=''
while(guess_password!=password):
    guess_password=random.choices(character_list,k=len(password))
    print(">"+str(guess_password)+"<<")
    if(guess_password==list(password)):
        print("Your password after performing brute force is "+"".join(guess_password))
        break
