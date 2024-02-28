#Asymptotic anolysis of different algorithms
print("Different Type of Analysis")

''' 1)  LOOPS'''

for i in range(0, n): #executes n times
    print('Number is ', i) # constant time

'''The time complexity is O(n)'''

'''2)  Nested loops'''

for i in range(0, n): #outer loop executes n times
    for j in range(0, n): #inner loop execute for n times
        print(i, j) #constant time

'''The time complexity is O(n^2)'''

'''3)  If then statemenst'''

def evenodd(n):
    if n % 2 == 0:
        print("event") #constant time
    else:
        print("odd") #constant time

'''4) Logarithmic '''

def logarithm(n):
    i = n
    while i >= 1:
        i = i // 2
        print(i)
logarithm(44)
'''The time time complexity is O(nlogn)'''



