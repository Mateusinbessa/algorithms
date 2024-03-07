#@Description: Uma função recursiva simples para decrementar um número
def decrement(number):
    if number <= 0:
        print("Caso base")
    else:
        print(f'Caso recursivo, number: {number}')
        number -= 1
        decrement(number)

def fat(x):
    if x == 1:
        return 1
    else:
        print(x)
        return x * fat(x-1)
    
print(fat(3))
