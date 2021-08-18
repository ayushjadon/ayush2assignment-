# creating class cat
class Cat:
    pass
    def speak_once (self):
     print("meau")
    def set_breed(self,breed):
        self.breed =breed
    def get_breed(self):
        return self.breed
    def walk_twice(self):
     print("walk")
# d is located for class cat
d =Cat()
# here we set breed name
d.set_breed("indian cat")
# checking outputs for speak walk class type  and get the breed and cat is in class main
print(type(d.speak_once))
print(type(d.walk_twice))
d.speak_once()
d.walk_twice()
print(d.get_breed())
print(type(d))
