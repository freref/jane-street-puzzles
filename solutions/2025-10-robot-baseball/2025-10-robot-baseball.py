from scipy.optimize import minimize_scalar

def get_q(p):
    V = {}
    sigma_dict = {}
    beta_dict = {}
    Q = {}
    states = [(b, s) for b in range(4) for s in range(3)]
    sorted_states = sorted(states, key=lambda x: -(x[0] + x[1]))
    for state in sorted_states:
        b, s = state
        if b + 1 >= 4:
            N_ball = 1.0
        else:
            N_ball = V.get((b+1, s), None)
        if s + 1 >= 3:
            N_strike = 0.0
        else:
            N_strike = V.get((b, s+1), None)
        A = N_strike - N_ball
        denom = A + p * (N_strike - 4)
        if abs(denom) < 1e-10:
            mix_prob = 0.0
        else:
            mix_prob = A / denom
        if mix_prob < 0 or mix_prob > 1:
            U11 = N_ball
            U12 = N_strike
            U21 = N_strike
            U22 = 4*p + (1-p)*N_strike
            denom_mat = U11 + U22 - U12 - U21
            if abs(denom_mat) < 1e-10:
                V[state] = 0.0
            else:
                V[state] = (U11 * U22 - U12 * U21) / denom_mat
            mix_prob = max(0, min(1, mix_prob))
        sigma_dict[state] = mix_prob
        beta_dict[state] = mix_prob
        V[state] = N_ball + mix_prob * A
        if b == 3 and s == 2:
            Q[state] = 1.0
        else:
            q_val = 0.0
            sig = sigma_dict[state]
            bet = beta_dict[state]
            if b + 1 >= 4:
                q_next_ball = 0.0
            else:
                q_next_ball = Q.get((b+1, s), None)
            q_val += (1 - sig) * (1 - bet) * q_next_ball
            if s + 1 >= 3:
                q_next_strike = 0.0
            else:
                q_next_strike = Q.get((b, s+1), None)
            q_val += sig * (1 - bet) * q_next_strike
            q_val += (1 - sig) * bet * q_next_strike
            q_val += sig * bet * (1 - p) * q_next_strike
            Q[state] = q_val
    return Q[(0, 0)]

res = minimize_scalar(
    lambda p: -get_q(p),
    bounds=(0, 1), method='bounded',
    options={'xatol': 1e-12,'maxiter': 1000}
)
max_q = -res.fun
print(f"{max_q:.10f}")
