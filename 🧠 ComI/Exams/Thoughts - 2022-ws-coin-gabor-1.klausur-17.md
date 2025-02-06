
# 1 

iii
ii
ii
iii
iv
ii
i
iv
i
i

# 2 Agents and Goals
## (i)
### **Given Variables and Elements**
1. **Agent**:
    - SquirrelBot on a 2D plane that can dig for nuts.
2. **Environment**:
    - A continuous 2D plane **$\mathcal{L}$** with bounds $\mathcal{L} = [0, 100] \times [0, 100] \subset \mathbb{R}^2$.
3. **Observations**:
    - **Current location**: $p \in \mathcal{L}$, the exact location of the SquirrelBot.
    - **Target location**: $g \in \mathcal{L}$, a marked location provided by the **MemoryAgent**, where nuts are buried.
4. **Actions**:
    - **Form**: $a = (\delta x, \delta y, \text{dig})$, where:
        - $\delta x$, $\delta y \in \mathbb{R}$: Movement in the $x$ and $y$ directions.
        - $\text{dig} \in \{ \text{True}, \text{False} \}$: A Boolean flag to decide whether to dig at the current location.
    - **Execution**:
        - Updates the location $p$ by $\delta x$, $\delta y$.
        - If $\text{dig} = \text{True}$, the SquirrelBot attempts to dig at the new location.
    - **Constraint**: Actions that result in movement of more than 1 unit per time step $\sqrt{(\delta x)^2 + (\delta y)^2} > 1$
1. **MemoryAgent**:
    - A separate agent that remembers locations where nuts are buried and provides the target location $g$ to the SquirrelBot.
    - The value of $g$ is observed directly by the SquirrelBot at every time step.

**State**: $s_t$ = Location of the SquirrleBot ($\mathcal{L}$) $\times$ Location of the Traget Location ($\mathcal{L}$) $\times$ Did the Squirrel Try to Dig ($\mathbb{B}$)

**Goal predicate:** $\gamma : \langle \mathcal{L} \times \mathcal{L} \times \mathbb{B} \rangle \to \mathbb{B}$

The **state** at time step $t$ is defined as a tuple: $$s_t = (p_t, g_t, \text{dug}_t)$$
- $p_t$: The SquirrelBot's position at time $t$.
- $g_t$​: The target position at time $t$.
- $\text{dug}_t$​: A flag indicating whether the SquirrelBot attempted to dig after moving.

### My Solution


$$\exists t : t \in T : T \in \mathbb{N} : \{p_{yt},p_{xt},TRUE_t\} \land dist(p_t,g_t) < 1$$

the definition what $t$ is are not needed as it is defined in the question and also the whole state of the squirrel is not needed just $dug_t$ would be enough, but i would assume this is also valid.

but else it is the same as the official solution.
$$\gamma : \langle \mathcal{L} \times \mathcal{L} \times \mathbb{B} \rangle \iff \exists t : \text{dist}(p_t,g_t) < 1 \land \text{dug}_t = \text{TRUE}   
$$

## (ii)

**The type signature of $\pi$: **
$$
\pi(p_t, g_t,\text{dug}) \in \mathcal{L} \times \mathcal{L} \times \mathbb{B} \to a \in \mathbb{R} \times \mathbb{R} \times \mathbb{B} 
$$

**My policy $\pi$:**
$$\pi(p_t, g_t) =
\begin{cases} 
(0, 0, \text{TRUE}) & \text{if } \text{dist}(p, g) < 1, \\ 
\left(
\frac{g_x - p_x}{\text{max}(|g_x - p_x|, 1)},
\frac{g_y - p_y}{\text{max}(|g_y - p_y|, 1)},
\text{FALSE}
\right) & \text{otherwise.}
\end{cases}
$$
The robot digs (`TRUE`) when it is within a distance of 1 from the target, meeting the goal predicate. Otherwise, it moves one step closer to the target along each coordinate, scaling the movement by the larger of the distance in that direction or 1. This ensures the step size stays within the allowed maximum of 1. The `max` function prevents excessively small steps or division by very small numbers, keeping the movement valid.

---
The **official solution** is honestly a bit weird. It’s neither particularly clear to devise from the given problem statement. However, it is straightforward and functional, achieving the same result as my solution. The main difference is that the official solution explicitly handles each possible movement direction with separate lines in the policy, making it more verbose.

$$\pi((x_p, y_p), (x_g, y_g)) =
\begin{cases}
(+0.1, 0, \text{False}) & \text{if } x_g - x_p > 0.1, \\
(-0.1, 0, \text{False}) & \text{else if } x_g - x_p < -0.1, \\
(0, +0.1, \text{False}) & \text{else if } y_g - y_p > 0.1, \\
(0, -0.1, \text{False}) & \text{else if } y_g - y_p < -0.1, \\
(0, 0, \text{True}) & \text{otherwise}.
\end{cases}$$
---
## 3  Optimization and Fuzzy Logic

- **Locations** are: $\mathcal{L} = [0;100] \times [0;100]$
- **Good locations** are:  $g \in \mathcal{L} \text{ with } \mathcal{L} = [0;100] \times [0;100] \subset \mathbb{R}^2$ 
- **Nutritional Score** can be 5 to 0: $\phi:\mathcal{L} \to \mathcal{N} \text{ where } \mathcal{N} = \{5, 4, 3, 2, 1, 0\}$
	- $\phi(g)$ is the nutrition score of the items found by digging at location $g$

## (i)

$$neighbors(x)= x \in [0;100] \times [0;100] \land dist(x,x') < 1$$

## (iii)

Because the optimum goal is so small and the simulated annealing - even when taking small steps - would just wander round the optimum, thats basically just randomly, because it would also take in wors steps to try to see if it is stuck in a local optima and not a global one.

## (iv)

hungry(x) = 1 - (nutritional value / 10)

calmnes = (close to Mr. Rodger / 1000)

happy(x) = calm(x) OR NOT(quite(hungry(x)))

OR = max()
NOT = 1- x

x = (42,42)

calm(x) = (1000 - dist((42,42) , (45,46))) / 1000
= (1000 - sqrt( (42 - 42)^2 + (45 - 46)^2 )) / 1000
= 1000 - sqrt( 0^2 + (-1)^2 )
= 1000 - sqrt(1)
= 1000 - 1
calm(x) = 999 / 1000 = 0,999

dist((42,42) , (42,42)) = sqrt( (42 - 42)^2 + (42 - 42)^2 ) = sqrt( 0^2 + 0^2 )= sqrt(0) = 0
nach der formel $\phi(0)$ = 5
hungry(x) = 1 - ( 5 / 10 )
= 1 - 1/2
= 0,5

quite(0,5) = min(2 * 0,5, 1) = min(1 , 1) = 1

not(1) = 1 - 1 = 0

999 OR 0,75 = max(0.999 , 0) = 0,999


# 5

## (ii)

