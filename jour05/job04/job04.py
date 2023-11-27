def tapis(n: int) -> None:
    cloture = "+" + "-" * n + "+"
    print(f"{cloture}")
    for i in range(n):
        interieur = "#" * (n-i-1) + " " + "#" * i
        print(f"|{interieur}|")
    print(f"{cloture}")
    
tapis(10)