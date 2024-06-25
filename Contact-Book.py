def Add(ph):
    name = input("Enter Contact Name: ")
    number = int(input("Enter Number: "))
    email = input("Enter E-mail: ")
    address = input("Enter Address: ")      
    details = {
        "name":name,
        "number":number,
        "email": email,
        "address":address
            }
    ph.append(details)
    print("Contact Added Successfully.")

def View(ph):
    if ph:
        for i,j in enumerate(ph,start=1):
            print("Contact",i,":")
            print("Name:",j['name'])
            print("Number:", j['number'])
            print("E-mail:",j['email'])
            print("Address:", j['address'])
    else:
        print("No Contacts in list...")

def Delete(ph):
    name = input("Enter a name of conatact to delete :- ")
    for i in ph:
        if i['name'].lower() == name.lower():
            ph.remove(i)
            print("Contact Permanent Removed")
            return
    print("Contact not found") 
   
def Search(ph):
    name = input("Enter the name of Contact :- ")
    print("please wait...")
    for i in ph:
        if i['name'].lower() == name.lower():
            print("Name:", i['name'])
            print("Number:", i['number'])
            print("E-mail:", i['email'])
            print("Address:", i['address'])
            return
    print("Contact not found")  


def Update(ph):
    name = input("Enter the name of Contact to Update :- ")
    print("please wait...")
    for i in ph:
        if i['name'].lower() == name.lower():
            i['number'] = int(input("enter New number: "))
            i['email'] = input("enter New E-mail: ")
            i['address'] = input("enter New Address: ")
            print("Contact Successfully Updated..")
            return
    print("Contact not found")


Phone_list = []
while True:
    print("Welcome to Contact Book Project :- ")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. Update Contact")
    print("6. Exit")
    try:
        get = int(input("Select an option above :- "))
    except:
        print("Please enter valid Number.. and try again later")
        exit()
    if get == 1:
        Add(Phone_list)
    elif get == 2:
        View(Phone_list)
    elif get == 3:
        Delete(Phone_list)
    elif get == 4:
        Search(Phone_list)
    elif get == 5:
        Update(Phone_list)
    else:
        exit()