def common_element(lst1,lst2):
    new_list = []
    
    for x in lst1:
        for y in lst2:
            
            if x == y:
                if x not in new_list:
                    new_list.append(x)
    
    return new_list

print(common_element([1,2,3],[5,2,6,1,1]))