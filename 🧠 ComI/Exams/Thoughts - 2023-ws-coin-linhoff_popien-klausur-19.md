| Cow |       | Cow    |       |     |     | Cow |     |     |     |
| --- | ----- | ------ | ----- | --- | --- | --- | --- | --- | --- |
|     | ----- | -----  | ----- | Cow |     |     | Cow |     |     |
|     | ----- | MowBot | ----- |     |     |     |     |     | Cow |
| Cow | ----- | -----  | ----- |     | Cow |     |     |     |     |
|     |       | Cow    |       |     |     |     |     |     |     |
|     | Cow   |        |       |     | Cow |     | Cow |     |     |
|     |       |        | Cow   |     |     |     |     | Cow |     |
|     |       | Cow    |       |     |     |     |     |     |     |
|     |       |        |       | Cow |     |     | Cow |     |     |
|     |       |        |       |     |     |     |     |     | Cow |
| Cow |       |        |       |     | Cow |     |     |     |     |

20 Cows = $G^{[1]}, \dots ,G^{[20]}$ 
1 MowBot = $G^{[0]}$ 

positions are defined as $l \in \mathbb{R}^2$ 

all States are: $\langle s_t\rangle_t \text{t of unspecified length for states} s_t \in \mathcal{S}$ at time $t$  where $\mathcal{S} = \mathbb{N} \times (\mathbb{R}^2)^{21}$ is the 43 dimemsional state-space

## (i)

Write a goal predicate $\gamma_1: \langle S \rangle \times \langle A \rangle \to \mathbb{B}$ such that $\gamma_1$​ holds if and only if the MowBot has never, at any full time step $t$, been closer than a distance of $1$ to any of the cows:

$$\gamma_1 \left( \langle (t, l^{[0]}_t, ..., l^{[20]}_t) \rangle_t, \langle (a^{[0]}_t, ..., a^{[20]}_t) \rangle_t \right) \iff \forall t \in \mathbb{N} : \forall i \in \{1, ..., 20\} \subset \mathbb{N} : dist(l^{[0]}_t,l^{[i]}_t) \geq 1$$ 
## (ii)

$$\mathcal{R}(s_t,a_t,s_{t+1})
\iff
\begin{cases}
+3 & a^{[0]}_t = \text{mow/eat} \\
-10 & dist(l^{[0]}_t,l^{[i]}_t) \geq 1  \text{ for any i} \\
0 & \text{else}
\end{cases}$$
## (iii)
(as long as the cows new policy does not corner the robot, and even then) the reward function of the robot should still be able to be learned because the actionspace of the cows is  still the same, so the robot can still avoid the cows and keep mowing the grass regardless of what the cows are doing. Even after the policy change in the cows the robot should still be able to learn as the new policy is still predictable.

ChatGPT made it 
The reward function $\mathcal{R}$ should still be learnable by the MowBot because the cows’ new policy, while different, is still fixed and predictable after the change. The MowBot's ability to learn does not depend on the specific details of the cows’ policy, but rather on the consistency of the environment's rules and the MowBot's ability to avoid collisions while maximizing rewards.

Even though the transition probabilities change at t=26t = 26t=26, they stabilize again once the cows adopt their new fixed policy. Since the action space of the cows remains unchanged, the MowBot can still observe and predict the new behavior over time. As long as the cows’ policy does not make it impossible for the MowBot to avoid them (e.g., by "cornering" it), the MowBot can continue to learn an optimal policy that fulfills its goals.

Thus, while the environment undergoes a one-time shift at t=26, the system remains an MDP post-change, with consistent P in each segment. This allows $\mathcal{R}$ to remain learnable.

## (iv)

Let γ2 : 〈S〉 × 〈A〉 → B be goal predicate so that γ2 holds iff the MowBot has never executed the action eat/mow within a radius of 1 from any point where any cow has ever executed mow/eat. Assume that the cows’ policies are fixed. Can the MowBot learn to fulfill γ2 effectively for an MDP with the given state space S for some reward function R′? Briefly state your reasoning.

