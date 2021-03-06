# -*- coding: utf-8 -*-
"""RL_qlearning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1By9xyEQfc1tFk_6IXc26aJdBul3SpuLo
"""

import numpy as np
import random
Q = np.zeros([16, 4])
num_episodes = 1000

def rargmax(vector):
    m = np.amax(vector) # Return the maximum of an array or maximum along an axis (0 or 1)
    indices = np.nonzero(vector == m)[0] # np.nonzero(True/False vector) => find the maximum 
    return random.choice(indices) # Random selection
# action: 0->L, 1->D, 2->R, 3->U
'''
def RL_step(state,action):
  # state 0
  if state == 0:
    if action == 0:
      new_state = 0
      reward = 0
      done = None
    elif action == 1:
      new_state = 4
      reward = 0
      done = None
    elif action == 2:
      new_state = 1
      reward = 0
      done = None
    elif action == 3:
      new_state = 0
      reward = 0
      done = None
  # state 1
  elif state == 1:
    if action == 0:
      new_state = 0
      reward = 0
      done = None
    elif action == 1:
      new_state = 5
      reward = 0
      done = None
    elif action == 2:
      new_state = 2
      reward = 0
      done = None
    elif action == 3:
      new_state = 0
      reward = 0
      done = None
  # state 2
  elif state == 2:
    if action == 0:
      new_state = 1
      reward = 0
      done = None
    elif action == 1:
      new_state = 6
      reward = 0
      done = None
    elif action == 2:
      new_state = 3
      reward = 0
      done = None
    elif action == 3:
      new_state = 0
      reward = 0
      done = None

  return new_state, reward, done
'''
def RL_step(state,action):
  if action == 0: #left
    if state % 4 == 0:
      new_state = state
    else:
      new_state = state - 1
  elif action == 1: #down
    if state > 11:
      new_state = state
    else:
      new_state = state + 4
  elif action == 2: #right
    if (state+1) % 4 ==0:
      new_state = state
    else:
      new_state = state +1
  else: #up
    if state < 4:
      new_state = state
    else:
      new_state = state - 4
  if new_state == 15:
    reward = 1
  elif (new_state == 5) or (new_state == 7) or (new_state == 11) or (new_state == 12):
    new_state = state
    reward = 0
  else:
    reward = 0
  if new_state == 15:
    done = True
  else:
    done = None
  return new_state, reward, done

for i in range(num_episodes):
  state = 0
  total_reward = 0
  done = None

  while not done:
    action = rargmax(Q[state,:])
    new_state, reward, done = RL_step(state, action)
    Q[state, action] = reward + np.max(Q[new_state, :])
    total_reward += reward
    state = new_state
print(Q)