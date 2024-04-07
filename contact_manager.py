import os

def command():
    while True:
        print("\nChoose the command you want to execute. \n\n [1] View Contacts \n [2] Store Contacts \n [3] Delete Contacts")

        command_option = int(input("Please enter an option: "))

        if command_option not in [1, 2, 3]:
            print("Invalid Command \n")
        else:
            if command_option == 1:
                # perform command 
                if not os.path.isfile(path):
                    print("No contacts found.")
                    continue

                print("Viewing Contacts\n")
                
                with open(path, 'r') as file:
                    cont = file.readlines()
                    for idx, line in enumerate(cont, 1):
                        print(f"{idx}. {line.strip()}")
                print('================================')
            elif command_option == 2:
                # perform command 
                contact_name = input("Please enter contact name: ")
                contact_number = input("Please enter phone number: ")

                with open(path, 'a') as file:
                    file.write(f"{contact_name}: {contact_number}\n")
                print("Contact added successfully!")
            elif command_option == 3:
                # perform command 
                if not os.path.isfile(path):
                    print("No contacts found.")
                    continue

                print("Deleting Contacts\n")
                
                with open(path, 'r') as file:
                    cont = file.readlines()
                    for idx, line in enumerate(cont, 1):
                        print(f"{idx}. {line.strip()}")
                        
                contact_to_delete = int(input("Please enter the number of the contact you want to delete: "))
                if contact_to_delete < 1 or contact_to_delete > len(cont):
                    print("Invalid contact number.")
                    continue
                
                with open(path, 'w') as file:
                    for idx, line in enumerate(cont, 1):
                        if idx != contact_to_delete:
                            file.write(line)
                print("Contact deleted successfully!")
            else: 
                print("Invalid Command")

path = "contacts.txt"

name = input("Please enter your name: \n\n")
print(f"Hello {name}! Welcome to the Contact management Software\n")

command()
