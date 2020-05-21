#Ref - https://www.w3resource.com/python-exercises/lambda/index.php

''' 
1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, 
also create a lambda function that multiplies argument x with argument y and print the result.
'''
def adds_15(nums):
    x = lambda a : a +15
    y = lambda a,b : a * b
    return x(nums), y(nums, 5)

'''
2. Write a Python program to sort a list of tuples using Lambda.
'''
def sorting(list1):
    list1.sort( key = lambda x:x[1] )
    return list1
    
if __name__=="__main__":
    print(adds_15(8))
    list1=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
    print(sorting(list1))
