import random
import numpy as np

def epsilon_greedy(q_values, epsilon=0.1):
    if np.random.rand() <= epsilon:
        return random.choice(range(len(q_values)))
    else:
        return np.argmax(q_values)


class Agent:
    """ Base class of an autonomously acting and learning agent. """

    def __init__(self, params):
        self.nr_actions = params["nr_actions"]

    def policy(self, state):
        """ Behavioral strategy of the agent. Maps states to actions. """
        pass

    def update(self, state, action, reward, next_state, done):
        """ Learning method of the agent. Integrates experience into the agent's current knowledge. """
        pass
        

class RandomAgent(Agent):
    """ Randomly acting agent. """

    def __init__(self, params):
        super(RandomAgent, self).__init__(params)
        
    def policy(self, state):
        return random.choice(range(self.nr_actions))


class SARSALearner(Agent):
    """ Autonomous agent using SARSA. """

    def __init__(self, params):
        super(SARSALearner, self).__init__(params)
        self.gamma = params["gamma"]
        self.alpha = params["alpha"]
        self.epsilon = params["epsilon"]
        self.q_values = dict()
        self.action_count = np.zeros(self.nr_actions)
        
    def q_table(self, state):
        state = np.array2string(state)
        if state not in self.q_values:
            self.q_values[state] = np.zeros(self.nr_actions)
        return self.q_values[state]

    def policy(self, state):
        q_values = self.q_table(state)
        return epsilon_greedy(q_values, None, epsilon=self.epsilon)

    def update(self, state, action, reward, next_state, done):
        # ***
        # TODO: Implement SARSA update
        # ***        
        pass
        