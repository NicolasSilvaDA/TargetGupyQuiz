def fibonacci(value, num1 = 0, num2 = 1):
    if num2 == value:
        print("O valor pertence a sequência de Fibonacci!")
        return True

    elif num2 > value:
        print("O valor não pertence a sequência de Fibonacci!")
        return False

    else:
        temp = num2
        num2 = num1 + num2
        num1 = temp
        fibonacci(value, num1, num2)


try:
    value = int(input("Insira um valor válido: "))
    fibonacci(value)
except:
    print("Valor inválido inserido! Tente novamente.")