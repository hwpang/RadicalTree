Ts = [300, 400, 500, 600, 800, 1000, 1500]

columns = ["H298 (kcal/mol)", "S298 (cal/mol/K)", "Sint298 (cal/mol/K)"]
for T in Ts:
    columns.append(f"Cp{T} (cal/mol/K)")