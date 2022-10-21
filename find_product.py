from unittest import result


def find_product(num1,num2,num3):
    result = 0
    if(num1 == 7):
        result = num2 * num3
    elif(num2 == 7):
        result = num3
    elif(num3 == 7):
        result = -1
    else:
        result = num1 * num2 * num3
    return result

result1 = find_product(3,5,8) 
print(result1) # 120

result2 = find_product(7,5,5)
print(result2) # 25

result3 = find_product(5,7,5)
print(result3) # 5

result4 = find_product(5,5,7)
print(result4) # -1