# Robot Javelin

Define

$$
g = \frac{\sqrt{5}-1}{2}.
$$

Spears adapts to the signal using thresholds

$$
T_0 = 0.5
$$

when

$$
X < g,
$$

and

$$
T_1 = 1 - \frac{g}{2}
$$

when

$$
X > g.
$$

Java-lin maximizes her advantage by shifting her cutoff to

$$
\frac{7}{12}.
$$

The total win probability is the sum over three intervals:

```math
P(\text{Win})
= \frac{7}{12}\cdot\frac{3}{8}
+ \int_{7/12}^{g} (1.5x - 0.5)\,dx
+ \left(\frac{5}{8}g - \frac{1}{8}\right).
```

Result:

$$
\frac{229 - 60\sqrt{5}}{192} \approx 0.4939370904.
$$
