
> [!CITE] Definition 11 (Training a neural network)
> Let $\mathcal{N} : \mathbb{R}^p \to \mathbb{R}^q$ be a neural network with $n$ weights $\overline{\mathcal{N}} = w ⧺ b \in \mathbb{R}^n$ as in [[Definition 8 (neural network)]]. Note that thus $|\overline{\mathcal{N}}|=n$. Let $\tau:\mathbb{R}^n\to\mathbb{R}$ be a target function as in [[Definition 2 (optimisation)]]. Note that thus $\mathcal{T}=\mathbb{R}$. The process of optimizing the network weights $|\overline{\mathcal{N}}|$ so that $\tau(\overline{\mathcal{N}})$ becmes minimal is called training.
> - Let $\mathbb{T}=\{(x_i,y_i):i=1,\dots,N\}$ be a set of $N$ points of training data, where $x_i \in\mathbb{R}^p$ and $y_i,\in\mathbb{R}^q$ for all $i$. If $\tau$ is of the form $$\tau(\overline{\mathcal{N}}) = \sum_{i=1}^N \left( \mathcal{N}(\mathbf{x}_i) - \mathbf{y}_i \right)^2$$
>   or a simmilar form, the process of training $\mathcal{N}$ is called supervised learning

### ELI5

This explains how a neural network learns by **adjusting its weights** so that it can make good predictions for a bunch of training examples.

This formula calculates the total squared error for a model $\mathcal{N}$ over a set of $\mathbb{N}$ samples. It compares the model's predictions to the true values and sums the squared differences for all the samples.

- If the model's prediction is very close to the true value for each sample, the error will be small, and so the loss function will have a low value.
- If the model’s predictions are far from the true values, the error will be large, and the loss function value will be higher.

The goal during training is typically to **minimize** this loss function (i.e., minimize the total squared error) to improve the model's accuracy.

### Components of the Definition

- **The Neural Network $\mathcal{N}$**:
    - This is the model being used. It takes in some numbers (inputs, $\mathbf{x}_i$​) and returns some numbers (outputs, $\mathbf{y}_i$).
    - Inside, it has "weights" ($\mathbf{w}$) and optional "biases" ($\mathbf{b}$) that determine what it does.
-  **The correct answer $\mathbf{y}_i$**
	- $\mathbf{y}_i$​ is the **true label** or **actual value** associated with the i-th sample. This is the ground truth we want the model to predict correctly.
- **Training Data $\mathcal{T}$**:
    - A collection of examples where input and output are allready currectly defined:
        - The inputs ($\mathbf{x}_i$​)
        - The **correct** answers ($\mathbf{y}_i$​).
- **Error $\tau(\overline{\mathcal{N}})$**:
    - After the neural network $\mathcal{N}$ makes a guess for each input, we compare its guesses $(\mathcal{N}(\mathbf{x}_i))$ to the correct answers ($\mathbf{y}_i$).
    - The **error** is how far off it is.
      The formula says: $τ(N)$=$Sum$of all the squared differences between guesses and correct answers.
- **Going over the Datapoints - $SUM \sum_{i=1}^N$**:
    - We are just going over all the given datapoints
    - $\mathbb{N}$ is just the number of datapoints

### The Goal (Learning/Training):
- **We want the machine to be as accurate as possible.**
    - This means we want the error $\tau(\mathcal{N})$ to be as small as possible.
- To do this, we **adjust the weights and biases** of the network until the guesses are super close to the correct answers for all the examples.

---

### Supervised Learning:

- It’s called **"supervised"** because the training data acts like a teacher—it tells the network what the right answers are.

---

### Why Squared Differences?

- Larger errors are penalized more heavily than smaller ones (this is the basis of **mean squared error** (MSE) as a loss function). (it's like saying, "If you're way off, that's a bigger problem").
- Positive and negative errors don’t cancel each other out.

---
---

### 1. **Understanding the Neural Network Notation**:

- The statement begins with: $$\mathcal{N} : \mathbb{R}^p \to \mathbb{R}^q$$
- This means that the neural network **$\mathcal{N}$** is a function that takes inputs from a $p$-dimensional space ($\mathbb{R}^p$) and maps them to a $q$-dimensional space ($\mathbb{R}^q$).
    - **$\mathbb{R}^p$**: This is the space of all ppp-dimensional real-valued vectors. These are the input features of the neural network.
    - **$\mathbb{R}^q$**: This is the space of all $q$-dimensional real-valued vectors. These are the outputs or predictions of the neural network.

---

### 2. **Weights of the Neural Network**:

- The weights of the neural network are denoted as: $\overline{\mathcal{N}} = w ⧺ b \in \mathbb{R}^n$
- Here’s what each term means:
    - **$\overline{\mathcal{N}}$**: This is the combined vector of all the parameters of the neural network. These parameters consist of:
        - **$w$**: The weights, which are assigned to the edges of the neural network and determine the contribution of each input to the network’s outputs.
        - **$b$**: The biases, which are scalar values added to the output of each neuron to allow the network to better fit the data.
    - **nnn**: The total number of parameters in the network, i.e., the sum of all weights and biases.

---

### 3. **The Symbol ⧺⧺⧺ (Concatenation)**:

- The symbol ⧺ represents **concatenation** in this context. It means that the weights w and the biases b are combined into a single vector: $\overline{\mathcal{N}} = w ⧺ b$ This essentially means:
    - Stack all the weights $w$ into one part of the vector.
    - Stack all the biases $b$ into another part of the vector.
    - Together, they form one long vector $\overline{\mathcal{N}}$ with $n$ elements.

For example:
- If $w = [w_1, w_2, w_3]$ and $b = [b_1, b_2]$
- then: $\overline{\mathcal{N}} = [w_1, w_2, w_3, b_1, b_2]$

---

### 4. **Parameter Space**:

- The combined weights and biases $\overline{\mathcal{N}}$ belong to the space Rn\mathbb{R}^nRn, meaning $\overline{\mathcal{N}}$ is an $n$-dimensional vector, where: $n = \text{(number of weights)} + \text{(number of biases)}$.

---

### Summary of Meaning:

- The neural network $\mathcal{N}$ transforms $p$-dimensional input data into $q$-dimensional output predictions.
- The parameters of $\mathcal{N}$ (weights $w$ and biases $b$) are combined into a single $n$-dimensional vector $\overline{\mathcal{N}}$ using the concatenation operator ⧺. This vector fully describes the "learnable" part of the neural network.