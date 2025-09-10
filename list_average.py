def calculate_average(numbers):
    sum = 0
    
    if len(numbers) == 0:
        return 0
    
    for x in numbers:
        sum += x 
        
    return sum / len(numbers)

print(calculate_average([1,2,3,4,5]))  
print(calculate_average([]))
print(calculate_average([2,3,4,5]))