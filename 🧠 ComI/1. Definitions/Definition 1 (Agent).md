
> [!CITE] Definition 1 (agent)
> Let $\mathcal{A}$ be a set of actions. Let $\mathcal{O}$ be a set of observations. An agent "A" can be given via a **policy function** $\pi : \mathcal{O}\to\mathcal{A}$. Given a time series of observations $\langle\mathcal{o}_t\rangle_{t\in\mathcal{Z}}$ for some **time space** $\mathcal{Z}$, the agent can thus generate a time series of actions $\langle a_t\rangle_{t\in\mathcal{Z}}$ by applying $a_t = \pi(\mathcal{o}_t)$.

## ELI5

An **agent** operates by perceiving its environment and performing actions based on those perceptions. This definition introduces the relationship between the **observation space** (Θ or O), the **action space** (𝒜 or A), and a **policy function** (𝜋) that governs the agent's behavior.

---

### Components of the Definition

1. **Action Space ($\mathcal{A}$):**  
    The set of all possible actions that the agent can perform. For example, in a cleaning robot scenario, the action space could include `{vacuum, move_to_room_A, move_to_room_B, do_nothing}`.
2. **Observation Space ($\mathcal{O}$):**  
    The set of all possible observations the agent can make about its environment. An observation provides the agent with information about the current state of the world, such as whether a room is clean or dirty, or which room the agent is currently in.
3. **Policy Function (𝜋):**  
    A function that maps observations (𝑜ₜ ∈ O) to actions (𝑎ₜ ∈ A). The policy function defines how the agent chooses an action based on its current observation. Formally, this is expressed as: $$\pi : \mathcal{O}\to\mathcal{A}$$
4. **Time Space ($\mathcal{Z}$):**  
    Observations and actions occur sequentially over time. The time space ($\mathcal{Z}$ represents this sequence, allowing the agent to process a time series of observations $\langle\mathcal{o}_t\rangle_{t\in\mathcal{Z}}$ and generate a corresponding time series of actions $\langle a_t\rangle_{t\in\mathcal{Z}}$.


---

### Explanation of the Policy Function

The policy function (𝜋) is central to the agent's operation. It takes an observation as input and determines the appropriate action to take. For example:

- Observation: `(current_room = A, is_dirty = True)`
- Action: `vacuum`.

![[Pasted image 20241205155501.png]]
"One Observation leads to an action based on the policy that was given"

This function encapsulates the agent's decision-making process, allowing it to interact with its environment in a structured and consistent manner.

---

### Summary
An agent uses observations from its environment to determine actions through a policy function. Over time, the agent continuously observes the environment and acts accordingly, forming a sequence of observations and actions. This framework enables the systematic design of intelligent agents that can operate in dynamic environments.

---
---

The expression $\langle a_t \rangle_{t \in \mathcal{Z}}$​ represents the **expectation** or **average** of the quantity $a_t$​ over a set of time steps or indices $t$ that belong to the set $\mathcal{Z}$. Specifically, it refers to the expected value (or mean) of the sequence $a_t$​ for all $t$ within the set $\mathcal{Z}$.

The angle brackets $\langle \cdot \rangle$ typically indicate this expectation, where:

- $a_t$​ is the variable or function of interest at each time step $t$.
- $\mathcal{Z}$ is the index set, which could be a range of time steps or any other set of indices.

### Alternative Representations

This can also be expressed in different ways, depending on the context:

1. **Integral or sum representation**: If $\mathcal{Z}$ is a continuous set, this can be written as an integral:
    $$\langle a_t \rangle_{t \in \mathcal{Z}} = \int_{\mathcal{Z}} a_t \, dt$$
    
    For a discrete set Z={t1,t2,…,tn}\mathcal{Z} = \{t_1, t_2, \dots, t_n\}Z={t1​,t2​,…,tn​}, the expectation can be written as:
    
    $\langle a_t \rangle_{t \in \mathcal{Z}} = \frac{1}{|\mathcal{Z}|} \sum_{t \in \mathcal{Z}} a_t$
    
    where $|\mathcal{Z}|$ is the cardinality of the set $\mathcal{Z}$.
    
2. **Statistical expectation notation**: If the context involves a probability distribution PPP, you could express this expectation as:
    
    $\mathbb{E}_{t \in \mathcal{Z}}[a_t]$
    
    where $\mathbb{E}$ denotes the expected value with respect to some probability distribution over $t$.
    

Thus, depending on whether you're dealing with a continuous or discrete set and the underlying probabilistic structure, the expression might change, but the meaning remains centered around the concept of averaging or expectation over a set of values indexed by $t$.