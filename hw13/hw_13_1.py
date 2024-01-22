with open('text_file.txt', 'w') as file:
    while True:
        user_input = input("Input data string (empty string to finish) >>> ")
        if user_input == "":
            break
        file.write(user_input + '\n')

print("Data is recorded to the 'text_file.txt'")
