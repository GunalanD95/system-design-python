'''
SINGLETON:
GOAL :
 - A class should has only one instance of its object created not more than that
'''
import threading

class Singleton:
    __instance = None 
    __lock = threading.Lock()
    
    def __new__(cls,*args,**kwargs):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super(Singleton,cls).__new__(cls)
                    cls.__instance.__initialized = False
        return cls.__instance        
    
    
    def __init__(self,db_name):
        if not self.__initialized:
            self.db_name = db_name
            self.__initialized = True
        else:
            print("already object is  initialized so returning...")
    
ss = Singleton('Redis')
s2 = Singleton('Postgres')
print("ss",id(ss),ss.db_name)
print("s2",id(s2),s2.db_name)
