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
3. Write a Python program to sort a list of tuples using Lambda.
'''
def sorting(list1):
    list1.sort( key = lambda x:x[1] )
    return list1

'''
4. Write a Python program to sort a list of dictionaries using Lambda in descending alphabetical order 
'''
def sort_dict(list1):
    sorted_models = sorted(sample, key = lambda x: x['color'], reverse=True)
    return sorted_models

'''
5. Write a Python program to filter a list of even integers using Lambda.
'''
def filter_even(list1):
    #x = [each  for each in list1 if each%2==0 ] # This is using list comprehension equivalent
    x1 = list(filter(lambda x : x %2==0,nums))
    return x1

'''
6. Write a Python program to square and cube every number in a given list of integers using Lambda.
'''
def cube_sq(list1,n):
    x = list(map(lambda x : x**n, list1))
    return x
def cube_wrapper(listname,n):
    y = lambda x,n : cube_sq(x,n)
    return y(listname,n)
'''
7.
'''
def check_start(sent,let):
    y = lambda x : 'Y' if x[0]==let else 'N'
    z = lambda x: True if x.startswith(let) else False
    return y(sent),z(sent)
'''
11. Write a Python program to find intersection of two given arrays using Lambda.
'''
def check_start(sent,inter):
    checking = list(filter(lambda x : x in inter, sent))
    return checking

if __name__=="__main__":
    print(adds_15(8))
    list1=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
    print(sorting(list1))
    sample = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
    print(sort_dict(sample))
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(filter_even(nums))
    print(cube_wrapper(listname,2))
    print(cube_wrapper(listname,3))
    sent = "cultivation"
    print(check_start(sent,c))
    sent = "Pultivation"
    inter = "tion"
    print(check_inter(sent,inter))
