def distance(x: int, y: int) -> float:
    return round((7 * x * y) / 10.,2)
x = int(input("NOmbre de marches: "))
y = int(input("Hauteur d'une marche (en cm): "))
print(f"Pour {x} marches de {y} cm, le gardien parcours {distance(x,y): .2f} m par semaine")