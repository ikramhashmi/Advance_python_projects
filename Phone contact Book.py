import pyfiglet
text= "Python phone contact"
new_text = pyfiglet.figlet_format(text)
print(new_text)


dic={}
def add_contact(dic):

  while True:
    user_name= input("Enter name:\n")
    number = input("Enter number\n")
    if len(number)==11 and number.isdigit():
      dic.update({user_name:number})
      print("****Contact added successfully****")
      break
    else:
     print("Error, 10 digit number was not inputted and/or letters were inputted.")
     continue


def search(dic):
  user_name= input("Enter name:\n")
  if user_name in dic:
   print(dic[user_name])
  else:
   print("****Contact not found****")


def delete(dic):
  user_name= input("Enter name:\n")
  if user_name in dic:
     del dic[user_name]
     print("****Contact deleted successfully****")
  else:
     print("****Contact not found****")



def show(dic):
  for key,value in dic.items():
    print(f"{key}:{value}")




def main():
  
  while True:
    print("1:Add a Contact")
    print("2:Search for a Contact")
    print("3:Delete a Contact")
    print("4:View All Contacts")
    print("5:Exit")
    option = input("Choose an option:\n")
    if option == "1":
        add_contact(dic)
        continue
    elif option =="2":
        search(dic)
        continue
    elif option =="3":
        delete(dic)
        continue
    elif option =="4":
        show(dic)
        continue
    elif option =="5":
        break
    else:
        print("Invalid option")


main()        