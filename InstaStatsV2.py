import instaloader

#Creates instance of instaloader
L = instaloader.Instaloader()
username = input("Enter your instagram username: ")
password = input("Enter your instagram password: ")

#(Optional) Logs in with credentials, might be required if account is private
L.login(username, password)

