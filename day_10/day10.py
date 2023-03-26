import art

print(art.logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculation():
    num1 = float(input("What's the first number? "))
    for operator in operations:
        print(operator)

    operation = input("Pick an operation from the line above: ")
    num2 = float(input("What's the second number? "))
    answer = operations[operation](num1, num2)

    print(f"{num1} {operation} {num2} = {answer}")

    to_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

    if to_continue == "y":
        continue_calc = True
    else:
        continue_calc = False

    while continue_calc:
        previous_answer = answer
        operation = input("Pick another operation: ")
        next_num = float(input("What's the next number? "))
        answer = operations[operation](previous_answer, next_num)
        print(f"{previous_answer} {operation} {next_num} = {answer}")
        to_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if to_continue != "y":
            continue_calc = False
    print(art.logo)
    calculation()


calculation()
