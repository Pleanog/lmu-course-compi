
> [!CITE] **Definition 16 (strategy):**  
Let $(G, \mathcal{A}, \mathcal{T}, \chi)$ be a normal-form game. In a single iteration of the game, an agent $G^{[i]}$'s behavior is given by a (possibly randomized) policy $\pi^{[i]} : () \to \mathcal{A}^{[i]}$. Then, $\pi^{[i]}$ is also called $G^{[i]}$'s **strategy**.  
If multiple iterations of the game are played, an agent $G^{[i]}$'s behavior can be given by a (possibly randomized) policy $\pi^{[i]} : \mathcal{A}^n \to \mathcal{A}^{[i]}$ where $n$ is the number of previous iterations. The agent's strategy is then conditioned on a list of previous joint actions.
> - An agent $G^{[i]}$ whose actions are given via a policy $\pi^{[i]}(-) = a^{[i]}$ for some action $a^{[i]} \in \mathcal{A}^{[i]}$ is playing a **pure strategy**.
> - An agent $G^{[i]}$ whose actions are given via a policy $\pi^{[i]}(-) \sim \mathcal{A}^{[i]}$ according to some distribution over $\mathcal{A}^{[i]} \subseteq \mathcal{A}^{[i]}$ is playing a **mixed strategy**.
>- If a mixed strategy is based on a uniform distribution over actions $\mathcal{A}^{[i]} \subseteq \mathcal{A}^{[i]}$, we write $\pi^{[i]} = \mathcal{A}^{[i]}$ as a shorthand.

## ELI5

A **strategy** is like a plan or rulebook that tells a player in a game how to act. It’s the logic behind their decisions.

There are two main types of strategies:
1. **Pure Strategy**:  
    The player always chooses the same specific action every time. Think of it like someone always picking "rock" in a game of rock-paper-scissors.
2. **Mixed Strategy**:  
    The player doesn't always pick the same action. Instead, they make their choices randomly, based on probabilities. For example, in rock-paper-scissors, they might choose "rock" 50% of the time, "paper" 30% of the time, and "scissors" 20% of the time.

---

## Components of the Definition

All the Agents $G$ share a combined $\mathcal{A}$ and a shared the utility function $\chi$ aswell as the Targetspace $\mathcal{T}$

1. **Normal-Form Game $(G, \mathcal{A}, \mathcal{T}, \chi)$**:  
    The framework of the game, as defined in [[Definition 13 (normal-form game)]].
2. **Agent's Behavior as a Policy $\pi^{[i]}$**:
    - A **policy** is a function (or rule) that tells the agent ($G^{[i]}$) what action to take.
    - If the game is played once, the policy maps directly to an action:  
        $\pi^{[i]} : () \to \mathcal{A}^{[i]}$.
    - If the game is played multiple times, the policy can depend on the previous actions:  
        $\pi^{[i]} : \mathcal{A}^n \to \mathcal{A}^{[i]}$, where $n$ is the number of past rounds.
3. **Pure vs. Mixed Strategies**:
    - **Pure Strategy**:  
        Always picks the same action, e.g., $\pi^{[i]}(-) = a^{[i]}$.
    - **Mixed Strategy**:  
        Picks actions randomly according to a probability distribution, e.g.,  
        $\pi^{[i]}(-) \sim \mathcal{A}^{[i]}$. Here we choose the further action from the subset of the possible actions $A^{[i]}\subseteq A^{[i]}$. If not further defined we assume the distibution is equally distributed.
4. **Uniform Mixed Strategy**:  
    If the mixed strategy is based on a uniform distribution (all actions equally likely), we write it as $\pi^{[i]} = \mathcal{A}^{[i]}$ for simplicity.

---

## Explanation

A **strategy** is simply a way for a player to decide what to do in a game. It can be a fixed plan (pure strategy) or involve randomness (mixed strategy).

- **Single Game**: The strategy only needs to decide what to do once.
- **Multiple Games**: The strategy might consider past actions to decide what to do next.

### Why Is This Useful?

Strategies are key to analyzing how players behave in games and how outcomes are determined. Understanding strategies helps us figure out the best way to play a game, especially when other players are unpredictable or when randomness is involved.

---

## Summary

A **strategy** is a plan that dictates an agent’s actions in a game.

- **Pure Strategy**: Always picks the same action.
- **Mixed Strategy**: Chooses actions randomly based on probabilities.
- **Uniform Mixed Strategy**: All actions are equally likely.

Strategies can consider the history of previous actions in games with multiple rounds.