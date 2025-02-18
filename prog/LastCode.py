from random import *
name = input("Ako sa voláš\n")
print(f"Ahoj {name} rád Ťa spoznávam :")
birthdate = input(f"{name} v ktorom roku si sa narodil?\n")
name2 = choice(("Alena", "Barbora", "Eva", "Sofia"))
print(f"A spominal si v roku {birthdate} sa narodila aj {name2}")
