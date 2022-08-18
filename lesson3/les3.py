class User:
    count1 = 1

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_name(self):
        print(self.name)


user1 = User('bobi',14)

user1.get_name()
