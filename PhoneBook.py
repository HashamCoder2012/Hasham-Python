import sys
def initial_phonebook():
    rows, cols = int(input("Please enter initial number of contacts: ")),3
    phone_book =[]
    print(phone_book)
    for i in range(rows):
        temp=[]
        for j in range(cols):
            if j==0:
                temp.append(str(input("Enter name*: ")))
                if temp[j] =='' or temp[j] == ' ':
                    sys.exit("Name is a madatory field.Process exiting due to blank field...")
            if j ==1:
                temp.append(int(input("Enter number*: ")))
        phone_book.append(temp)

    return phone_book
def add_contact(pb):
    dip=[]
    for i in range(len(pb[2])):
        if i ==0:
            dip.append(str(input("Enter name: ")))
        if i == 1:
            dip.append(int(input("Enter number: ")))
        if i ==2:
            dip.append(int(input("Enter Number: ")))
    pb.append(dip)
    return pb
print("Welcome to PhoneBook app")
pb=initial_phonebook()
print(pb)
add=input("Do you want to add a new contact?(y/n)")
if add=="y":
    pb=add_contact(pb)
    print(pb)

def remove_existing(pb):
    query=str(input("Please enter the name of the contact you wish to remove: "))
    temp=0
    for i in range(len(pb)):
        if query == pb[i][0]:
            temp +=1
            print(pb.pop(i))
                         