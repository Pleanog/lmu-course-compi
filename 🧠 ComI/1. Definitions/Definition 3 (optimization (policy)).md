
> [!CITE] Definition 3 (optimization (policy))
> 
> Let $\mathcal{X} = \Pi$ be a policy space. Let $\mathcal{D} = (\Pi, \mathcal{T}, \tau, e, \langle x_t \rangle_{0 \leq t \leq g})$ be an optimization process according to Definition 2. $\mathcal{D}$ is called a policy optimization process.
## ELI5

Policy optimization is a special type of optimization where the goal is to find the best strategy (policy) for solving a problem. A chess player  trying to develop a strategy to win. Each possible strategy you could use is part of the policy space ($\Pi$), and the "goodness" as a player is evaluated by a target function ($\tau$), which could measure how many games are beeing won or how quickly a checkmate occurs.

Starting with one strategy ($x_0$), the Optimisation Process analyzes its performance and adjust it step by step using a process similar to [[Definition 2 (optimisation)]]. At each step, it makes improvements to the strategy based on your past games and results. The goal is to refine the approach until the best possible strategy for playing chess was found. This specific focus on optimizing strategies is what makes policy optimization different from general optimization.

---

## Components of the Definition

1. **Policy Space ($\Pi$):**
    Represents the set of all possible policies (decision-making strategies).
2. **Optimization Process ($D$):**
    Defined according to Definition 2 as $(\mathcal{X}, \mathcal{T}, \tau, e, \langle x_t \rangle_{0 \leq t \leq g})$.
3. **Policy Optimization Process:**
    An optimization process where $\mathcal{X} = \Pi$.

---
## Explanation

Policy optimization focuses on finding the best decision-making strategy (policy). It treats policies as the states to be optimized, applying the principles from Definition 2 to search for the optimal policy within $\Pi$.

![[Pasted image 20241210114854.png]]
![[Pasted image 20241210114832.png]]
![[Pasted image 20241210114846.png]]

These maps illustrate the **Solution Landscape Metaphor**, where the x- and y-axes represent the policy space $\pi$, and the z-axis represents the target function $\tau(\pi)$ as defined in  [[Definition 2 (optimisation)]]. The surface reflects the values of $\tau(\pi)$ across all possible policies in $\pi$, forming a rugged landscape of peaks and valleys. Peaks correspond to local maxima, while valleys correspond to local minima.
In the context of **Definition 3**, the map visually depicts the optimization process, where an algorithm or search process navigates this landscape to locate an optimal solution (e.g., the deepest valley for minimization). The z-axis (the height of the surface) represents the value of $\tau(\pi)$, while the x- and y-axes show the various policies $\pi$, emphasizing the complexity of the problem space and the challenges of avoiding local optima while searching for the global optimum.

---
## Summary

Definition 3 extends [[Definition 2 (optimisation)]]. by specifying that the states being optimized are policies themselves. It describes a process for finding the optimal strategy among many.