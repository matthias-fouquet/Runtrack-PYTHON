#Proposition de fonction 1

def Calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erreur : division par zéro"
    elif operator == '%':
        return num1 % num2
    else:
        return "Opérateur inconnu"


print(Calcule(10, '+', 5))
print(Calcule(10, '-', 3))
print(Calcule(10, '*', 2))
print(Calcule(10, '/', 0))
print(Calcule(10, '%', 3))