# PySRTest
Experiments with [PySR](https://github.com/MilesCranmer/PySR)

**Language: Python**

**Start: 2022**

## Why
I wanted to test PySR (High-Performance Symbolic Regression in Python) to see if it was capable to find known physics formulas from data.

## Example
I considered the case of a [falling body](https://en.wikipedia.org/wiki/Equations_for_a_falling_body). In particular, the formula to calculate the time (_t_) taken for an object to fall distance (_d_):

![formula](/images/formula.jpg)

I created 100 data points including 2 random useless columns and adding some random noise:

```python
# falling body: t = sqrt(2 * h / g)  where g is 9.8
X = 100 * abs(np.random.randn(100, 2)) # h + 2 useless variables
y = np.sqrt(2 * X[:, 0] / 9.8) + np.random.randn(100) # + a random error
```

The result was:

```python
PySRRegressor.equations = [
           pick     score                                           equation      loss  complexity
        0        0.000000                                          3.8280957  3.960987           1
        1        0.248942                                 (x0 * 0.038038906)  2.407549           3
        2  >>>>  0.935639                          sqrt_abs(x0 * 0.21392302)  0.944566           4
        3        0.007042           ((sqrt_abs(x0) + 0.6000069) * 0.4366105)  0.931357           6
        4        0.005178             sqrt_abs((x0 * -0.21441233) + cos(x0))  0.926547           7
        5        0.041718  ((sqrt_abs(x0 + -3.4519234) * 0.4204526) + 0.5...  0.888689           8
        6        0.037596  sqrt_abs((x0 * -0.21530855) + sin(x1 * 1.62781...  0.855898           9
        7        0.005490  sqrt_abs((x0 * 0.21296117) + (sin(x1 * -1.8019...  0.846552          11
```

The most accurate one is marked with ">>>>". It correctly ignored the useless variables (x1, x2) and it found a constant of 0.21 which is quite close to 2 / 9.8 = 0.20.