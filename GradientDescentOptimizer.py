import numpy as np
import matplotlib.pyplot as plt

def generate_data():
    x = np.linspace(20, 40, 100)
    true_a, true_b = 2, 5  # True parameters
    y = true_a * np.log(x) + true_b + np.random.normal(0, 0.5, size=x.shape)
    return x, y

def loss(a, b, x, y):
    y_pred = a * np.log(x) + b
    return np.mean((y_pred - y) ** 2)

def gradient_descent(x, y, lr=0.01, epochs=1000):
    a, b = np.random.randn(), np.random.randn()
    n = len(x)
    
    for _ in range(epochs):
        y_pred = a * np.log(x) + b
        da = (2/n) * np.sum((y_pred - y) * np.log(x))
        db = (2/n) * np.sum(y_pred - y)
        
        a -= lr * da
        b -= lr * db
        
    return a, b

# Generate data
x, y = generate_data()

# Run gradient descent
a_opt, b_opt = gradient_descent(x, y)


print(f'Optimized parameters: a = {a_opt:.4f}, b = {b_opt:.4f}')
