
# 1
ii
iii
i
iii
ii
iv
ii
ii
i
ii

# 2

## (i)

-(32-42)^2-(32-42)^2
-(-10)^2-(-10)^2
-100-100 = -200

-(-2)^2-(-2)^2
-(-2*-2)-(-2*-2)
-4-4=-8

# 3  Optimization and Search 

## (i)

(x ~ X) * 5

X = variation(x)*5

$$
\begin{align*}
\text{variation}(\emptyset) &= \emptyset \\
\text{variation}(X) &= \{\text{mutate}(x)\} \cup \text{variation}(X \setminus \{x, x'\}) \quad \\
\text{where } X &\neq \emptyset \\
\text{ and } x, x' &\sim X \\
\text{mutate}(x) &= (x'_0, x'_1, x'_2, x'_3, x'_4) \quad \\ \text{where }x'_i &= 
\begin{cases} 
g \sim \{A, C, G, T\} & \text{if } i = j \\
x_i & \text{otherwise}
\end{cases} \\
j &\sim \{0, ..., 4\}
\end{align*}

$$

## (ii)
both functions take a population and remove (aka selection) canidates recusivly from it until there are no more than 10 in the populaition. As stated in the definition the selection can be randomized and non deteministic but it does no need to be. the selection1 is deterministic in its approach, while selection2 is random. So both fulfill the definition.
Selectio1 is exerts more pressure becaue it removes the canidate with the worst fintessfunction first and not randomly

# 4  Reinforcement Learning 

## (i)

Statespace is a concartinated tuple of all possible states of the given world.
Actionspace is a concartinated tuple of all possible actions an agent can take.
Target Space are the possible results of the actions an agent makes accordingly to a given state
The reward function R retuns a reward positiv or nagetativ depending on the actions and the state

## (ii)

s_0 = {A, clean, dirty} - vacuum -> -1 
s_1 = {A, clean, dirty} - switch -> 0
s_2 = {B, clean, dirty} - vacuum -> 10
s_3 = {B, clean, clean} - vacuum -> -1
s_4 = {B, clean, clean}

$V\pi(s_4)$ = 0
$V\pi(s_3)$ = -1
$V\pi(s_2)$ = 9
$V\pi(s_1)$ = 9
$V\pi(s_4)$ = 8


# Question for the Prof:

somewhat(0) = 0 aber 0 ist nicht kleiner als 0 damit ist die lösung doch falsch ...
ich härre hier eine geschweifte klammer genutzt und gesagt x^3 if x>0 else x-0,1


## (iii)

OR = max(y,x)

$$very(good(A_{price})) \lor somewhat(good(A_{location}))$$



$$very(good(B_{price})) \lor somewhat(good(B_{location}))$$
$$very(good(600k)) \lor somewhat(good(0,7))$$

#### For A
good price 400k = 0,8 (taken from the graph)
very(0,8) = 0,8^2 = 0,64

somewhat(0,6) = 0,6/2 = 0,3

0,64 OR 0,3 = max(0.64 , 0.3) = 0,64


#### For B 
good price 600k = 0,6 (taken from the graph)
very(0,6) = 0,6^2 = 0,36

somewhat(0,7) = 0,7/2 = 0,35

0,36 OR 0,35 = max(0.36 , 0.35) = 0,36

A > B

# 7  Game Theory

## (i)

|     | a    | b    |
| --- | ---- | ---- |
| a   | -1,1 | 0,0  |
| b   | 0,0  | 1,-1 |

## (ii)

|     | a    | b    |
| --- | ---- | ---- |
| a   | -1,1 | 0,0  |
| b   | 0,0  | 1,-1 |

## (iv)

|     | a   | b   |
| --- | --- | --- |
| a   | 1,1 | 0,0 |
| b   | 0,0 | 0,0 |


#  8  Reading
