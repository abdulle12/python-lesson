class computer:

    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram


    def config(self):
        print('The configuration of object: ',self.cpu,self.ram)
com1=computer('b2', 8)
com2=computer('i5', 16)
com1.ram=20
com1.cpu="2gp"
com1.config()
com2.config()

