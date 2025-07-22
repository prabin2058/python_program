# dic={
#     "name": "prabin",
#     "age": 20,
#     "class": 10,
#     "roll": 23
# }
# print(dic["roll"])
# print(dic["age"])


#take input from user
# dic={}

# dic["name"]=input("enter a name:")
# dic["age"]= int(input("enter a age: "))

# print(dic)


#loop to take a input

# contact={}
# for i in range(3):
#     name = input("enter a name: ")
#     contact[name]=int(input("enter a contact number: "))
# print("\n all the contact") 
# print(contact)

# input the marks of 5 subject and total and average is calculate 

# marks={}

# for i in range(5):
#     name= input("enter a name of subject: ")
#     marks[name]=int(input("enter a marks: "))
#     total= sum(marks.values())
#     avg= total/5
# print(marks)
# print(total)    
# print(avg)


#merge two dictionary

# fruit={
#     "mango":50,
#     "apple":55

# }
# fruits2={
#     "kiwi":60
# }  
# fruits=fruit.copy()
# fruits.update(fruits2)
# print(fruits)




#reverse the key value
# dic={}

# for i in range(2):
#     key = input("enter a key: ")
#     value= input("enter a values: ")
#     dic[key]=value

# print(dic)

# reverse_dic={}
# for key, value in dic.items():

#     reverse_dic[value]=key
# print("reverse value",reverse_dic)    

# keys and there list

data= {}


for i in range(2):
    name=input("enter a name: ")
    marks=[]
    for i in range(3):
        mark=int(input("enter a marks of student: "))
        marks.append(mark)
        data[name]=marks
print("the data is :",data)        
   
