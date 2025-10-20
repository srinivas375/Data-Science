import pickle
from matplotlib import pyplot as plt
import numpy as np
import gymnasium as gym

# import warnings
# warnings.filterwarnings("ignore", category=UserWarning)


# Training environment (no rendering)
env = gym.make('FrozenLake-v1', is_slippery=False, map_name='8x8')

# Q-table
state_size = env.observation_space.n
action_size = env.action_space.n
Q = np.zeros((state_size, action_size))

# Hyperparameters
alpha = 0.8
gamma = 0.95
epsilon = 1.0
epsilon_decay = 0.999
epsilon_min = 0.01
episodes = 15000
max_steps = 1000


# Training
print("Training started .....")
for episode in range(episodes):
    state, info = env.reset()
    done = False

    for step in range(max_steps):
        # Epsilon-greedy policy
        if np.random.rand() < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(Q[state])

        # Environment response
        next_state, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated

        # Q-learning update
        Q[state, action] = Q[state, action] + alpha * (
            reward + gamma * np.max(Q[next_state]) - Q[state, action]
        )

        state = next_state

        if done:
            break

    # Decay epsilon
    if epsilon > epsilon_min:
        epsilon *= epsilon_decay

print("Training completed.")
print("Learned Q-table:")
print(Q)


# save Q-table to a .pkl file
with open("q_table.pkl", 'wb') as f:
    pickle.dump(Q, f)
print("Q-table saved to q_table.pkl")



# Test (with rendering)
test_env = gym.make('FrozenLake-v1', is_slippery=False, render_mode='human', map_name='8x8')
state, info = test_env.reset()
done = False
while not done:
    action = np.argmax(Q[state])
    state, reward, terminated, truncated, info = test_env.step(action)
    test_env.render()
    done = terminated or truncated
    print("Reward is:", reward)

env.close()
test_env.close()