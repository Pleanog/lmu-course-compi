>[!CITE] **Theorem 4 (Nash's Theorem)**
Every game $(G, \mathcal{A}, \mathcal{T}, \chi)$ with $|G|$ and |$\mathcal{A}$| finite has a Nash equilibrium

### **ELI5**
Imagine you're playing a board game with your friends. Everyone is trying to win, and they’re making moves based on what they think you'll do. **Nash's Theorem** says:
> No matter how complicated the game is, there’s always a situation where everyone has made their best move, and no one wants to change what they’re doing — because changing wouldn’t help them win more.
This special situation is called a **Nash Equilibrium**.

---

### **Explanation:**

Nash's Theorem applies to **games** with specific rules and players::
1. **Game**:
    - Think of a "game" as any situation where multiple agents (players) interact, make decisions, and try to maximize their own reward (or utility).
    - Examples: Chess, poker, or even AI agents bidding in an auction.
2. **Players (G)**:
    - The set of all people (or agents) in the game.
    - Example: Two players in a chess game, or multiple AI systems in a multi-agent environment.
3. **Strategies (𝒜)**:
    - A "strategy" is a plan or decision rule for a player. It tells them what to do in every possible situation in the game.
    - A strategy can be:
        - **Pure**: Always choosing one action (e.g., always attacking in a game).
        - **Mixed**: Randomly choosing between multiple actions (e.g., bluffing in poker 30% of the time and playing safe 70%).
4. **Utility/Payoff (𝒯)**:
    - This is what players care about: their reward, score, or outcome. Each player tries to maximize this.
5. **Nash Equilibrium**:
    - This is a situation where **no player has any reason to change their strategy**, given what others are doing.
    - Example: In a rock-paper-scissors game, if both players play randomly (mixing their choices), neither can improve by changing their strategy.

### **What Nash’s Theorem Says**:

For any game where:
- The number of players (**|G|**) is finite.
- The number of possible strategies (**|𝒜|**) is finite.

There **always exists** at least one Nash equilibrium. This equilibrium could involve:
- Pure strategies (e.g., both players play the same way every time).
- Mixed strategies (e.g., players use probabilities to decide what to do).

---

### **Example for AI**:

Two self-driving cars at an intersection:
1. Each car can either go straight, turn left, or wait.
2. Both cars want to avoid crashing while minimizing their delay.

**Nash's Theorem guarantees** there’s a set of strategies where:
- Each car knows what the other is doing.
- Neither car has any incentive to change its decision because doing so would make things worse for itself.

---

### **Clarifications:**

- **Is a strategy a target function?**    
    - Not exactly. A strategy is more like a **decision-making rule** or policy that determines actions based on the game's state.
    - A "target function" could be part of how an AI agent learns its strategy (e.g., in reinforcement learning, the target function updates the policy).
- **Mixed strategies**:
    - In some games, it’s impossible to find a pure-strategy equilibrium. Nash’s genius was proving that **randomization (mixing)** can always create an equilibrium in such cases.
