def decrement(number):
    if number <= 0:
        print("Caso base")
    else:
        print(f'Caso recursivo, number: {number}')
        number -= 1
        decrement(number)

decrement(20)

