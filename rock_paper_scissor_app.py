import numpy as np
import time


rps = {0: 'Rock', 1: 'Paper', 2: 'Scissor'}
element = [0, 1, 2]
probi = [1/3, 1/3, 1/3]


mark = 0

def game():
    global mark 
    count = 0

    while True:
        
        y = rps[np.random.choice(element, p=probi)]
        x = input('Rock, Paper or Scissor? ').capitalize()  

        if x not in rps.values():  
            print('Wrong input. Please enter Rock, Paper, or Scissor.')
            continue 

        
        if x == y:
            print('It\'s a tie!')
        elif (x == 'Rock' and y == 'Scissor') or (x == 'Paper' and y == 'Rock') or (x == 'Scissor' and y == 'Paper'):
            print('You win!')
            count += 1
        else:
            print('You lose!')
            count -= 1

        print(f'Your mark for this round: {count}')
        mark += count  
        break 


game()


while True:
    z = input('One more round? [Y/N]: ').upper()  
    if z not in ['Y', 'N']:
        print('Wrong input, please input again.')
        continue 
    elif z == 'Y':
        game()
    else:  
        print(f'Your total mark: {mark}')
        break  

