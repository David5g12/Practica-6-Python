print("                    Python")
print("           David Hernandez Hernandez")
print("           Proyecto de estructura de datos")
print("\n")

aves = ["Loro gris", "Paloma de diamante", "Coctel"]

print("-----------------------------------------------------------------|")
print("   Los valores de la lista antes de insertar las demas aves:     |")
print("-----------------------------------------------------------------|")


aves_str = "          | ".join(aves)
print(aves_str)

print()
print("-----------------------------------------------------------------|")
print("\n")


aves.append("Mayna")
aves.append("periquitos")
aves.append("cacatua")

print("------------------------------------------------------------------------------------|")
print("           Los valores de la lista despues de insertar las demas aves es:           |")
print("------------------------------------------------------------------------------------|")


aves_str = "   | ".join(aves)
print(aves_str)

print()
print("------------------------------------------------------------------------------------|")