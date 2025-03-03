import numpy as np

def logistic(x, beta=1):
    return 1 / (1 + np.exp(- (beta * x)))

def predict_win_probability(Sk_A, Sk_B, beta=1):
    skill_diff = Sk_A - Sk_B  # Define x as the skill difference
    return logistic(skill_diff, beta)

# Example Inputs
Sk_A =  19.441158001442925 # Team A's skill
Sk_B = 18.768183098883284 # Team B's skill
beta = 0.2592  # Weight of skill difference

# Compute win probability
win_prob = predict_win_probability(Sk_A, Sk_B, beta=beta)
print(f"Win Probability for Team A: {win_prob:.4f}")
