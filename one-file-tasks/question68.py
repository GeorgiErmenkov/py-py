#Please write a program using generator to print the even numbers between 0 and n in comma separated 
# form while n is input by console.

#Example:
#If the following n is given as input to the program:
#10
#Then, the output of the program should be:
#0,2,4,6,8,10
#Hints:
#Use yield to produce the next value in generator.
#In case of input data being supplied to the question, it should be assumed to be a console input.



#I  made it with loops

n = int(input())
val_list = []
for i in range(0, n+1):
    if i % 2 == 0:
        val_list.append(str(i))

print(','.join(val_list))

# Aprroach with while loop

m = int(input())
answer = ''
i = 0
while (i <= m):
    if i % 2 == 0 and i != m :
        answer += str(i) + ','
    elif i % 2 == 0 and i == m:
        answer += str(i)
    i += 1
print(answer)

