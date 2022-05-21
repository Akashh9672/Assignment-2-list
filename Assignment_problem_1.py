size=int(input("Enter of size of list:"))
list=[]
for i in range(size):
    first_value=int(input("enter first number:"))
    second_value=int(input("enter second number:"))
    tuple=(first_value,second_value)
    list.append(tuple)
print("Your list:",list)
len=len(list)
for i in range(0,len):
    for b in range(0,(len-i-1)):
        if(list[b][1]>list[b+1][1]):
            sample=list[b]
            list[b]=list[b+1]
            list[b+1]=sample
print("sorted list:",list)
