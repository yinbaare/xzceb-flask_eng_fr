from translator import english_to_french, french_to_english
import unittest


class TestTranslator(unittest.TestCase):

    def test_english_to_french(self):
        self.assertEqual(english_to_french("Hello, world"), "Bonjour, monde")
        self.assertNotEqual(english_to_french("IBM Watson rocks"), "Bonjour, monde")
    


    def test_french_to_english(self):
        self.assertEqual(french_to_english("Bonjour, monde"),"Hello, world")
        self.assertNotEqual(french_to_english("Bonjour, monde"), "IBM Watson rocks")



if __name__ == "__main__":
    unittest.main()