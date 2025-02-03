
 >[!CITE] Algorithm 3 (Simulated Annealing)
 Let $\mathcal{D} = (\mathcal{X}, \mathcal{T}, \tau, e, \langle x_u \rangle_{0 \leq u \leq t})$ be an optimization process. Let $\text{neighbors} : \mathcal{X} \to \wp(\mathcal{X})$ be a function that returns a set of neighbors of a given state $x \in \mathcal{X}$. Let $\kappa : \mathbb{N} \to \mathbb{R}$ be a temperature schedule, i.e., a function that returns a temperature value for each time step. Let $A : \mathcal{T} \times \mathcal{T} \times \mathbb{R} \to \mathbb{P}$ with $\mathbb{P} = [0; 1]$ be a function that returns an acceptance probability given two target values and a temperature. Commonly, we use
>
> $$A(Q, Q', K) = e^{\frac{\neg(Q' - Q)}{K}}$$
>
>for ....
>
>
> $$e(\langle x_u \rangle_{0 \leq u \leq t}, \tau) = x_{t+1} =
\begin{cases} 
x'_t, & \text{if } \tau(x'_t) \leq \tau(x_t) \text{ or } r \leq A(\tau(x_t), \tau(x'_t), \kappa(t)), \\
x_t, & \text{otherwise},
\end{cases}$$
>
> where ...
## ELI5

Simulated annealing is like trying to climb down a mountain to find the lowest valley, but sometimes you deliberately climb a little uphill to avoid getting stuck in a smaller valley. The "neighbors" are like nearby paths you can take, and the "temperature" controls how willing you are to climb uphill: at high temperatures, you're more willing to explore worse paths, but as the temperature decreases, you become more selective.

The graph shows this process: we can see the algorithm exploring both good (downhill) and bad (uphill) paths, but gradually focusing on better areas as time progresses.

---
### Components of the Definition

1. Optimization Process ($\mathcal{D}$):**
    Defined as in previous definitions, describing the overall optimization framework.
2. Neighbors Function ($\text{neighbors}$):**
    A function that provides a set of states near the current state $x_t$, representing possible next steps.
3. Temperature Schedule ($\kappa$):**
    A function that decreases over time (cooling schedule), controlling the likelihood of accepting worse solutions.
4. Acceptance Probability Function ($A$):**
    Determines the probability of accepting a worse solution, based on the difference in target values ($Q'$ and $Q$) and the current temperature $K$.
5. State Update Rule ($e$):**
    Chooses the next state $x_{t+1}$:
	 🠚 If the new state $x'_t$ is better than or equal to the current state ($\tau(x'_t) \leq \tau(x_t)$), it is accepted.
	 🠚 If the new state is worse, it may still be accepted with probability $A$.

---
### The Graph
The graph illustrates the optimization process over time, showing how the target function ($\tau(x)$) behaves as different states are evaluated.
![[Pasted image 20241210120848.png]]
- The x-axis represents the states ($x$) being evaluated.
- The y-axis represents the target function value $\tau(x)$, which determines the quality of each state.
- The curve shows how the algorithm explores states: valleys represent better (lower) target values, and peaks represent worse ones.
- The red dots indicate states that were explored, and the movement between dots shows how the algorithm transitions based on the acceptance criteria. Occasionally, the algorithm moves "uphill" to explore worse solutions (peaks) to avoid getting stuck in local minima.

**Importance of the Slope**
The negative slope (downhill) indicates improvement in the target function (moving toward better states). The algorithm should prioritize these transitions when possible.
The positive slope (uphill) indicates worse states, which might be accepted based on the acceptance probability. This uphill movement is critical to escape local minima and achieve better global solutions.

---
### Summary
Simulated annealing is an optimization algorithm that balances exploration (accepting worse solutions) and exploitation (focusing on better solutions). It uses a decreasing temperature to control the probability of accepting worse solutions, ensuring a good balance between exploring and refining. The graph demonstrates this behavior, with the algorithm navigating between better and worse states to avoid getting stuck in suboptimal solutions.