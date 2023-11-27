def draw_rectangle(width,height):
    cloture = "|" + "-" * (width - 2) + "|"
    center = "|" + " " * (width - 2) + "|"
    print(f"{cloture}")
    for k in range(1, height-1):
        print(f"{center}")
    print(f"{cloture}")
        
draw_rectangle(10,3)