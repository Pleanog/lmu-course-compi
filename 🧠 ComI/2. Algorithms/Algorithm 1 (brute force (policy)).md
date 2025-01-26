
> [!CITE] Algorithm 1 (brute force (policy))
> Let $\mathcal{A}$ be a set of actions. Let $\mathcal{O}$ be a set of observations. Let $\Gamma \subseteq (\mathcal{O} \to \mathcal{A}) \to \mathbb{B}$ be a space of goal predicates on policy functions. Let $\gamma \in \Gamma$ be a goal predicate. We assume that the policy space $\Pi \subseteq \mathcal{O} \to \mathcal{A}$ is enumerable, i.e., $\Pi = \langle \pi_i \rangle_{i \in \mathbb{N}}$. 
> $$ b(i) =
\begin{cases} 
\pi_i & \text{if } \gamma(\pi_i), \\
b(i+1) & \text{otherwise}.
\end{cases}$$
>If not further specified, the call to $b(0)$ is called brute force search for an agent policy. Usually, an additional termination condition is specified.

## ELI5

The algorithm goes through a list of possible policies (plans) one by one to find one that satisfies a specific goal. Starting with the first policy, it checks if the goal condition (like cleaning a dirty tile or finding a diamond) is met. If it is, the policy is selected; otherwise, the algorithm moves to the next policy in the list and repeats the process. This method ensures that a working policy is eventually found, but it can be slow if the list is very long, as it doesn't use any shortcuts.

---
### Explanation

1. **Overview**:
      - The algorithm describes a brute-force approach to find a **policy** (a function mapping observations to actions) that satisfies a **goal predicate**
2. **Key Components**:
    - **Actions ($\mathcal{A}$)**: The set of all possible actions the agent can take.
    - **Observations ($\mathcal{O}$)**: The set of all possible observations the agent can perceive.
    - **Policies ($\Pi$)**: The space of functions mapping observations to actions. These are enumerable (can be listed one by one as $\pi_i$).
    - **Goal Predicate ($\gamma$)**: A condition that a policy must satisfy to be considered valid.
3. **Function $b(i)$**:
	- The function evaluates policies sequentially, starting at index $i$.
    - If the current policy $\pi_i$ satisfies the goal predicate $\gamma$, it is returned.
    - Otherwise, the function recursively moves to the next policy, $b(i+1)$.
4. **Use of $b(0)$**:
    - Starting at $b(0)$ means testing all policies in $\Pi$ from the first one onwards until a policy satisfying $\gamma$ is found.
    - This is a brute-force method because it exhaustively searches through all possible policies.
5. **Termination Condition**:
    - The text notes that an additional termination condition is often required to avoid infinite loops, especially if no valid policy exists within the enumerable space $\Pi$.

---
### Practical Interpretation

- This algorithm is a **baseline approach** to policy search. While simple, it is computationally expensive because it checks each possible policy one by one.
- The utility of this method lies in ensuring completeness: if a valid policy exists in $\Pi$, it will eventually be found.

