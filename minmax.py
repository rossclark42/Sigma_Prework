def get_numbers():
    array = []
    while True:
        user_input = input("Enter a number or write done to end: ")
        if user_input.lower() == "done":
            break
        elif (user_input.lstrip("-")).isdigit():
            array.append(int(user_input))
        else:
            print("Please enter a valid number or 'done'.")
    return array


def min_max(values):
    lowest = values[0]
    highest = values[0]
    for num in values:
        if num < lowest:
            lowest = num
        elif num > highest:
            highest = num
    return [lowest, highest]


numbers = get_numbers()
print(min_max(numbers))
