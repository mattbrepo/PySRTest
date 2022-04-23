import numpy as np
from pysr import PySRRegressor

if False:
  # example from the git repo: https://github.com/MilesCranmer/PySR
  X = 2 * np.random.randn(100, 5)
  y = 2.5382 * np.cos(X[:, 3]) + X[:, 0] ** 2 - 0.5
else:
  # falling body: t = sqrt(2 * h / g)  where g is 9.8
  X = 100 * abs(np.random.randn(100, 3)) # h + 2 useless variables
  y = np.sqrt(2 * X[:, 0] / 9.8) + np.random.randn(100) # + a random error

model = PySRRegressor(
    niterations=5,
    binary_operators=["+", "*"],
    unary_operators=[
        "cos",
        "exp",
        "sin",
        "inv(x) = 1/x",  # Custom operator (julia syntax)
        "sqrt"
    ],
    model_selection="best",
    loss="loss(x, y) = (x - y)^2",  # Custom loss function (julia syntax)
)

model.fit(X, y)
print(model)

