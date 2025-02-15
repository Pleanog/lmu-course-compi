

> [!CITE] **Definition 12 (Multi-Agent System)**  
> Let $G=\{G^{[1]},\dots,G^{[N]}\}$ be a set of $|G| = N$ agents, where each agent $G^{[i]}$ has its own observation space $O^{[i]}$ and action space $A^{[i]}$. These are controlled by individual policies $\pi^{[i]}$ for all $i = 1,\dots,N$.  
> The multi-agent system $G$ then takes a joint action $a \in A$, where $A = A^{[1]} \times \dots \times A^{[N]}$, after making a joint observation $o \in O$, where $O = O^{[1]} \times \dots \times O^{[N]}$. The joint action $a$ is determined by the joint policy $\pi(o^{[1]}, \dots, o^{[N]}) = (a^{[1]}, \dots, a^{[N]})$, where $a^{[i]} = \pi^{[i]}(o^{[i]})$ for all $i$.

---

## ELI5

Imagine a team of robots (agents) working together to clean a house. Each robot has its own "eyes" (observation space) and "hands" (action space). Each robot also has its own way of deciding what to do (its policy).

When they work together, they take in all their observations (what each robot sees) and make a joint decision (a combined action). This decision is based on each robot's policy, which tells it what to do based on what it sees.

So, the multi-agent system is just a fancy way of describing a team of agents that observe their surroundings, decide what to do, and act together in a coordinated way.

---

## Components of the Definition

1. **Agents ($G$):** A group of $N$ agents, denoted as $G^{[1]},…,G^{[N]}$, where each agent operates individually.
    
2. **Observation Spaces ($O^{[i]}$):** Each agent has its own set of observations it can make about the environment.
    
3. **Action Spaces ($A^{[i]}$):** Each agent has its own set of actions it can take based on its observations.
    
4. **Policies ($\pi^{[i]}$):** Each agent has a policy—a rule or function that determines its actions based on its observations.
    
5. **Joint Observation ($o$):** The combined observations of all agents, represented as $o = (o^{[1]}, \dots, o^{[N]})$.
    
6. **Joint Action ($a$):** The combined actions of all agents, represented as $a = (a^{[1]}, \dots, a^{[N]})$.
    
7. **Joint Policy ($\pi$):** The overall policy that combines the individual policies of all agents to determine the joint action based on the joint observation.
    

---

## Explanation

The definition describes how a **multi-agent system** works:

- A group of agents operates together. Each agent has its own way of observing the environment and its own set of possible actions.
- The agents observe their surroundings individually, and their observations are combined into a joint observation.
- Based on this joint observation, the agents decide on a joint action using their combined policies.
- This system enables the agents to work collaboratively, even though each agent acts based on its own rules and observations.

For example, in a drone delivery system, each drone (agent) observes its location and the location of nearby drones. Using their individual policies, they decide their actions (e.g., flying to a package or avoiding a collision). Together, they achieve the overall goal of efficient and safe delivery.

---

## Summary

A multi-agent system consists of multiple agents, each with its own observation and action spaces, controlled by individual policies. The system operates by combining the agents' observations into a joint observation, which is used to determine a joint action based on a joint policy. This allows the agents to act collaboratively in a coordinated manner.