class MyBaseClass(object):
    def method_one(self):
        print("MyBaseClass::method_one()")


class MyChildClass(MyBaseClass):
    def method_one(self):
        print("MyChildClass::method_one()")

def call_method_one(obj):
    obj.method_one()

instanceOne = MyBaseClass()
instanceTwo = MyChildClass()

call_method_one(instanceOne)
call_method_one(instanceTwo)