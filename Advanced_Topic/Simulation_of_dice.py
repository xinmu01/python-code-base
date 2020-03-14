# Simulation of dice
import random
def simulationOfDice(thre):    
    previousProb = 0
    interation = 0
    step = 1000
    while True:
        counter = 0 
        interation = interation + step
        for i in range(interation):
            dice1 = random.randrange(1,7,1)
            dice2 = random.randrange(1,7,1)
            if dice1 + dice2 == 9:
                counter += 1

        prob = counter/interation
        if prob - previousProb <= thre:
            break
        previousProb = prob

    print("The probablity of rolling two dices when the results are equal to 9 is: {}.".format(round(prob,3)))

if __name__ == '__main__':
    simulationOfDice(0.0000000000000000000001)

