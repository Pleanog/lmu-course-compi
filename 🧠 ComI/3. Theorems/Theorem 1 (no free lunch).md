
>[!CITE] Theorem 1 (no free lunch [1, 2]). As measured by sample efficiency, i.e., the achieved minimal value of $\tau$ per evaluations of $\tau(x)$ for some new $x \in \mathcal{X}$ for finite $\mathcal{X}$, **all optimization algorithms perform the same when averaged over all possible target functions $\tau$**.

So, for any search/optimization algorithm, any elevated performance over one class of problems is exactly paid for in performance over another class.

---

### Explanation (With LaTeX-Style Math Symbols)

#### Theorem Statement

The **No Free Lunch Theorem** states that:
> "If we consider all possible target functions $\tau$, then all optimization algorithms perform equally well on average when measured by sample efficiency."

#### Elements in the Theorem

- **$\tau$**: The target function, representing the "problem" we want to optimize. For example, $\tau(x)$ could represent the cost, error, or fitness value for a given input $x$.
- **$\mathcal{X}$**: The input space, representing all possible inputs $x$ we can evaluate the function $\tau(x)$ on.
- **$x \in \mathcal{X}$**: A specific input or solution from the input space $\mathcal{X}$.
- **Sample Efficiency**: The ability of an algorithm to achieve a minimal value of $\tau$ with as few evaluations of $\tau(x)$ as possible. This is used to measure the performance of an optimization algorithm.

#### Key Claim

When averaging performance over **all possible target functions $\tau$**, no optimization algorithm performs better than any other. For every problem $\tau$ where an algorithm does well, there is another problem where it does poorly.

#### Implication

For any search or optimization algorithm:

- Elevated performance on a specific class of problems (e.g., linear problems) is "paid for" by worse performance on other problem classes (e.g., non-linear problems).

This means there is **no universal optimization algorithm** that performs better for all possible problems.

---

#### Summary of the Idea

The theorem emphasizes that optimization algorithms are problem-specific tools. Instead of seeking a universal algorithm, practitioners must match the algorithm to the specific characteristics of the problem at hand.