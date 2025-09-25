class User:
    def __init__(self, name:str =None, email:str =None, age:int =None):
        self.name = name
        self.email = email
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age} {self.email}"


    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_age(self):
        return self.age

a= User("test","testemail",38)
print(a.get_name())
print(a.get_email())
print(a.get_age())




