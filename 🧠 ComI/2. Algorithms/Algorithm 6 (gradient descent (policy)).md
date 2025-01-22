
> [!CITE] **Algorithm 6 (gradient descent (policy))**
Let $\pi_\theta$ be a policy $\pi$ that depends on a vector of continuous parameters $\theta \in \Theta$ such that usually $\Theta = \mathbb{R}^N$ for some $N$. Let $\tau: \Theta \to \mathcal{T}$ be a target function on the parameters $\theta$ of a policy $\pi_\theta$. Let $\mathcal{T}$ be continuous ($\mathcal{T} = \mathbb{R}$, e.g.) and let $\tau': \Theta \to \mathcal{T}$ be the first derivative of $\tau$, i.e., $\tau'(\theta) = \frac{\partial \tau(\theta)}{\partial \theta}.$
If $\mathcal{D} = (\Theta, \mathcal{T}, \tau, e, \langle x_u \rangle_{0 \leq u \leq t})$ is an optimization process that continues via gradient descent, $\mathcal{D}$ is a process of **policy optimization** via gradient descent.
