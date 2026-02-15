# activation.py - activation functions
# implement identity, threshold, ReLU (sigmoid is given in main)
# method names - act_relu, act_threshold, act_identity

def act_relu(x):
    # f(x) = max(0,x)
    return max(0, x)

def act_threshold(x):
    # f(x) = 1 if x > 0 else 0
    return 1 if x >= 0 else 0

def act_identity(x):
    # f(x) = x
    return x