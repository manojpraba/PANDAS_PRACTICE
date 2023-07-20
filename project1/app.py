from src.person import Person




##positional and keyword argumets

def hello(name,lastname,number):
    pass
def method(*args,**kwargs):
    print(args)
    print(kwargs)

list=(10,12,30)
dictvalues={"name":"jeya","age":12}




if __name__=="__main__":
    method(*list,**dictvalues)
    boj = Person("manoj","muni")
    boj.display()
    


