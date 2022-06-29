# -*- coding: utf-8 -*-
"""
Created on Wed May  2 13:54:18 2018

@author: HPuser
"""
low = 0
high = 100
guess = 50
print( "Please think of a number between 0 and 100!" )
print( "Is your secret number " + str(guess) + "?" )
char = input( "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

while (char != 'c'):
    if (char == 'h'):
        high = guess
    elif (char == 'l'):
        low = guess
    guess = (low + high) // 2    
    print( "Is your secret number " + str(guess) + "?" )
    char = input( "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
    while (char != 'c' and char != 'l' and char != 'h'):
        print( "Sorry, I did not understand your input." )
        print( "Is your secret number " + str(guess) + "?" )
        char = input( "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

print( "Game over. Your secret number was: " + str(guess))   