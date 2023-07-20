class Test:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age

test = Test('dylan','100')

print(test.__dict__)