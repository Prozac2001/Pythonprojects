
Bio_data = {
    }

print("Welcome to my Bio data\nRegister your data Below\n")

Bio_data["Surname"] = input("Surname: ")
Bio_data["Other names"] = input("Other names: ")
Bio_data["Date of birth"] = input("Date of birth: ")
Bio_data["Gender"] = input("Gender: ")
Bio_data["Course"] = input("Course: ")
Bio_data["Username"] = input("Username: ")
Bio_data["Password"] = input("Password: ")
Bio_data["Confirm password"] = input("Confirm password: ")

print("Thank you for registering\nEnter your details to Continue\n")
Username = input("Enter username: ")
Password = input("Enter password: ")

if Username == Bio_data["Username"] and Password == Bio_data["Password"]:
    print("Data Successful")

else:
    print("Incorrect Data!!! Try again!")
