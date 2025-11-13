"""Program to accept a list of numbers and print all numbers greater than it average @Aakashninan IMCA Rollno:02"""
my_list=[]
num=int(input("Enter the number of elements in the list"))
for i in range(0,num):
    element=int(input("Enter the element"))
    my_list.append(element);
avg=sum(my_list)/len(my_list)
print("Average :- ",sum(my_list)/len(my_list))
for i in my_list:
    if(i>avg):
        print(i)
          
