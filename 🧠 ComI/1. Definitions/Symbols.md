#### **Mathematical Symbols**
- **$\mathcal{O}$** : Represents the **observation space**, containing all possible observations an agent can receive from the environment.
- **$\mathcal{S}$** : Represents the **state space**, the set of all possible configurations of the environment.
- **$\mathcal{A}$** : Represents the **action space**, containing all possible actions an agent can take.
- **$\mathbb{R}$**: The set of real numbers, often used for rewards, probabilities, or continuous actions.
- **$T$**: Represents **timestamps** for observations or timesteps in a sequence.
- **$\times$** (Cartesian product): Used to construct spaces where multiple variables exist, e.g., combining state and action spaces into tuples.
- **$\mathbb{B}$**: Represents the set of **Boolean values** $\{ \text{true}, \text{false} \}$.

---

### **Policy Function $\pi$**
A **policy** ($\pi$) is a function that tells an agent what action to take based on its current state.

##### **Mathematical Definition**
A policy maps a **state space** to an **action space**:
$$\pi:\mathcal{S}\to\mathcal{A}$$
where:
- $\mathcal{S}$ is the **state space** (set of all possible states the agent can be in).
- $\mathcal{A}$ is the **action space** (set of all possible actions the agent can take).
- $\pi(s)$ is the action the agent takes when in state $s$.

Alternatively, if the agent does not have direct access to the true state and must rely on **observations**, then the policy can be defined as:
$$\pi:\mathcal{O}\to\mathcal{A}$$
where:
- $\mathcal{O}$ is the **observation space** (what the agent perceives).
- $\pi(o)$ is the action the agent takes given observation $o$.

#### **Example**
$$\pi : \mathcal{L} \times \mathcal{L} \to \mathbb{R} \times \mathbb{R} \times \mathbb{B}$$
Here:
- **State space**: Two concartinated Locations ($\mathcal{L}$) of the agent and the target.
- **Action space**: Movement in $x$- and $y$-directions ($\mathbb{R} \times \mathbb{R}$) and a Boolean value ($\mathbb{B}$) indicating whether a special action (e.g., picking something up) is taken.

---

### **Goal Predicate $\gamma$**
A **goal predicate** is a function that checks whether the agent has achieved its goal. It does **not** influence decisions like a policy or assign numerical rewards like a reward function. Instead, it acts as a logical condition.

##### **Mathematical Definition**
$$\gamma: \mathcal{S} \to \mathbb{B}$$
where:
- $\gamma(s) = \text{true}$ if the agent is in a goal state.
- $\gamma(s) = \text{false}$ otherwise.

##### **Example**
If the goal is to reach position $(x_{\text{goal}}, y_{\text{goal}})$, then:
$$\gamma(s) = \begin{cases} 
\text{true}, & \text{if } s = (x_{\text{goal}}, y_{\text{goal}}) \\ 
\text{false}, & \text{otherwise} 
\end{cases}$$
This means the goal is **fulfilled only if** the agent reaches the target position.

---

### **Reward Function $R$**
A **reward function** assigns a numerical score to an agent’s actions, indicating how good or bad they are.

##### **Mathematical Definition**
$$R: \mathcal{S} \times \mathcal{A} \to \mathbb{R}$$
where:
- $R(s, a)$ is the **reward** received when taking action $a$ in state $s$.
- Higher values mean better outcomes, while lower values indicate penalties.

##### **Example**
A robot navigating a grid have the following **reward function**:
$$
\mathcal{R}(s_t, a_t, s_{t+1}) =
\begin{cases}
+10 & \text{if } s_{t+1} = s_{\text{goal}} \\
-1 & \text{if } a_t = a_{\text{wrong}} \\
0 & \text{otherwise}
\end{cases}
$$

- **`+10`** → The agent gets a reward of **+1** if it reaches the goal state $(s_{\text{goal}})$.
- **`-1`** → The agent gets a penalty of **-1** if it takes an incorrect action $(a_{\text{wrong}})$.
- **`0`**   → Otherwise, no reward or penalty is given.

