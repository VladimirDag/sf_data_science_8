from itertools import count
import numpy as np
number = np.random.randint(1, 101)
count = 0
while True:
    count += 1
    predict_number = int(input('Guess the number from 1 to 100_:')) #Угадай число от 1 до 100
    if predict_number > number:
        print('The number must be less than') #Число должно быть меньше
    elif predict_number < number:
        print('The number must be greater than') #Число должно быть больше
    else:
        print(f'You guessed the number! This number = {number}, for {count} attempts')
        break
    