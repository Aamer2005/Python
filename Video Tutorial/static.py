class Demo:
    count = 0

    def __init__(self):
        Demo.count+=1
        self.serial_no = Demo.count

    #@static method
    def info():
        print("Demo Class : ")

Demo.info()