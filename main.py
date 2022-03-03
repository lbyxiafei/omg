from logger import Logger

class OMG():
    def __init__(self):
        self.logger = Logger()
    



if __name__ == '__main__':
    omg = OMG() 
    omg.logger.info("hello world")