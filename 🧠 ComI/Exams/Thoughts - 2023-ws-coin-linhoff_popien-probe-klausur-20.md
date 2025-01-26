## 2 Agents and Goals

S = ``working, alarming, defect``

The state of the power node at position (x, y) can be checked by calling a function ``state_of ``: $C^2 \to \mathcal{M}$ where $\mathcal{C} = [0; 9] \subset \mathbb{N}$ is the space of grid positions and $\mathcal{M}$ = ``{working, alarming, defect}`` is the space of power node states, i.e., states that a single power node can be in.


| w     | w   | w   | w   | ==a Bot== | w   | w   | w   | w   | w   |     |
| ----- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
| ==d== | w   | w   | w   | w         | w   | w   | w   | w   | w   |     |
| w     | w   | w   | w   | w         | w   | w   | w   | w   | w   |     |
| w     | w   | w   | w   | w         | w   | w   | w   | w   | w   |     |
| w     | w   | w   | w   | w         | w   | w   | w   | w   | w   |     |
| w     | w   | w   | w   | w         | w   | w   | w   | w   | w   |     |
| w     | w   | w   | w   | w         | w   | w   | w   | w   | w   |     |
| w     | w   | w   | w   | w         | w   | w   | w   | w   | w   |     |
| w     | w   | w   | w   | w         | w   | w   | w   | w   | w   |     |
| w     | w   | w   | w   | w         | w   | w   | w   | w   | w   |     |
| w     | w   | w   | w   | w         | w   | w   | w   | w   | w   |     |

### i) As stated above, the RepairBot can observe (x†, y†), which is the nearest alarming power node. Why is this coordinate data not needed as a separate part of the system state definition?

The coordinate data $(x^\dagger, y^\dagger)$ of the nearest alarming power node is not needed as a **separate part of the system state definition** because it can be derived directly from the information already provided in the system state. Let's break this down:

### System State Definition:

The system state is defined as: $$\mathcal{S} = (\mathcal{C}^2 \to \mathcal{M}) \times \mathcal{C}^2$$
where:
- $\mathcal{C}^2 \to \mathcal{M}$: A mapping of all grid positions to their states $\mathcal{M}$ = ``{working, alarming, defect}``.
- $\mathcal{C}^2$: The position of the RepairBot $(x,y)$.
### Why $x^\dagger, y^\dagger$ is redundant:
- The full state of the grid $\mathcal{C}^2 \to \mathcal{M}$ provides the status of every power node, including which nodes are in the **alarming** state.
- Since the RepairBot's current position $(x, y)$ is part of the system state, the **nearest alarming node** can be determined by calculating the  distance (e.g. Euclidean) between the current position of the RepairBot $(x, y)$ and all nodes with state $\mathcal{M}$ = ``alarming``.

## ii) Give a goal predicate γ : ⟨S⟩ → B so that γ(⟨state oft, (xt, yt)⟩0≤t≤T ) holds iff no power node has ever been defect and any alarming power node is working again (at least once) within at most 5 time steps.

The goal predicate $(\gamma : \langle S \rangle \to \mathbb{B})$ holds if and only if the following conditions are satisfied:

$$
\gamma(\langle s_t \rangle_{0 \leq t \leq T}) \iff \begin{cases} \forall t : (x, y) : \text{state}(x, y, t) = \text{alarming}, \exists t' \in [t+1, t+5], \text{state}(x, y, t') = \text{working} \\ \forall t: (x, y) : \text{state}(x, y, t) = \text{defect}, \gamma(\langle s_t \rangle) = \text{False} \end{cases}
$$

Where:
- $\text{state}(x, y, t)$ refers to the state of the power node at coordinates $(x, y)$ at time  $t$.
- The first condition ensures that any alarming power node becomes working within $5$ timesteps.
- The second condition ensures no power node ever becomes defect.

Solution from the Prof:

$$\gamma\left(\left(\text{state\_of}_t, (x_t, y_t)\right){0 \leq t \leq T}\right) \iff \forall t: \forall X, Y: \text{state\_of}_t((X, Y)) \neq defect \\ \wedge \text{state\_of}_t((X, Y)) = alarming \implies \exists t': t' - t \leq 5 \wedge \text{state\_of}_{t'}((X, Y)) = working$$

## (iii)

the agent gets more reward if the cell is defect, so wating for a cell to go defect is a better strategy than repairing it right away while the cell is in the alarming state.
Since there is no real harm in defect for the agent he could wait collect a cuploe rounds of 0 points but then many 10 points instead of 5points every then and now

---
One Option is to add a penality for a cell that goes from alarming to defect, but this is maybe to complex as directly penalizing the defect cell every state is more robust. As for every following state where the cell is not repaired and still defect the penalty would not be given in this example.
$$R = 
\begin{cases} 
-5 & \text{if state\_of}_t((x_t, y_t)) = \text{alarming} \text{ and state\_of}_{t+1}((x_t, y_t)) = \text{defect}, \\
\end{cases}
$$
---

Another option would be to add a delta, this is my preffered option but i am not sure about how to propperly track the delta in this connotation. I just added it. 
By tying the reward to the speed of repair, the bot is encouraged to address `alarming` cells quickly before they transition to `defect`. 
The bot is rewarded for maintaining good performance without explicitly punishing bad behavior.

$$R = 
\begin{cases} 
+10 - \Delta t & \text{if action is repair and state\_of}_t((x_t, y_t)) = \text{defect}, \\
+5 - \Delta t & \text{if action is repair and state\_of}_t((x_t, y_t)) = \text{alarming}, \\
-5 & \text{if state\_of}_{t+1}((x_t, y_t)) = \text{defect}, \\
0 & \text{otherwise.}
\end{cases}
$$---
Here i try to incentivizes quick repairs by penalizing unresolved `alarming` states (-2) and discourages letting cells become `defect` with a stronger penalty (−3), while also rewarding maintenance with a +3 if all cells are `working`. The +1 reward for maintenance may not be strong enough to compete with the repair rewards (+10, +5), so the bot might prioritize repair over "prevention".

$$
R =
\begin{cases}
+10 & \text{if action is repair and state\_of}_t((x_t, y_t)) = \text{defect}, \\
+5 & \text{if action is repair and state\_of}_t((x_t, y_t)) = \text{alarming}, \\
-2 & \text{if state\_of}_t((x_t, y_t)) = \text{alarming and } \text{state\_of}_{t+1}((x_{t+1}, y_{t+1})) \neq \text{working and } a_{t+1} \neq \text{repair}, \\
-3 & \text{if state\_of}_t((x_t, y_t)) = \text{defect (every defect cell at the current state is penalized heavy)}, \\
+3 & \text{if state\_of}_t(X,Y) = \text{working (all cells are working)}, \\
0 & \text{otherwise}.
\end{cases}
$$

### Official Solution

−3 if ∃X,Y:state_oft​((X,Y))∈{defect, alarming}.

#### **Questions:**
- How does this solution account for the 5-step limit before a cell in an `alarming` state must be repaired? Should the reward function consider the timing for quicker repairs?
- The solution penalizes `defect` and `alarming` states, but how does it ensure the agent prioritizes "prevention" of `defect` cells rather than waiting to earn higher rewards for repairs?
- Why choose a penalty over adding time-sensitive rewards, such as rewarding faster repairs or penalizing delays explicitly?