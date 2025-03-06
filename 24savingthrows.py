## Saving Throw
import random

def roll_d20():
    return random.randint(1, 20)
    
def saving_throws(dc, advantage, disadvantage):
    successes = 0
    num_simulations = 10000
    
    for i in range(num_simulations):
        
        if advantage:
            roll = max(roll_d20(), roll_d20())
        elif disadvantage:
            roll = min(roll_d20(), roll_d20())
        else:
            roll = roll_d20()
        
        if roll >= dc:
            successes += 1
    return successes / num_simulations

dcs = [5, 10, 15]
scenarios = [("", False, False), ("Advantage", True, False), ("Disadvantage", False, True)]

print(f"{'DC':<10}{'Normal':<15}{'Advantage':<15}{'Disadvantage':<15}")

for dc in dcs:
    print(f"{dc:<10}{saving_throws(dc, False, False)*100:<15.2f}{saving_throws(dc, True, False)*100:<15.2f}{saving_throws(dc, False, True)*100:<15.2f}")