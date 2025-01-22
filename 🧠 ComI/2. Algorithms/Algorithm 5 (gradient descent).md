

>[!CITE] **Algorithm 5 (gradient descent)**
>Let $\mathcal{D} = (\mathcal{X}, \mathcal{T}, \tau, e, \langle x_u \rangle_{0 \leq u \leq t})$ be an optimization process. Let $\mathcal{T}$ be continuous ($\mathcal{T} = \mathbb{R}$, e.g.) and let $\tau': \mathcal{X} \to \mathcal{T}$ be the first derivative of $\tau$. The process $\mathcal{D}$ continues via gradient descent (with update rate $\alpha \in \mathbb{R}^+$) if $e$ is of the form
>
$$e(\langle x_u \rangle_{0 \leq u \leq t}, \tau) = x_{t+1} = x_t - \alpha \cdot \tau'(x_t).$$
>
The learning rate $\alpha$ can also be given as a function, usually $\alpha: \mathbb{N} \to \mathbb{R}$, so that $e(\langle x_u \rangle_{0 \leq u \leq t}, \tau) = x_{t+1} = x_t - \alpha(t) \cdot \tau'(x_t).$
>
If $\tau$ is stochastic, this process is called stochastic gradient descent (SGD).
