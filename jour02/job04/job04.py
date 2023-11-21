
    
N = int(input("Veuillez saisir un entier supérieur à zéro (N) : "))

if N <= 0:
        print("Veuillez saisir un entier supérieur à O")
        
else :
        for i in range(1, N + 1):
                print(f"\nTable de Multiplication de {i} :")
                
                for j in range(1, 11):
                        result = i * j
                        print(f"{i} x {j} = {result}")