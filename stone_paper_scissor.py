
from art import *
import random
pat = text2art('''stone
paper
scissor''',"bulbhead")
print(pat)
print('For exiting the game press \'ctrl+z\'')
options = ['stone', 'paper', 'scissor']
count_co = 0
count_us = 0
while True:
 print(('\n\t\t\tPOINTS\n\n\t\tUser:     {}\n\t\tComputer: {}').format(count_us,count_co))
 x = input("\nEnter your choice: stone(1), paper(2) or scissor(3)?\n")
 y = random.choice(options) 
 if x == '1':
   x = 'stone'
 elif x == '2':
   x = 'paper'
 elif x == '3':
   x = 'scissor'

 if x == y:
   print('user: '+x+'\n'+'computer: '+y)
   print("It's a tie")
 elif x == 'stone' and y == 'paper':
   print('user: '+x+'\n'+'computer: '+y)
   print('\nComputer wins!!')
   count_co = count_co+1
 elif x == 'stone' and y == 'scissor':
   print('user: '+x+'\n'+'computer: '+y)
   print('\nUser wins!!')
   count_us = count_us+1
 elif x == 'paper' and y == 'stone':
   print('user: '+x+'\n'+'computer: '+y)
   print('\nUser wins!!')
   count_us = count_us+1
 elif x == 'paper' and y == 'scissor':
   print('user: '+x+'\n'+'computer: '+y)
   print('\nComputer wins!!')
   count_co = count_co+1
 elif x == 'scissor' and y == 'stone':
   print('user: '+x+'\n'+'computer: '+y)
   print('\nComputer wins!!')
   count_co = count_co+1
 elif x == 'scissor' and y == 'paper':
   print('user: '+x+'\n'+'computer: '+y)
   print('\nUser wins!!')
   count_us = count_us+1
 else:
   print('Invalid choice')
