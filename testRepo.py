class testRepo:
    
    def __init__ (self):
        self.tests = []
    
    def addTest(self, test_name):
        self.tests.append(test_name)
        
        return self