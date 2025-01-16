
> [!CITE] Algorithm 2 (random search(policy))
> Let $\mathcal{A}$ be a set of actions. Let $\mathcal{O}$ be a set of observations. Let $\Gamma \subseteq (\mathcal{O} \rightarrow \mathcal{A}) \rightarrow \mathbb{B}$ be a space of goal predicates on policy functions. Let $\gamma \in \Gamma$ be a goal predicate. We assume that the policy space $\Pi \subseteq \mathcal{O} \rightarrow \mathcal{A}$ can be sampled from, i.e., $\pi \sim \Pi$ returns a random element from $\Pi$. Random search for $n$ samples is given via the function
> $$ \rho(n) =
\begin{cases} 
\emptyset & \text{if } n = 0, \\
\pi & \text{if } n > 0 \text{ and } \gamma(\pi) \text{ where } \pi \sim \Pi, \\
\rho(n-1) & \text{otherwise.}
\end{cases}$$

## ELI5

This algorithm randomly tries different plans (policies) to see if one works. If it finds a plan that satisfies the goal, it stops and returns it. If not, it keeps trying until it runs out of allowed attempts $n=0n$ . It's like throwing darts at a board and hoping one hits the target, instead of checking every spot systematically.

---

### Explanation:

This algorithm explores policies randomly and works as follows:

1. If $n = 0$, the algorithm stops and returns $\emptyset$, meaning no valid policy was found.
2. If $n > 0$, it samples a random policy $\pi$ from the policy space $\Pi$.
	🠚 If $\pi$ satisfies the goal predicate $\gamma(\pi)$, it returns $\pi$ as the solution.
	🠚 Otherwise, it reduces $n$ by 1 and recursively calls $\rho(n-1)$ to try again.

This approach does not systematically check all policies, but rather samples them randomly, which can potentially find a valid policy faster. However, it may miss some policies due to the random nature of sampling unless the number of samples $n$ is large enough.

---
### Practical Interpretation:

In a real-world scenario, like programming a robot to navigate a grid, this algorithm would randomly generate strategies (policies) for the robot, test if they lead to success (e.g., finding a diamond), and stop once it finds one that works. If it fails after $n$ tries, it gives up. This is useful when systematically testing all options is too slow or impractical, but it assumes that sampling randomly has a reasonable chance of hitting a valid solution.