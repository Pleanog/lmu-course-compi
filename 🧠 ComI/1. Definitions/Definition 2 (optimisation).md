
>[!CITE] Definition 2 (optimisation)
> Let $\mathcal{X}$ be an arbitrary state space. Let $\mathcal{T}$ be an arbitrary set called target space and let $\leq$ be a total order on $\mathcal{T}$. A total function $\tau : \mathcal{X} \to \mathcal{T}$ is called target function. Optimization (minimization/maximization) is the procedure of searching for an $x \in \mathcal{X}$ so that $\tau(x)$ is optimal (minimal/maximal). Unless stated otherwise, we assume minimization. An optimization run of length $g + 1$ is a sequence of states $\langle x_t \rangle_{0 \leq t \leq g}$ with $x_t \in \mathcal{X}$ for all $t$.
> 
> Let $e : \langle \mathcal{X} \rangle \times (\mathcal{X} \to \mathcal{T}) \to \mathcal{X}$ be a possibly randomized or non-deterministic function so that the optimization run $\langle x_t \rangle_{0 \leq t \leq g}$ is produced by calling $e$ repeatedly, i.e., $x_{t+1} = e(\langle x_u \rangle_{0 \leq u \leq t}, \tau)$ for all $t, 1 \leq t \leq g$, where $x_0$ is given externally (e.g., $x_0 \overset{\text{def}}{=} 42$) or chosen randomly (e.g., $x_0 \sim \mathcal{X}$). An optimization process is a tuple $(\mathcal{X}, \mathcal{T}, \tau, e, \langle x_t \rangle_{0 \leq t \leq g})$.
## ELI5 

Optimization is like a methodical search for the best possible choice among a group of options. Imagine you are trying to find the best possible route for a road trip. The set of all potential routes is the state space ($\mathcal{X}$), and the "goodness" of each route (like the shortest time or most scenic views) is measured by a target function ($\tau$). This target function assigns a value to each route, and you use a rule ($\leq$) to compare these values (e.g., smaller is better if you want the shortest route).

Now, you start at some route ($x_0$), and at each step, you improve your choice based on a strategy ($e$). This strategy evaluates previous routes and decides the next one to try. You keep repeating this process, step by step, until you find the best route. The whole sequence of choices is called an optimization run, and the process is described by putting all the parts (routes, evaluations, rules, and steps) together into a clear structure.

--- 

## Components of the Definition

1. **State Space ($\mathcal{X}$):**
    Represents the set of all possible states or solutions.
2. **Target Space ($\mathcal{T}$):**
    The range of possible values assigned to states by the target function.
3. **Total Order ($\leq$):**
    A way to compare values in $\mathcal{T}$ to determine which is better (e.g., smaller or larger).
4. **Target Function ($\tau: \mathcal{X} \to \mathcal{T}$):**
    Maps states from $\mathcal{X}$ to values in $\mathcal{T}$ and determines their "quality."
5. **Optimization Run:**
    A sequence $\langle x_t \rangle_{0 \leq t \leq g}$ of states from $\mathcal{X}$, where $t$ indexes time steps.
6. **Update Rule ($e$):**
    Determines the next state $x_{t+1}$ given previous states $\langle x_u \rangle_{0 \leq u \leq t}$ and $\tau$.
7. **Optimization Process:**
    Described by the tuple $(\mathcal{X}, \mathcal{T}, \tau, e, \langle x_t \rangle_{0 \leq t \leq g})$, encapsulating all components of optimization.

---
## Explanation
Optimization is about finding the "best" solution within a set of possibilities. The goal is to find a state $x \in \mathcal{X}$ such that $\tau(x)$ achieves an optimal value (e.g., minimum for minimization tasks). The optimization process iteratively updates the state based on the update rule $e$, considering the past and the target function.

![[Pasted image 20241210113200.png]]

 The graph illustrates the relationship between policies $\pi$ (x-axis) and their corresponding target function values $\tau(\pi)$ (y-axis). Points on the graph represent individual policies, with some labeled as "biased sample" and others as "random sample." The biased samples are distributed in a way that appears to prioritize certain regions of the target function values, while the random samples are scattered more uniformly across the x-axis. This distribution highlights the difference in sampling strategies with respect to the target function $\tau(\pi)$.

The correlation suggests that:
 1. **Random sampling** is less directed, exploring the state space more broadly without prioritizing solutions based on $\tau$.
 2. **Biased sampling** integrates the target function $\tau$ into the optimization process, guiding the search toward promising areas of the state space.

This distinction is crucial in optimization because biased sampling typically leads to faster convergence, while random sampling ensures broader exploration.

---

## Summary
This formalizes the process of optimization as finding the best state in a defined set. It defines the components needed: states, evaluation criteria, and the iterative process to improve solutions.