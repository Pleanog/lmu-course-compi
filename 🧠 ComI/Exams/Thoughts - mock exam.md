# 1  General Knowledge / Blanks

evolutionary
population
individual
fitness
selection (elimination)
recombination
parent
mutation
exploration
exploitation

# 2  Agents and Goals

## (i)
$c_t$ = Position of the Crow

$\mathcal{O} = \mathbb{R}^2 \times \mathbb{R}^2 \times \mathbb{R}^2 \times \mathbb{B}   = \{c_t, p_t, l_t, claws\}$
position of the crow, nut and truck and if the crows "claws's state" 

$\mathcal{S} = \mathcal{O}$

## (ii)
same solution as the prof. basically just with t => t'

$$
\iff \forall t \to t' : q_t = 1 \land p_t = (x,y,0) | x,y \in \mathbb{N} \land \text{dist}(p_{t'}, l_{t'}) < 1
$$
ist so auch mehr oder weniger ok, wobei das mit dem $\forall$ macht, wobei das evtl. etwas unklar ist, ob die Vorraussetzung dann in jedem zeitschritt vorkommen sollte
## (iii)

The CrowBot should learn two main behaviors based on the reward function:
1.	Avoiding the truck: The CrowBot must always maintain a distance of at least 1 from the truck’s position, as coming too close likely results in the CrowBot being “killed.” This caution might extend to avoiding the leftmost coordinates, anticipating the truck’s random reappearance after it loops back to the left or just to stay above $z > 1$ but these two ideas might not necesarrily be learned.
2.	Picking up and cracking the nut: The CrowBot should learn to pick up the nut and fly above the truck’s last position. From there, it moves further to the right, timing its action to drop the nut in front of the moving truck, cracking it successfully. But this would result in the end of the game, so it would most likely (if the reward is not super high) not drop the nut and just awoid the end of the game and gain small rewards indefinitly. So there is a direct conflict (see: iv).

## (iv)

Yes, there is a conflict between the goal predicate and the reward function. The goal predicate requires the CrowBot to drop the nut in front of the truck so it can crack it open, completing the task. However, the reward function does not incentivize this behavior properly because cracking the nut ends the game. If the reward function focuses solely on avoiding the truck and staying alive, the CrowBot may prioritize prolonging the game rather than achieving the goal, creating a misalignment between the goal and the rewards.


# 3  Fuzzy Logic

# 4  Optimization

## (iii)

### **Questions to Ask the Professor**

1. **Indexing in the Official Solution**:
    - The official definition states $i \in [0,1000)$, meaning the range is from **0 to 999** (not 1000).
    - **Why does the definition use $[0,1000]$ instead of $[0,999]$?**
3. **Is There a Specific Reason for Excluding the Same Action?**
    - Our new function ensures that the new action differs from the previous one.
    - **Is this necessary for evolutionary convergence, or could keeping the same action in some cases be beneficial?**


## (iv)
helper funciton die dritte zeile mit helper(X.n) sollte so aussehen:
$$
\text{helper}(X \backslash \{\text{best}(X)\},n)$$














# 5  Game Therory

![[Pasted image 20250131213006.png]]

warum sind die blauen nicht relevant?
# 6  Scientific Reading: Empowerment

## (i)
Empowerment can help maximize long term reward for RL algorithms by giving the agent information over the changes its actions have in the enviroment. This can lead to broader exploration and a more robust learning of startegies and solutions. Having feedback over the actions and resulting changes on the enviroment more complex problems can be solved and even chaning in the enviroments are handled more effectivly. The mutual informationis a key aspects of empowerment is about maximizing control over future states (and the envoriment) based on previous actions.
**! Example is meant to be like this: example of how it can be used to encourage more efficient exploration.**
An example would be an agnet that needs to harcest crop. if it can get feedback on the actions it takes ic can be more resourcefull and not just harvest all the crop but let some stand for it to spread and grow more crop later.

## (ii)
Depending on the problem statement empowerment might lead to more exploration that is not cost effective. As a signal it could also be hard to be sure that the given signals are guiding the agent in the desired direction as it is not directly definied in the policy as the signals are not directly tied to external rewards, which can sometimes lead to suboptimal behavior. In complex enviroments the behaviour can than be less predicatable and in very simple enviroments the empowerment might lead to more randomnes.
There is also the the computational cost of estimating mutual information.

## Questions:

- What will not be in the exam?
	- ($\pi$-process)
