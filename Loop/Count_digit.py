# N=int(input("Enter the number:"))
# count=0
# while N>0:
#     N=N//10
#     count=count+1
# print(count)    



#Reverse the number
# N= int(input("enter a number:"))
# reverse=0

# while N>0:
#     digit = N%10
#     reverse= reverse*10 + digit
#     N=N//10
# print(reverse)    



#check the prime

# Factoral of number
# num= int(input("Enter a number"))
# factorial =1
# for i in range(1,num+1):
#     factorial = factorial *i
    

# print(factorial)    


#fibonacci series up to N Terms

# num= int(input("Enter a number you want to find fibonacci: "))
# a,b=0,1
# count=0
# print("Fibonacci series:")
# while count< num:
#     print(a, end=" ")
#     a,b=b,a+b
#     count +=1

#find the lcm 
# Input two numbers
# smallest digit in the number

# num=int(input("enter a number"))

# small= min(num)

# print(small)

# find the largest digit in the number

num = int(input("Enter a number: "))
digits = []

while num > 0:
    digit = num % 10
    digits.append(digit)
    # num = num // 10

largest = max(digits)
print("The largest digit is:", largest)







   
