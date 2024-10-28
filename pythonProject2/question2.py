def continuous_input():
    while True:
        user_input = input("Enter something (type 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        print(user_input)

continuous_input()
