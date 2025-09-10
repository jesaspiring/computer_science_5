def reverse_list(lst):
    new_list = []
    
    for x in range(len(lst)-1,-1,-1):
        new_list.append(lst[x])

print(reverse_list([1,2,3]))