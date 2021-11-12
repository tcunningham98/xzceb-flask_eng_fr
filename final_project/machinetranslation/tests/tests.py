import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslateEnToFr(unittest.TestCase):
    """
    Class to test the function englishToFrench
    """
    def test1(self):
        """
        Function to test the function englishToFrench
        """
        self.assertIsNone(englishToFrench(None))
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        self.assertNotEqual(englishToFrench("Bonjour"), "Hello")

class TestTranslateFrToEn(unittest.TestCase):
    """
    Class to test the function frenchToEnglish
    """
    def test2(self):
        """
        Function to test the function frenchToEnglish
        """
        self.assertIsNone(frenchToEnglish(None))
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        self.assertNotEqual(frenchToEnglish("Hello"), "Bonjour")

unittest.main()