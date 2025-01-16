> [!CITE] **Definition 15 (zero-sum game):**  
> A normal-form game $(G, \mathcal{A}, \mathcal{T}, \chi)$ is a **zero-sum game** iff for any joint action $a = (a^{[1]}, \ldots, a^{[N]}) \in \mathcal{A}$, it holds that $\sum_{i=1}^{|G|} \chi^{[i]}(a) = 0$.

## ELI5

A **zero-sum game** is the opposite of a common-payoff game. In this type of game, if one player wins, the others lose by exactly the same amount. Imagine a seesaw: if one side goes up, the other must go down by the same amount.

For example, think of a chess game. If you win, your opponent loses, and vice versa. The total "reward" in the game always adds up to zero—whatever you gain, your opponent loses, and whatever they gain, you lose.

This means players are in direct competition, and their interests are completely opposed. There’s no teamwork here!

---

## Components of the Definition

1. **Normal-form Game $(G, \mathcal{A}, \mathcal{T}, \chi)$**:  
    The game framework, as defined in [[Definition 13 (normal-form game)]]:
    - $G$: Set of agents (players).
    - $\mathcal{A}$: Space of joint actions.
    - $\mathcal{T}$: Joint target space.
    - $\chi$: Utility function mapping joint actions to rewards.
2. **Zero-sum Condition ($\sum_{i=1}^{|G|} \chi^{[i]}(a) = 0$)**:  
    For any joint action $a$, the total rewards of all players add up to zero.
3. **Condition ($iff$)**:  
    The zero-sum property is what makes a normal-form game a **zero-sum game**.

---

## Explanation

A **zero-sum game** describes a situation where one player's gain is exactly balanced by the losses of the other players. The rewards (or losses) are distributed such that their total sum is always zero.

This means:

- Players are in complete opposition.
- Winning requires making the other players lose.
- There’s no scenario where all players win or all lose simultaneously.

### Why Is This Useful?

Zero-sum games are useful for modeling competitive scenarios, such as:

- Chess or poker, where players directly compete for a win.
- Market trading, where one trader's profit is another's loss.

---

## Summary

A **zero-sum game** is a normal-form game where the sum of all players' rewards for any joint action always equals zero. It models situations of pure competition, where one player's gain is another's loss.