class Test_match:
    def test_add_002(self):
        a = 10
        b = 20
        sum = a + b
        print("the sum is :",sum)
        if sum == 30:
            assert True
        else:
            assert False
