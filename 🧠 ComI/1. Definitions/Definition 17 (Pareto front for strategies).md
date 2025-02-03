
> [!CITE] **Definition 17 (Pareto front for strategies):**  
Let $(G, \mathcal{A}, \mathcal{T}, \chi)$ be a normal-form game. A joint strategy $\pi(\_) = (\pi^{[1]}(-), \ldots, \pi^{[|G|]}(\_))$ **Pareto-dominates** another joint strategy $\pi'(\_) = (\pi^{\prime[1]}(\_), \ldots, \pi^{\prime[|G|]}(\_))$ $iff$ for all agents $G^{[i]}$, it holds that $$\chi^{[i]}(\pi(\_)) \geq \chi^{[i]}(\pi'(\_))$$ and there exists some agent $G^{[j]}$ so that $$\chi^{[j]}(\pi(\_)) > \chi^{[j]}(\pi'(\_))$$.  
A joint strategy $\pi$ is **Pareto-optimal** $iff$ there is no other strategy $\pi'$ so that $\pi'$ Pareto-dominates $\pi$.

## ELI5

The **Pareto front for strategies** is a way to figure out which strategies are "better" in a game when considering all the players involved. It's about fairness and finding strategies where no one can be made better off without making someone else worse off.
A strategie, 

- A strategy that is not dominated by any other strategy is considered **Pareto-optimal**.
- The **Pareto front** is the set of all Pareto-optimal strategies. This means there can be multiple optimal strategies within a game.
- If no strategy dominates the others, then all strategies are Pareto-optimal.

In other words, a **zero-sum game** is always Pareto-optimal because no strategy can improve one player's outcome without reducing the other's.

---

### Step-by-Step Explanation

1. **Joint Strategy**:  
    A **joint strategy** is a combination of strategies chosen by all players in the game. It is written as:  
    $$\pi(-)=(\pi^{[1]}(-),\pi^{[2]}(-),\dots ,\pi^{[|G|]}(-))$$
    Here:
    - $\pi^{[i]}(-)$ represents the strategy chosen by player $G^{[i]}$.
    - $|G|$ is the total number of players.
    
    This simply means: "We are looking at the plan (strategy) of each player in the game together as a group."
    

---

2. **Pareto-Domination**:  
    A joint strategy $\pi$ **Pareto-dominates** another joint strategy $\pi'$ if the following two conditions hold:
    
    - **No player is worse off**:  
        Every player’s payoff using $\pi$ is at least as good as their payoff using $\pi'$. Formally:  
        $\chi^{[i]}(\pi(-)) \geq \chi^{[i]}(\pi'(-)) \quad \text{for all players } G^{[i]}.$
        
    - **At least one player is better off**:  
        There is at least one player who receives a strictly better payoff with $\pi$ compared to $\pi'$. Formally:  
        $\exists , G^{[j]} \quad \text{such that} \quad \chi^{[j]}(\pi(-)) > \chi^{[j]}(\pi'(-)).$
        
    
    In simpler terms, strategy $\pi$ **beats** strategy $\pi'$ because:
    
    - Everyone gets at least the same rewards (no one is worse off).
    - At least one person gets a strictly better reward (someone is happier).

---

3. **Pareto-Optimal**:  
    A joint strategy $\pi$ is considered **Pareto-optimal** if no other joint strategy $\pi'$ exists that Pareto-dominates $\pi$.
    
    Formally:  
    $\nexists , \pi' \quad \text{such that } \pi' \text{ Pareto-dominates } \pi.$
    
    This means:
    
    - It is impossible to find another strategy where some players are better off without making at least one player worse off.

---

### Real-Life Analogy

Imagine you're deciding on a dinner menu for a group of friends:

- **Strategy $\pi$**: Everyone gets food they like, and at least one friend gets their absolute favorite meal.
- **Strategy $\pi'$**: Everyone is still okay with the food, but one friend doesn’t like it as much as they would with $\pi$.

In this case, $\pi$ **Pareto-dominates** $\pi'$, because everyone is as happy or happier, and at least one person is noticeably happier.

- A **Pareto-optimal** menu is one where you can’t make anyone happier without making someone else less happy.

---

### Why Is This Useful?

The **Pareto front** helps us identify the "best" strategies in a game where all players matter. It focuses on fairness and efficiency, making sure no one can improve their outcome at the expense of others.

---

## Summary

- **Pareto-Domination**: Strategy $\pi$ is better than $\pi'$ if no one is worse off, and at least one person is better off.
- **Pareto-Optimal**: A strategy where you can't make anyone better off without making someone else worse off.

This is like finding the most efficient and fair way for everyone to play the game.