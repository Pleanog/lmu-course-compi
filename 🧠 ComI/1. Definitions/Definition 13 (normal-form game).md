
> [!CITE] **Definition 13 (normal-form game):** 
> Let $G = \{G^{[1]}, \ldots, G^{[N]}\}$ be a set of $|G|=N$ agents. Let $\mathcal{A} = \mathcal{A}^{[1]} \times \ldots \times \mathcal{A}^{[N]}$ be the space of joint actions where $\mathcal{A}^{[i]}$ is the set of actions available to agent $G^{[i]}$ for all  $i$. Let $\chi: \mathcal{A} \to \mathcal{T}$ be a utility function for the joint action space $\mathcal{A}$ and the joint target space $\mathcal{T} = \mathcal{T}^{[1]} \times \ldots \times \mathcal{T}^{[N]}$ where $\mathcal{T}^{[i]}$ is the target space of agent $G^{[i]}$ for all $i$. Unless stated otherwise, the utility $\chi$ is to be maximized. From $\chi$, we can derive a set of single-agent utility functions $\chi^{[i]} : \mathcal{A} \to \mathcal{T}^{[i]}$  for all $i$. A tuple $(G, \mathcal{A}, \mathcal{T}, \chi)$ is called a **normal-form game**. 

## ELI5

A **normal-form game** describes a scenario where multiple players (agents) act independently, each choosing from their own set of possible actions. The actions of all players together determine an outcome (called the utility or reward), which is represented as a number. Each player wants to maximize their own utility, and the definition lays out how these utilities are calculated based on everyone's actions.

Imagine a group of friends deciding on a dinner place. Each friend (agent) has their own preferences (action choices) like pizza, sushi, or burgers. Once everyone makes a choice, their combined decision determines how satisfied (utility) each person feels about the dinner spot.

---

## Components of the Definition

1. **Agents ($G$):**  
    A set of $N$ agents ($G^{[1]}, G^{[2]}, \ldots, G^{[N]}$), each representing an individual decision-maker.
    
2. **Action Space ($\mathcal{A}$):**  
    The space of all possible combinations of actions taken by all agents. Each agent $G^{[i]}$ has their own set of available actions $\mathcal{A}^{[i]}$.
    
3. **Utility Function ($\chi$):**  
    Maps the combined actions of all agents ($\mathcal{A}$) to a reward or outcome in the joint target space $\mathcal{T}$. This utility measures how favorable the outcome is for the agents.
    
4. **Target Space ($\mathcal{T}$):**  
    The space of possible rewards, expressed as $\mathcal{T} = \mathcal{T}^{[1]} \times \ldots \times \mathcal{T}^{[N]}$, where each $\mathcal{T}^{[i]}$ represents the personal rewards of agent $G^{[i]}$.
    
5. **Derived Utilities ($\chi^{[i]}$):**  
    Each agent $G^{[i]}$ has an individual utility function $\chi^{[i]}$ that determines their personal reward based on the joint actions $\mathcal{A}$.
    
6. **Tuple $(G, \mathcal{A}, \mathcal{T}, \chi)$:**  
    This formalizes the structure of a normal-form game, summarizing the agents, their actions, possible rewards, and utility function.
    

---

## Explanation

In a **normal-form game**, each agent independently chooses an action from their action set $\mathcal{A}^{[i]}$. The combination of all these actions forms a "joint action" in $\mathcal{A}$, which determines a reward or utility for every agent based on the function $\chi$. The reward for each agent is specific to their target space $\mathcal{T}^{[i]}$.

To put it simply:

- Each agent decides on their action without knowing what the others will do.
- The joint decision (all agents' actions together) leads to rewards for everyone.
- The goal for each agent is to pick actions that maximize their own reward.

The German note explains that agents don’t need extra information to act—they can simply choose an action from their action set, and the result (reward) is derived from the entire system using the utility function $\chi$. The reward is structured within a mathematical space $\mathcal{T}$, which is a Cartesian product of individual reward spaces for all agents.

---

## Summary

A **normal-form game** models interactions between independent agents, where each chooses actions from their set. These joint actions determine outcomes (utilities) for all agents via a utility function. The goal is to maximize rewards, and the system is defined using a tuple $(G, \mathcal{A}, \mathcal{T}, \chi)$.