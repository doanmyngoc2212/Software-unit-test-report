import unittest
from GuessNumberGame import GuessNumberGame


class MyTestCase(unittest.TestCase):
    game = GuessNumberGame()

    def test_getNewNumber(self):
        self.assertTrue(1000 <= self.game.getNewNumber() <= 9999)

    def test_checkValidGuess(self):
        # The Guessing input should be True
        self.assertTrue(self.game.checkValidGuess("1234"))
        self.assertTrue(self.game.checkValidGuess("1000"))
        self.assertTrue(self.game.checkValidGuess("9999"))
        self.assertTrue(self.game.checkValidGuess("5486"))
        # The Guessing input should be False: too short
        self.assertFalse(self.game.checkValidGuess(""))
        self.assertFalse(self.game.checkValidGuess("1"))
        self.assertFalse(self.game.checkValidGuess("12"))
        self.assertFalse(self.game.checkValidGuess("123"))
        # The Guessing input should be False: too long
        self.assertFalse(self.game.checkValidGuess("12345"))
        self.assertFalse(self.game.checkValidGuess("123456"))
        # The Guessing input should be False: not 4 digit number
        self.assertFalse(self.game.checkValidGuess("123a"))
        self.assertFalse(self.game.checkValidGuess("12ab"))
        self.assertFalse(self.game.checkValidGuess("1abc"))
        self.assertFalse(self.game.checkValidGuess("abcd"))

    def test_giveHint_4_O(self):
        self.assertEqual("OOOO", self.game.giveHint("2145", "2145"))
        self.assertEqual("OOOO", self.game.giveHint("1234", "1234"))

    def test_giveHint_3_O(self):
        self.assertEqual("OOO_", self.game.giveHint("1234", "1235"))
        self.assertEqual("OO_O", self.game.giveHint("1234", "1254"))
        self.assertEqual("O_OO", self.game.giveHint("1456", "1256"))
        self.assertEqual("_OOO", self.game.giveHint("1234", "9234"))

    def test_giveHint_2_O(self):
        self.assertEqual("OO__", self.game.giveHint("1234", "1256"))
        self.assertEqual("O_O_", self.game.giveHint("4567", "4268"))
        self.assertEqual("_OO_", self.game.giveHint("4238", "6235"))
        self.assertEqual("O__O", self.game.giveHint("1234", "1564"))
        self.assertEqual("_O_O", self.game.giveHint("7896", "1826"))
        self.assertEqual("__OO", self.game.giveHint("4567", "1267"))
        self.assertEqual("OO_X", self.game.giveHint("1272", "1234"))
        self.assertEqual("OOX_", self.game.giveHint("1234", "1253"))
        self.assertEqual("OXO_", self.game.giveHint("1435", "1234"))
        self.assertEqual("O_OX", self.game.giveHint("1932", "1234"))
        self.assertEqual("_OOX", self.game.giveHint("7231", "1234"))
        self.assertEqual("XOO_", self.game.giveHint("4237", "1234"))
        self.assertEqual("_OXO", self.game.giveHint("9214", "1234"))
        self.assertEqual("XO_O", self.game.giveHint("3284", "1234"))
        self.assertEqual("X_OO", self.game.giveHint("3934", "1234"))
        self.assertEqual("_XOO", self.game.giveHint("7134", "1234"))

    def test_giveHint_1_O(self):
        self.assertEqual("___O", self.game.giveHint("7894", "1234")) 
        self.assertEqual("__O_", self.game.giveHint("7538", "1234"))
        self.assertEqual("_O__", self.game.giveHint("7256", "1234"))
        self.assertEqual("O___", self.game.giveHint("1568", "1234"))
        self.assertEqual("__XO", self.game.giveHint("8914", "1234"))
        self.assertEqual("_X_O", self.game.giveHint("5374", "1234"))
        self.assertEqual("X__O", self.game.giveHint("2784", "1234"))
        self.assertEqual("__OX", self.game.giveHint("8531", "1234"))
        self.assertEqual("_XO_", self.game.giveHint("9137", "1234"))
        self.assertEqual("X_O_", self.game.giveHint("4839", "1234"))
        self.assertEqual("_O_X", self.game.giveHint("7261", "1234"))
        self.assertEqual("_OX_", self.game.giveHint("8246", "1234"))
        self.assertEqual("XO__", self.game.giveHint("3289", "1234"))
        self.assertEqual("O__X", self.game.giveHint("1562", "1234"))
        self.assertEqual("O_X_", self.game.giveHint("1749", "1234"))
        self.assertEqual("OX__", self.game.giveHint("1489", "1234"))

    def test_giveHint_1_X(self):
        self.assertEqual("___X", self.game.giveHint("7893", "1234"))
        self.assertEqual("__X_", self.game.giveHint("7829", "1234"))
        self.assertEqual("_X__", self.game.giveHint("7197", "1234"))
        self.assertEqual("X___", self.game.giveHint("4895", "1234"))

    def test_giveHint_allwrong(self):
        self.assertEqual("____", self.game.giveHint("7895", "1234"))


if __name__ == '__main__':
    unittest.main()
