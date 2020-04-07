import operator

#remove duplicates function from list
def removeDuplicates(mylist):

    bmylist=[]
    for i in mylist:
        if i not in bmylist:
            bmylist.append(i)
        
    mylist=bmylist
    print("List without duplicate numbers:",mylist)

    sortList(mylist)

#Sort function for list
def sortList(newlist):
    
    newlist.sort()
    print("Sorted List:",newlist)


#Remove function for dictionary
def removeDuplicates2(a_dict):
    
    b_dict={}

    for key,value in a_dict.items():
        if value not in b_dict.values():
            b_dict[key]=value

    a_dict=b_dict
    print ("Dictionary without duplicates:",a_dict)

    sortList2(a_dict)
    

#Sort function for dictionary
def sortList2(mydict):
   
    newa_dict= sorted(mydict.items(), key=operator.itemgetter(1))
    mydict=newa_dict
    print("Sorted Dictionary:",mydict)


#list input
list1=[]
print("First we are gonna create a list.")
n=int(input("Enter number of elements in the list : ")) #Zhtaw ton arithmo twn elements pou tha uparxoun sthn lista
print("Enter the numbers : ")
for i in (range(0,n)):
    ele= int(input())
    list1.append(ele)

print("Current List:",list1)
removeDuplicates(list1)
#Kalw thn removeduplicate kai tautoxrona afou afairethoun oi diploeggrafes , kanw kai sort thn lista mou.

print("-----------------------------------------")

#dictionary input
dict1={}
print("Now we are gonna create a dictionary.")
n=int(input("Enter number of elements in the list : ")) #Zhtaw ton aritmo twn element pou tha uparxoun sto dictionary
for i in (range(0,n)):
    print("First enter your key and then your value:")
    mykey= input()
    myvalue=input()
    dict1[mykey]=myvalue

print("Current Dictionary:",dict1)
removeDuplicates2(dict1)
#Kalw thn removeduplicate2 kai tautoxrona afou afairethoun oi diploeggrafes , kanw kai sort to dictionary mou.






