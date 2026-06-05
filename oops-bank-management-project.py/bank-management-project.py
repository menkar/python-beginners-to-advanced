import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exists.")
    except Exception as err:
        print(f"Error occurred as {err}")

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountGenerate(cls):
        alpha = random.choices(string.ascii_letters, k = 3)
        num = random.choices(string.digits, k = 3)
        splChars = random.choices("~!@#$%^&*()", k =1)
        id = alpha + num + splChars
        random.shuffle(id) # We got list

        return "".join(id)

    def createAccount(self):
        info = {
            "name": input("Tell your name : "),
            "age": int(input("Tell your age : ")),
            "email": input("Tell your email : "),
            "pin": int(input("Tell your 4 digit pin : ")),
            "accountNo": Bank.__accountGenerate(),
            "balance": 0 
        }

        if info['age'] < 18 or len(str(info["pin"])) != 4:
            print("Sorry you cannot create your account")
        else:
            print("Acount has been created successfully")
            for i in info:
                print(f"{i} : {info[i]}")

            print("Please note down your account number")
        
        Bank.data.append(info)
        Bank.__update()


    def depositMoney(self):
        accountNumber = input("Please tell your account number : ")
        pin = int(input("Please tell your pin number : "))

        userData = [i for i in Bank.data if i["accountNo"] == accountNumber and i["pin"] == pin]
        
        if userData == False:
            print("Sorry, not user found")

        else:
            amount = int(input("How much amount you want to deposit : "))
            if amount > 10000 or amount < 0:
                print("Below 10000 amount acceptable and above 0 amount")
            else:
                userData[0]["balance"] += amount
                Bank.__update()
                print("Amount deposited successfully")


    def withdrawMoney(self):
        accountNumber = input("Please tell your account number : ")
        pin = int(input("Please tell your pin number : "))

        userData = [i for i in Bank.data if i["accountNo"] == accountNumber and i["pin"] == pin]
        
        if userData == False:
            print("Sorry, not user found")

        else:
            amount = int(input("How much amount you want to withdraw : "))
            if userData[0]['balance'] < amount:
                print("Sorry, you don't have that much money into your account")
            else:
                userData[0]["balance"] -= amount
                Bank.__update()
                print("Amount withdraw successfully")


    def showDetails(self):
        print("\n\n")
        accountNumber = input("Please tell your account number : ")
        pin = int(input("Please tell your pin number : "))

        userData = [i for i in Bank.data if i["accountNo"] == accountNumber and i["pin"] == pin]
        
        if userData == False:
            print("Sorry, not user found")

        else:
            print("Your information are \n\n\n")
            for i in userData[0]:
                print(f"{i}: {userData[0][i]}")
                
            print("\n User details displayed successfully")


    def updateDetails(self):
        accountNumber = input("Please tell your account number : ")
        pin = int(input("Please tell your pin number : "))

        userData = [i for i in Bank.data if i["accountNo"] == accountNumber and i["pin"] == pin]
        
        if userData == False:
            print("Sorry, not user found")

        else:
            print("You cannot change the age, account number, balance \n")
            print("Fill the details for change or leave it empty if no change \n")

            newData = {
                "name": input("Tell your new name or press enter to skip : "),
                "email": input("Tell your new email or press enter to skip : "),
                "pin": int(input("Tell your new 4 digit pin or press enter to skip : ")),
                
            }

            if newData["name"] == "":
                newData["name"] = userData[0]["name"]
                
            if newData["email"] == "":
                newData["email"] = userData[0]["email"]

            if newData["pin"] == "":
                newData["pin"] = userData[0]["pin"]

            newData["age"] = userData[0]["age"]
            newData["accountNo"] = userData[0]["accountNo"]
            newData["balance"] = userData[0]["balance"]

            if type(newData["pin"]) == str:
                newData["pin"] = int(newData["pin"])
            
            for i in newData:
                if newData[i] == userData[0][i]:
                    continue
                else:
                    userData[0][i] = newData[i]
            
            Bank.__update()

            print("\n\n")
            print("Details are updated successfully")
            

    def deleteAccount(self):
            accountNumber = input("Please tell your account number : ")
            pin = int(input("Please tell your pin number : "))

            userData = [i for i in Bank.data if i["accountNo"] == accountNumber and i["pin"] == pin]
            
            if userData == False:
                print("Sorry, not user found") 
            else:
                check = input("Press y if you actually want to delete the account or press n : ")
                if check == 'n' or check == 'N':
                    print("Bypassed")
                else:
                    index = Bank.data.index(userData[0])
                    Bank.data.pop(index)
                    print("Account deleted successfully")
                    Bank.__update()
                    

user = Bank()


print("Press 1 for creating account : ")
print("Press 2 for depositing money : ")
print("Press 3 for withdrawing money : ")
print("Press 4 for details bank account : ")
print("Press 5 for updating account : ")
print("Press 6 for deleting account : \n")


res = int(input("Tell your response : "))


if res == 1:
    user.createAccount()

if res == 2:
    user.depositMoney()

if res == 3:
    user.withdrawMoney()

if res == 4:
    user.showDetails()

if res == 5:
    user.updateDetails()

if res == 6:
    user.deleteAccount()