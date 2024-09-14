string = str(input())
As = 0


caixa_alta = string.upper()

for c in caixa_alta:
    if c == "A":
        As += 1


print(f"A letra 'a' ocorre {As} vezes na string informada")