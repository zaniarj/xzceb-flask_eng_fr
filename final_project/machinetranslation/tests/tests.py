from machinetranslation.translator import english_to_french, french_to_english
import unittest

class TestTranslate(unittest.TestCase):

    def test_e_to_f(self):
        '''test for english_to_french function '''
        self.assertEqual(english_to_french("hello"),"bonjour")
    
    def test_f_to_e(self):
        '''test for french_to_english function '''
        self.assertEqual(french_to_english("bonjour"),"hello")

unittest.main()