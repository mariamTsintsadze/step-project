def input_number(prompt_text):
    while True:
        try:
            return float(input(prompt_text))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

while True:
    #რიცხვების შეყვანა
    first_number = input_number("Enter the first number: ")
    second_number = input_number("Enter the second number: ")
    #ის ოპერაციები რომელთა შესრულებას შეგვიძლია
    all_operations = ['+', '-', '*', '/', '%', '**']

    while True:
        operation = input("Enter one of the main arithmetic operations (+, -, *, /, %, **): ")
        if operation in all_operations:
            break
        else:
            print("Invalid operation. Please enter one of: +, -, *, /, %, **.")
    
    #თითოეული ოპერაციის დროს რა მოქმედება სრულდება
    if operation == '+':
        print(f"Result: {first_number + second_number}")
    elif operation == '-':
        print(f"Result: {first_number - second_number}")
    elif operation == '*':
        print(f"Result: {first_number * second_number}")
    elif operation == '/':
        #გაყოფის დროს მეორე რიცხვი თუ ნულია იქამდე გვთხოვს შეყვანას სანამ სწორს არ შევიყვანთ
        while second_number == 0:
            print("ERROR: Division by 0 is not allowed.")
            second_number = input_number("Enter a valid second number: ")
        result = first_number / second_number
        if first_number % second_number == 0:
            print(f"Result: {int(result)}")  
        else:
            print(f"Result: {round(result, 2)}")  
    elif operation == '%':
        print(f"Result: {first_number % second_number}")
    elif operation == '**':
        print(f"Result: {first_number ** second_number}")

    #გვეკითხება უნდა თუ არა სხვა ოპერაციის შესრულება.
    continue_calculations = input("Do you want to continue calculations? (yes/no): ").strip().lower()
    if continue_calculations == 'No':
        print("Exiting the calculator. Goodbye!")
        break
