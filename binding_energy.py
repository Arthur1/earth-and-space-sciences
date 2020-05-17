# coding: utf-8

def main():
    atoms = [
        { "name": "He 3", "a": 3, "z": 2 },
        { "name": "He 4", "a": 4, "z": 2 },
        { "name": "C 12", "a": 12, "z": 6 },
        { "name": "Fe 56", "a": 56, "z": 26 },
        { "name": "Se 80", "a": 80, "z": 34 },
        { "name": "Bi 209", "a": 209, "z": 83 },
    ]
    for atom in atoms:
        print(atom["name"] + " " + str(binding_energy(atom["a"], atom["z"]) / atom["a"]))

# 質量公式に基づいて結合エネルギーを計算する
def binding_energy(a, z):
    B_VOL = 15.56
    B_SURF = 17.23
    B_COUL = 0.697
    B_SYM = 23.29

    energy = B_VOL * a
    energy -= B_SURF * (a ** (2 / 3))
    energy -= B_COUL * (z ** 2) * (a ** (-1 / 3))
    energy -= B_SYM * ((a - z) ** 2) / (2 * a)

    if z % 2 == 0 and (a - z) % 2 == 0:
        delta = -12 / (a ** (1 / 2))
    elif z % 2 == 1 and (a - z) % 2 == 1:
        delta = 12 / (a ** (1 / 2))
    else:
        delta = 0
    energy -= delta

    return energy

if __name__ == "__main__":
    main()
