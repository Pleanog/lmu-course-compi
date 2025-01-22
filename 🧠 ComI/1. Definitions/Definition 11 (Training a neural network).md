

> [!CITE] Definition 11 (Training a neural network)
> Let ...
> 
>$$
\tau(\overline{\mathcal{N}}) = \sum_{i=1}^N \left( \mathcal{N}(\mathbf{x}_i) - \mathbf{y}_i \right)^2
>$$


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
-  **The currect answer $\mathbf{y}_i$**
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
