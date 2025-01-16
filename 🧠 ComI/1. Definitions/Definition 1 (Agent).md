
> [!CITE] Definition 1 (agent)
> Let 𝒜 be a set of actions. Let 𝛕 be a set of observations. An agent "A" can be given via a **policy function** 𝜋 : Θ → 𝒜. Given a time series of observations ⟨𝑜ₜ⟩ₜ∈ℤ for some **time space** ℤ, the agent can thus generate a time series of actions ⟨𝑎ₜ⟩ₜ∈ℤ by applying 𝑎ₜ = 𝜋(𝑜ₜ).

## ELI5

An **agent** operates by perceiving its environment and performing actions based on those perceptions. This definition introduces the relationship between the **observation space** (Θ or O), the **action space** (𝒜 or A), and a **policy function** (𝜋) that governs the agent's behavior.

---

### Components of the Definition

1. **Action Space (𝒜):**  
    The set of all possible actions that the agent can perform. For example, in a cleaning robot scenario, the action space could include `{vacuum, move_to_room_A, move_to_room_B, do_nothing}`.
    
2. **Observation Space (𝛕 or O):**  
    The set of all possible observations the agent can make about its environment. An observation provides the agent with information about the current state of the world, such as whether a room is clean or dirty, or which room the agent is currently in.
    
3. **Policy Function (𝜋):**  
    A function that maps observations (𝑜ₜ ∈ O) to actions (𝑎ₜ ∈ A). The policy function defines how the agent chooses an action based on its current observation. Formally, this is expressed as:  
    𝜋: 𝛕 → 𝒜.
    
4. **Time Space (ℤ):**  
    Observations and actions occur sequentially over time. The time space ℤ represents this sequence, allowing the agent to process a time series of observations ⟨𝑜ₜ⟩ₜ∈ℤ and generate a corresponding time series of actions ⟨𝑎ₜ⟩ₜ∈ℤ.
    

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