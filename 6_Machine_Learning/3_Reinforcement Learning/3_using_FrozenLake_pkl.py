import pickle
import gymnasium as gym
import numpy as np
import warnings

warnings.filterwarnings('ignore', category=UserWarning)

with open('q_table.pkl', 'rb') as f:
    Q = pickle.load(f)

env = gym.make('FrozenLake-v1', is_slippery=False, render_mode='ansi')

state, info = env.reset()
done = False

while not done:
    action = np.argmax(Q[state])

    new_state, reward, terminated, truncated, info = env.step(action)
    done = terminated or truncated
    print(env.render())
    print(type(env.render()))
    print("Reward:", reward)
    state = new_state
env.close()