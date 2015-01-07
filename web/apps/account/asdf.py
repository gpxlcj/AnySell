class Father(object):
    
    first_name = str()
    last_name = str()
    def __init__(self):
        
        self.first_name = 'James'
        self.last_name = 'Grant'

    def eat(self):
        
        print '%s%s is eating' %(self.first_name, self.last_name)

class Son(Father):
  
    age = int()

    def __init__(self, age):
        Father.__init__()
        self.age = age

    def play(self):
        print 'playing'

    def eat(self):
        
        print 'eating'
