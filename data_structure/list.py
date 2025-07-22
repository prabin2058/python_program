# num =int(input("enter the number of elemnents: "))

# user_list = []

# for i in range(num):
#     element = int(input("enter element: "))
#     user_list.append(element)
# total= sum(user_list)

    
# print("the element: ", user_list) 
# print("the sum is: ", total)  


# program tocount the number in the list 

# num= int(input("enter number of list: "))

# list_number=[]

# for i in range(num):
#     element= int(input("enter the elements: "))
#     list_number.append(element)
# count_number=int(input("enter number do you want count: "))
# counnts =list_number.count(count_number)
# print(f" the count number of {count_number} in list is: ", counnts)


#remove the even number
# lists = [2,5,4,6,7,8]
# new_list= []
# for i in lists:
#     if i% 2 != 0:
#         new_list.append(i)
# print(new_list)


#find small and large number in list

# lists = [2,5,4,6,7,8]


# maximun = max(lists)
# min = min(lists)
# print(maximun,min)




# chcek in the fruit is in the list or not

fruits = ["apple", "kiwi", "banana","pineapple"]

check= input("enter a fruit to check: ")

if check in fruits:
    print("found")
else:
    print("not found")    