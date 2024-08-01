import random
import unittest
import script

# class TestMain(unittest.TestCase):
#     def setUp(self):
#         print("About to run a function...")
#         print("this is useful for when you need to run something every time for a test")
#     def test_do_stuff_1(self):
#         testParam = 10
#         result = script.do_stuff(testParam)
#         self.assertEqual(result, 15)
#
#     def test_do_stuff_2(self): # trying to improve my function by breaking it
#         testParam = 'happy'
#         result = script.do_stuff(testParam)
#         self.assertIsInstance(result, ValueError) #becuase you are returning an error, you need the result to be an instance of valueError
#
#     def test_do_stuff_3(self):
#         testParam = None
#         result = script.do_stuff(testParam)
#         self.assertTrue(result, "Please enter number")
#
#     def test_do_stuff_4(self):
#         testParam = ''
#         result = script.do_stuff(testParam)
#         self.assertTrue(result, "Please enter number")
#
#     def tearDown(self):
#         print("usually do this to clean up some variables or set up other variables")
#         print("you won't use this super often. you\'ll use it when you work more with a database")

class TestGame(unittest.TestCase):
    def testCorrectNumber(self):
        print('Correct Number Test')
        script.guessNumber(4, 4)
        self.assertTrue('You are a genius!')

    def testIncorrectNumber(self):
        print('Incorrect Number Test')
        script.guessNumber(5, 4)
        self.assertTrue("Enter a Guess Here | Number 1-10 -> ")

    def testIntegerAboveRange(self):
        testParam = 11
        result = script.guessNumber(testParam)
        self.assertEqual(result, "Hey bozo, I said 1~10")

    def testIntegerBelowRange(self):
        testParam = -1
        result = script.guessNumber(testParam)
        self.assertEqual(result, "Hey bozo, I said 1~10")
if __name__ == '__main__':
    unittest.main()