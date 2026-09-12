# Create a User class with a login() method. Create an Admin class that inherits from User and adds a delete_user() method.

class User:
    def login(self):
        print("User logged in")


class Admin(User):
    def delete_user(self):
        print("User deleted")


admin = Admin()

admin.login()
admin.delete_user()