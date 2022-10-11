# PySRTest
Experiments with [PySR](https://github.com/MilesCranmer/PySR).

**Language: Python**

**Start: 2022**

## Why
I wanted to test PySR (High-Performance Symbolic Regression in Python) to see if it was capable to find known physics formulas from data.

## Example
I considered the case of a [falling body](https://en.wikipedia.org/wiki/Equations_for_a_falling_body). In particular, the formula to calculate the time _t_ taken for an object to fall distance _d_:

$$ t = \sqrt{\frac{2d}{g}} $$

I created 100 data points including 2 random useless columns and added some random noise to the _y_ (i.e., _t_):

```python
# falling body: t = sqrt(2 * h / g)  where g is 9.8
X = 100 * abs(np.random.randn(100, 3)) # h + 2 useless variables
y = np.sqrt(2 * X[:, 0] / 9.8) + np.random.randn(100) # + a random error
```

The results were:

```python
PySRRegressor.equations = [
            pick     score                                           equation      loss  complexity
        0         0.000000                                           3.867227  4.889949           1
        1         0.452888                                 (x0 * 0.038884826)  1.976655           3
        2   >>>>  0.575769                          sqrt_abs(x0 * 0.21829543)  1.111418           4
        3         0.009650        ((sqrt_abs(x0) * 0.50124663) + -0.34722018)  1.090174           6
        4         0.006606            ((sqrt_abs(x0) * 0.46379715) + inv(x1))  1.082995           7
        5         0.021643        sqrt_abs(x0 * (exp(inv(x1)) * -0.21177335))  1.059808           8
        6         0.007409   sqrt_abs(x0 * (exp(exp(inv(x1))) * -0.07769506))  1.051985           9
        7         0.021338  (sqrt_abs(x0 * (exp(inv(x1)) * 0.25029796)) + ...  1.029775          10
        8         0.020468  sqrt_abs((cos(sin(sin(x2 * 0.59266335))) * 0.2...  1.008913          11
        9         0.056676  sqrt_abs((sqrt_abs(sqrt_abs(sin(exp(x1 * 0.232...  0.953322          12
        10        0.011135  ((sqrt_abs(x0) + sin(cos(sqrt_abs(x0 * 4.90378...  0.942765          13
        11        0.010939  ((sqrt_abs(x0) + sin(inv(cos(sqrt_abs(x0 * 4.7...  0.932509          14
```

The most accurate result is marked with ">>>>". It correctly ignored the useless variables (x1, x2) and it found a constant of 0.21 which is quite close to 2 / 9.8 = 0.20.