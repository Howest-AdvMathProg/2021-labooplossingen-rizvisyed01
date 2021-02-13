import math


def soft_max(x1, x2, index_cat, cats_weights):
    return upper_soft_max(x1, x2, cats_weights[index_cat]) / lower_soft_max(x1, x2, cats_weights)


def upper_soft_max(x1, x2, weights_list):
    return math.e ** calc_xk(x1, x2, weights_list)


def calc_xk(x1, x2, weights_list):
    return weights_list[0] + weights_list[1] * x1 + weights_list[2] * x2


def lower_soft_max(x1, x2, cats_weights):
    denom = 0
    for i in cats_weights:
        denom += math.e ** calc_xk(x1, x2, i)
    return denom


weights = [
    [0.01, 0.1, 0.1],
    [0.1, 0.2, 0.2],
    [0.1, 0.3, 0.3]
]

# deel 1
for i in range(0, 3):
    print("De kans dat (0.1, 0.5) bij cat ", chr(ord('a') + i), " behoort is: ", soft_max(0.1, 0.5, i, weights))

print("------------------------------------------------------------------------------")
print("De kans dat (0.1, 0.5) bij cat A behoort is: ", soft_max(0.1, 0.5, 0, weights))
print("De kans dat (1.1, 2.3) bij cat b behoort is: ", soft_max(1.1, 2.3, 1, weights))
print("De kans dat (-1.1, -2.3) bij cat c behoort is: ", soft_max(-1.1, -2.3, 2, weights))
print("De kans dat (-1.5, -2.5) bij cat c behoort is: ", soft_max(-1.5, -2.5, 2, weights))

# het model is zeker niet goed, er is lage zekerheid bij iedere waarde
