class TestClass:
    x = "変数1"
    
    def test_method1(self):
        print(self.x)
        
    def test_method2(self, arg1):
        print("引数:" + arg1)
        
testClass = TestClass()
testClass.test_method1()
testClass.test_method2("引数Test")