---
### **Comparison: Policy vs. Reward Function vs. Goal Predicate**

- **Policy ($\pi$)** is an **action generator** → "What should I do next?"
- **Reward Function ($R$)** is a **feedback mechanism** → "Was my last action good or bad?"
- **Goal Predicate ($\gamma$)** is a **final condition checker** → "Did I achieve my objective?"
- - **Fitness Function ($\phi$)** is a **solution evaluator** → "How good is my overall performance?"

| Concept                                        | What it does                                                         | Inputs                                                              | Outputs                      | Example                                                      |
| ---------------------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------- | ---------------------------- | ------------------------------------------------------------ |
| [[#$ pi$ **Policy function**\|Policy (π)]]<br> | Decides what action to take in a given state                         | State $s$                                                           | Action $                     | "If the robot is 2 meters away from the goal, move forward." |
| **Reward Function** ($R$)                      | Assigns a numerical value to states/actions to indicate desirability | State $s$, Action $a$, sometimes multible states like $s_t$ or $s'$ | Reward $r$ (a number)        | "+10 if at goal, -1 per step to encourage efficiency."       |
| **Goal Predicate** (γ)                         | A logical condition that checks if a goal has been achieved          | State $s$                                                           | Boolean (true/false)         | "The goal is fulfilled if the robot reaches (x, y)."         |
| **Fitness Function** ($\phi$)                  | Evaluates how good a solution is                                     | Solution $l$                                                        | Natural number $\mathcal{N}$ | "If the robot takes 5 steps, fitness = 5 (lower is better)." |

---

### **$\phi$ Fitness Function** 
$$\phi : \mathcal{L} \to \mathcal{N}$$
### **Explanation**
- The **fitness function** $(\phi)$ assigns a **fitness value** (natural number) to an element in the space $(\mathcal{L})$.
- It measures **how good a solution is** in a given problem context.
- Lower values of $(\phi(l))$ can indicate **better performance** (e.g., less time needed, fewer errors).
- Higher values may indicate **worse performance** (e.g., more time taken, more mistakes).

##### **Example**
If $\mathcal{L}$ represents different **possible solutions** and $\mathcal{N}$ represents **time taken**, then:
$$\phi(l) = \begin{cases} 5 & \text{if solution } l \text{ takes 5 steps} \\ 10 & \text{if solution } l \text{ takes 10 steps} \\ \end{cases}$$

- If the solution takes **5 steps**; $\phi(l) = 5$ (better fitness).
- If the solution takes **10 steps**, $\phi(l) = 10$ (worse fitness).

---

### **Value Function $V$**
The **value function** represents the long-term expected reward starting from a given state.

##### **Mathematical Definition**
$$V^\pi(s) = \mathbb{E} \left[ \sum_{t=0}^{\infty} \gamma^t R(s_t, a_t) \mid s_0 = s \right]$$
where:
- $\mathbb{E}[\cdot]$ is the **expected value**.
- $\gamma$ is the **discount factor** (how much future rewards are valued compared to immediate rewards).
- The summation accounts for **future rewards** over time.


---

### **Utility Function $\chi$**
A **utility function** evaluates how favorable an outcome is for an agent.

##### **Mathematical Definition**
$$\chi: \mathcal{A} \to \mathcal{T}$$
where:
- $\mathcal{T}$ is the target space (e.g., a numerical score or classification).
- $\chi(a)$ represents the utility of an action $a$.

##### **Example**
- In a **multi-agent system**, $\chi$ might evaluate the **combined actions** of all agents to determine how well the group is performing.
- If multiple robots are cooperating, $\chi$ can represent a **team performance score**.

---

### **Transition Function $T$**
The **transition function** defines how the environment evolves based on an agent’s actions.

##### **Mathematical Definition**
$$T: \mathcal{S} \times \mathcal{A} \to \mathcal{S}$$
where:
- $T(s, a)$ gives the next state after taking action $a$ in state $s$.

##### **Example**
- If a robot moves **left** from $(2,3)$, the transition function updates the state to $(1,3)$.

---
