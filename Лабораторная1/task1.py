def find_missing_and_replace(lst):
    
    missing_element = None
    for element in lst:
        if element is None:
            missing_element = element
            break

    
    total_sum = 0
    count = 0
    for element in lst:
        if element is not None:
            total_sum += element
            count += 1

    
    if missing_element is not None:
        average = total_sum / count
        lst[lst.index(None)] = average

    return lst


numbers = [1, 2, None, 4, 5]
result = find_missing_and_replace(numbers)
print(result)
