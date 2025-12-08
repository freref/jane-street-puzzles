# Robot Javelin
Define $g = \frac{\sqrt{5}-1}{2}$. Spears adapts to the signal using thresholds $T_0 = 0.5$ (when $X < g$) and $T_1 = 1 - \frac{g}{2}$ (when $X > g$). Java-lin maximizes her advantage by shifting her cutoff to $7/12$.

The total win probability is the sum over three intervals:
$$P(\text{Win}) = \underbrace{\frac{7}{12}\left(\frac{3}{8}\right)}_{X \in [0, \frac{7}{12}], \text{Reroll}} + \underbrace{\int_{7/12}^g (1.5x - 0.5) dx}_{X \in [\frac{7}{12}, g], \text{Keep}} + \underbrace{\left(\frac{5}{8}g - \frac{1}{8}\right)}_{X \in [g, 1], \text{Keep}}$$

Result:
$$\frac{229 - 60\sqrt{5}}{192} \approx 0.4939370904$$
