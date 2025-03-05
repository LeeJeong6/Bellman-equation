import numpy as np
import random

'''
Grid-based Random Movement Simulation

   _____________
   | L 0 | L 1 |     
   |     |  *  |     
   |_____|_____|  

- The agent starts at L0.
- It randomly moves left (-1) or right (+1).
- If it moves to L1 → get * (Reward = +1).
- The * resets when returning to L0
- If it moves out of bounds (-1 or 2) → Reward = -1.
- Otherwise, Reward = 0.

'''
grid = np.array([0, 1])
total_reward = 0 
def action(state):
    pi = random.choice([-1, 1]) 
    new_state = state + pi

    if new_state in (-1, 2):
        return min(state, abs(new_state)), -1
    return new_state, int(new_state == 1)

if __name__ == "__main__":
    x = grid[0]
    print(f"Start_Point : {x}")

    for i in range(5):
        x, reward = action(x)
        total_reward+=reward
        print(f"{i+1}'st : {x} state, reward : {reward}")
    print(f"Total Reward  : {total_reward}")