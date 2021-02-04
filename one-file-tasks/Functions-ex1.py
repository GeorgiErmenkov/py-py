#Exercise Question 4: Create a function showEmployee() in such a way that it should accept employee 
# name, and it’s salary and display both, and if the salary is missing in function call it should 
# show it as 9000

def showEmployee(name, salary=9000):
    print('Employee', name, 'salary is', salary)

showEmployee('John')

#Exercise Question 5: Create an inner function to calculate the addition in the following way
#Create an outer function that will accept two parameters a and b
#Create an inner function inside an outer function that will calculate the addition of a and b
#At last, an outer function will add 5 into addition and return it

def add5(a, b):
    def add(a, b):
        return a+b
    res = add(a, b) + 5
    return res

result = add5(5, 10)
print(result)

#Exercise Question 6: Write a recursive function to calculate the sum of numbers from 0 to 10

def sumof(num):
    if num > 0:
        return num + sumof(num-1)
    else:
        return 0

res = sumof(20)
print(res)
