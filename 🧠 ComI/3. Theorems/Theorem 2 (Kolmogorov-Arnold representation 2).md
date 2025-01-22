
>[!CITE] **Theorem 2 (Kolmogorov-Arnold representation [2])**.
Any continuous function $f : \mathbb{R}^n \to \mathbb{R}$ for some $n \in \mathbb{N}$ can be written as a finite composition of continuous functions of a single variable ( $f_i : \mathbb{R} \to \mathbb{R}$ for $i \in \mathbb{R}, 1 \leq i \leq n$ for some $n \in \mathbb{N}$ ) and addition ($_-+_- : \mathbb{R} \times \mathbb{R} \to \mathbb{R}$).

$\Rightarrow$ neural networks are **universal function approximators**

### **ELI5**

Imagine we have a super-complicated machine (the function $f$) that takes in multiple dials (inputs $x_1, x_2, \dots, x_n$​) and gives you one final result (the output). It feels like magic, and we’re not sure how it works.

The **Kolmogorov-Arnold theorem** says:
> “Don’t worry! This complicated machine can actually be built using smaller, simpler machines. Each of these smaller machines only looks at _one dial at a time_ and gives a simple output. Then, you can combine all these outputs (by adding them up or something similar) to get the final result.”

So instead of trying to figure out how the big machine works all at once, you can break it down into:
1. Small, easy-to-understand machines (functions of one dial at a time).
2. A simple way to combine their results (like addition).

It’s like saying: _No matter how fancy a cake is, it’s really just sugar, flour, eggs, and butter, mixed together in the right way._

---
### **Key Components**

1. **The Input Function**:
    - We start with a function $f : \mathbb{R}^n \to \mathbb{R}$.
    - This means $f$ is a function that takes nnn-dimensional inputs (vectors of $n$ real numbers) and outputs a single real number.
2. **Continuity**:
    - The theorem applies only to **continuous** functions, which means there are no sudden jumps or breaks in the function's graph.
3. **Representation**:
    - The theorem states that such a function $f$ can be rewritten as a **finite combination** of simpler functions. These simpler functions are:
        - **Functions of a single variable**, $f_i : \mathbb{R} \to \mathbb{R}$, which map one real number to another.
        - **Addition operations**, where we combine the results of these single-variable functions.
4. **Addition Function**:
    - The addition is represented as $_-+_- : \mathbb{R} \times \mathbb{R} \to \mathbb{R}$, which is just a formal way of saying we sum the outputs of the one-variable functions.

---
### **Explanation**

The **Kolmogorov-Arnold Representation Theorem** is a result from mathematical analysis that describes how we can represent a complex multivariable function using simpler functions of just one variable.

### **What Does This Mean?**

The theorem tells us that any continuous multivariable function $f(x_1, x_2, \dots, x_n)$ can be **decomposed** into:
1. A set of one-variable continuous functions $f_i(x)$.
2. A combination process (like summing or composing these simpler functions).

This decomposition simplifies the analysis or computation of $f$, as it reduces a complicated, multidimensional problem to multiple easier, one-dimensional problems.

---

### **Why is This Important?**

1. **Neural Networks**:
    - This theorem underpins the idea that neural networks can approximate any continuous function. By combining simple operations (like weighted sums and activation functions), neural networks are capable of representing highly complex relationships.
2. **Function Approximation**:
    - It shows that even complex systems can be broken into simpler parts, which is a foundational concept in many fields of mathematics, physics, and computer science.

---

### **Summary**

Any continuous function that takes multiple inputs can be built from a finite number of functions that each take only one input, combined using addition.


---
---

## **Backpropagation** 

Backpropagation is the process neural networks use to learn. It calculates how much each weight in the network contributes to the error (difference between the predicted and actual values). Then, it adjusts these weights step by step, working backward from the output layer to the input layer, using a mathematical rule called the **chain rule**.

![[Pasted image 20250122203651.png]]

1. **Learning by Gradients:** Backpropagation uses gradients (slopes) to figure out how to change the weights to reduce the error.
2. **Iterative Improvement:** By repeating this process over many iterations (called epochs), the network gets better at making accurate predictions.
3. **Efficiency in Training:** Neural networks are relatively efficient to train because backpropagation distributes the computational work layer by layer, avoiding the need for manual adjustment of weights. Modern optimizations like GPU acceleration and advanced algorithms (e.g., Adam optimizer) make this process even faster.

