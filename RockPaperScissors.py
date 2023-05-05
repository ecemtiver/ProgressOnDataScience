#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import the random library
import random


# In[2]:


#create a list containing the three action of the game
action_list = ['rock', 'paper', 'scissors']


# In[9]:


#set the scores of players to 0
computer_score=0
player_score=0

#ask the user how many rounds they want to  play
total_rounds=input("How many rounds do you want to play? Please enter a number here: ")

#add a round counter that is 0 at the beginning
round_counter=0

#write while loop and put the game inside
while True:
    #increase round_counter by and print it
    round_counter += 1
    print("ROUND NUMBER:", round_counter)
    
    #select a random action for computer
    computer_choice=random.choice(action_list)
    
    #ask player to choose an action
    player_choice=input("Please choose your action:")
    
    #print the players choices
    print("COMPUTER:", computer_choice)
    print("PLAYER:", player_choice)
    
    #tie condition
    if computer_choice==player_choice:
        print("Tie! Both players choose the same action.")
    
    #remaining conditions
    elif computer_choice=='paper':
        if player_choice=='rock':
            print("WINNER IS: COMPUTER")
            computer_score += 1
        else:
            print("WINNER IS: PLAYER")
            player_score += 1
            
    elif computer_choice=='rock':
        if player_choice=='paper':
            print("WINNER IS: PLAYER")
            computer_score += 1
        else:
            print("WINNER IS: COMPUTER")
            player_score += 1
    
    elif computer_choice=='scissors':
        if player_choice=='paper':
            print("WINNER IS: COMPUTER")
            computer_score += 1
        else:
            print("WINNER IS: PLAYER")
            player_score += 1
            
    #stop the while loop if the round_counter equals the number of total rounds
    if round_counter==int(total_rounds):
        break

#print the outcome of the game of using conditional statements
if computer_score==player_score:
    print("There is no winner, TIE", computer_score, ":", player_score)
elif computer_score>player_score:
    print("Computer won with score", computer_score, ":", player_score)
elif computer_score<player_score:
    print("Player won with score", computer_score, ":", player_score)

