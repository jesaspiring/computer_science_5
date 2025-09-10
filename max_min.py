def max_min(numbers):
    if not numbers:
        return None
    
    current_max_num = numbers[0]
    current_min_num = numbers[0]
    
    for x in numbers[1:]:
        if x < current_min_num:
            current_min_num = x
        if x > current_max_num:
            current_max_num = x
    
    return current_min_num, current_max_num    

numbers = list()
while True:
    user_input = input("Enter a number: ")
    
    if user_input.lower() == "done":
        break
    else:
        numbers.append(int(user_input))

print(max_min(numbers))