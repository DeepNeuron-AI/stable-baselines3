import numpy as np
import gym

class DiscreteActionForceConversion(gym.ActionWrapper):
    def action(self, action):
        return int(action)
    
    def reverse_action(sef, action):
        return np.array(action)