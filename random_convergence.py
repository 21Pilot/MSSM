import random
from random import randint 
import numpy as np
import math 
import matplotlib.pyplot as plt
from statistics import mean

def randomgenerator(n):
    np.random.randint(low = 0, high = n)
    return random.randint(0,n-1)
def birthday(n):
    result = []
    random = randomgenerator(n)
    count =0
    while random not in result:
        result.append(random)
        random = randomgenerator(n)
        count += 1
    return count
def birthday_sim(n):
    n_trials = 10000
    birthday_sim = [birthday(n) for _ in range(n_trials)]
    average = sum(birthday_sim)/n_trials
    
    return average
  
for n in range(2,1000,100):
    sq_rt = math.sqrt(math.pi*(np.power(n,2))/2)
    value = birthday_sim((np.power(n,2)))
    diff = round(abs(value-sq_rt),2)
    
    print("n =",n,"sqrt value is",round(sq_rt,2), "Birthday_sim value is",value,"Absolute difference=",diff)
    plot1 = plt.figure(1)
    plt.scatter((np.power(n,2)),sq_rt, color='red', s= 75)
    plt.scatter((np.power(n,2)),value, color='blue', s = 20)
    plt.xlim(0,(np.power(n,2)))
    plt.ylim(0,math.sqrt(math.pi*(np.power(n,2))/2))
    plt.xlabel('n^2')
    plt.title ("Birthday Problem Graph")
    plt.legend(['red: square root','blue: birthday_sim'], loc = "lower right")
    
