import numpy as np
import matplotlib.pyplot as plt

reward = {
0: [(-1, 0), (1, 1)],  
1: [(0, 0), (-1, 1)]   
        }
t=[]
class State_Value_Function():
    def __init__(self,gamma):
        self.gamma = gamma
        self.P_action = 0.5
        self.V = np.zeros(2)  
        

    def calculate_value(self):
        
        for s in range(2):
            value = 0
            for action, (reward_value, next_state) in enumerate(reward[s]):
                value += self.P_action * (reward_value + self.gamma * self.V[next_state])
            self.V[s] = value   
        t.append(self.V.copy())     
        return self.V

def calculate_state_value():
    
    for _ in range(100):  
        state_value_func.calculate_value()
    
    return state_value_func.V[0],state_value_func.V[1]
    

class Bellman_Equation():
    def __init__(self, gamma=0.9):
        self.gamma = gamma
        A = np.array([
            [1, -self.gamma],  
            [-self.gamma, 1]   
        ])
        b = np.array([1, 0])  # 보상 값

        # 방정식 풀이
        self.B = np.linalg.solve(A, b)
    
def calculate_bellman_value():
    return bellman_eq.B[0],bellman_eq.B[1]
    

class Action_Value_Function():
    def __init__(self,gamma):
        self.gamma = gamma
        
    def calculate_value(self,value_0,value_1):
        value_list = np.array([value_0,value_1])
        self.value = np.zeros((2,2))
        for s in range(2):
            for action, (reward_value, next_state) in enumerate(reward[s]):
                self.value[s][action] = reward_value + self.gamma * value_list[next_state]
        return self.value
    
def calculate_action_value(v1,v2):
    action_value_result = action_value_func.calculate_value(v1,v2)
    
    return action_value_result

def policy(action_value_list):
    for i in range(2):
        if max(action_value_list[i])==action_value_list[i][1] : 
            print(f"S{i}'s optimal policy : ->")
        else : 
            print(f"S{i}'s optimal policy : <-")

def draw():
    plt.figure(figsize=(10, 6))
    plt.title("<State Value over Time>", fontsize=16)
    plt.xlabel('Iterations', fontsize=12)
    plt.ylabel('State Value', fontsize=12)
    plt.plot(t, label='State Value', color='b', lw=2)
    plt.axhline(y=5.263157894736843, color='r', linestyle='--', label="Bellman Value (S0)")
    plt.axhline(y=4.736842105263159, color='black', linestyle='--', label="Bellman Value (S1)")
    plt.legend(loc='best', fontsize=10)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.tight_layout()
    plt.savefig("Result.jpg")
    plt.show()


if __name__ == "__main__":
    state_value_func = State_Value_Function(gamma=0.9)
    bellman_eq = Bellman_Equation(gamma=0.9)
    action_value_func = Action_Value_Function(gamma=0.9)

    V_0,V_1 = calculate_state_value()
    print("100 times state value:")
    print(f"V(S0) = {V_0}")
    print(f"V(S1) = {V_1}")
    print("--------------------------------")

    B_0,B_1 = calculate_bellman_value()
    print("Bellman_Reult:")
    print(f"V(S0) = {B_0}")
    print(f"V(S1) = {B_1}")
    print("--------------------------------")

    state_action_value_result = calculate_action_value(V_0,V_1)
    bellman_action_value_result = calculate_action_value(B_0,B_1)

    print(f"State Value's Action Value :\n {state_action_value_result}")
    policy(state_action_value_result)
    print("--------------------------------")
    print(f"Bellman Value's Action Value :\n {bellman_action_value_result}")
    policy(bellman_action_value_result)
    print("--------------------------------")

    draw()
    
    
