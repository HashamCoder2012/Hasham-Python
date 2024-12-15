import sys
def initial_phonebook():
    rows, cols = int(input("Please enter initial number of contacts: ")),2
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

    print(phone_book)
    return phone_book
print("Welcome to PhoneBook app")
pb=initial_phonebook()
print(pb)                        
                         