#Exercise Question 8: Generate a Python list of all the even numbers between 4 to 30


def evens(start_num,end_num):
    evens_list=[]
    for n in range(start_num,end_num+1):
        if n % 2 == 0:
            evens_list.append(n)
    return evens_list

print(evens(4,30))

#Exercise Question 9: Return the largest item from the given list
import math
def largest_item(l):
    large_num = max(l)
    
    
    return large_num

print(largest_item([4, 3, 2, 4]))
