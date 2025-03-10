# Bellman-equation
Practice code for Bellman's equation
# Value Iteration and Random Movement Simulations

This repository contains two main Python scripts that simulate different strategies for moving in a 1D environment: one using random actions to observe the total reward (`Basic_situation.py`) and another using value iteration and Bellman equations to determine the optimal policy (`get_value.py`).

## Basic Situation: Random Movement Simulation (`Basic_situation.py`)

### Overview
This script simulates a random movement process in a 1D grid, where the agent moves left or right based on a random decision. The goal is to observe the total reward accumulated during these random movements.

Calculate <state value function > and <Action value function> and <Bellman equation>.
This graph is difference of calculated value of state and bellman value
![Image](https://github.com/user-attachments/assets/8b243bf3-ad5b-46b2-bd86-cb8adf734465)
### How it works:
- The agent can move between two states (S0 and S1) on the grid.
- The action is chosen randomly, either left (-1) or right (+1).
- The reward is determined based on the state and the chosen action.
- The total reward over 200 steps is tracked and displayed as a bar chart comparing random action rewards to the Bellman optimal values.

### Output:
- A bar chart showing the total reward from random actions (`random`) and the Bellman values (`Bellman`).
- The bar chart is saved as `Compare Result.jpg`.
![Image](https://github.com/user-attachments/assets/5f902278-8226-48d4-bc5f-c1fe854a6251)
### Dependencies:
- `numpy`
- `matplotlib`

### Running the Script:
`python Basic_situation.py`

`python get_value.py`
