import unittest
import script

class TestGame(unittest.TestCase):
    def testCorrectGuess(self):
        print("\nRunning testCorrectGuess...")
        guess, answer = 5, 5
        result = script.runGuess(guess, answer)
        self.assertEqual(result, True)

    def testIncorrectGuess(self):
        print("\nRunning testIncorrectGuess...")
        guess, answer = 4, 6
        result = script.runGuess(guess, answer)
        self.assertFalse(result)

    def testOutOfRangeGuess(self):
        print("\nRunning testOutOfRangeGuess...")
        guess, answer = 11, 5
        result = script.runGuess(guess, answer)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()