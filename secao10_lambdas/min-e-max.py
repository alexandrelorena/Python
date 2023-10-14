"""
Min e Max

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos.

"""
# ------------------------------ ↓ Min e Max ↓ -------------------------------------

print(f"\033[33m{'-' * 70}\n\033[94m{'↓ Min e Max ↓'.center(70)}\033[33m\n{'-' * 70}\033[0m")

# ------------------------- ↓ lista ↓ ----------------------------

print(f"\033[33m{'-' * 70}\n\033[94m{'↓ lista ↓'.center(70)}\033[33m\n{'-' * 70}\033[0m")

lista = [1, 8, 4, 99, 34, 129]
print(f"{'↓ max() ↓'.center(70)}\n")
print(max(lista))
print(f"{'↓ min() ↓'.center(70)}\n")
print(min(lista))
print(f"{'↓ tipo ↓'.center(70)}\n")
print(type(lista))

# ------------------------- ↓ tupla ↓ ----------------------------

print(f"\033[33m{'-' * 70}\n\033[94m{'↓ tupla ↓'.center(70)}\033[33m\n{'-' * 70}\033[0m")

tupla = (1, 8, 4, 99, 34, 129)
print(f"{'↓ max() ↓'.center(70)}\n")
print(max(tupla))
print(f"{'↓ min() ↓'.center(70)}\n")
print(min(tupla))
print(f"{'↓ tipo ↓'.center(70)}\n")
print(type(tupla))

# ------------------------- ↓ conjunto ↓ ----------------------------

print(f"\033[33m{'-' * 70}\n\033[94m{'↓ conjunto ↓'.center(70)}\033[33m\n{'-' * 70}\033[0m")

conjunto = {1, 8, 4, 99, 34, 129}
# ------------------------- ↓ max ↓
print((f"conjunto = {conjunto} | " + f"\033[36mTipo: {type(conjunto)}\n\033[0m").center(70))
print(f"{f' max() >> {max(conjunto)} '.center(70)}\n")
# ------------------------- ↓ min ↓ ----------------------------\033[35m:
print(f"{f' min() >> {min(conjunto)} '.center(70)}\n")
# ------------------------- ↓ tipo ↓ ----------------------------
print(f"{'↓ tipo ↓'.center(70)}\n")
print(f"{f' {type(conjunto)} '.center(70)}\n")


# ---------------------------------------------------------------

conjunto = {1, 8, 4, 99, 34, 129}
print(f"{'↓ max() ↓'.center(70)}\n")
print(max(conjunto))
print(f"{'↓ min() ↓'.center(70)}\n")
print(min(conjunto))
print(f"{'↓ tipo ↓'.center(70)}\n")
print(type(conjunto))
