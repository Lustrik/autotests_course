#def test_abs1():
#    assert abs(-42) == 42, "Should be absolute value of a number"

#def test_abs2():
#    assert abs(-42) == -42, "Should be absolute value of a number"

#if __name__ == "__main__": #служит для подтверждения того, что данный скрипт был запущен напрямую, а не вызван внутри другого файла в качестве модуля. Весь код написанный в теле этого условия будет выполнен только если пользователь запустил файл самостоятельно
#    test_abs1()
#    test_abs2()
#    print("All tests passed!")

import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
        
    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")
        
if __name__ == "__main__":
    unittest.main()
