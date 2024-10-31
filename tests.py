import unittest
from correct import correct_text

class TestCorrectText(unittest.TestCase):
    def test_spelling_errors(self):
        text = "She go to shcool every day."
        expected = "She goes to school every day."
        output, errors = correct_text(text)
        print(output)
        print(errors)
        self.assertEqual(output, expected)

    def test_grammatical_errors(self):
        text = "She don't like ice cream."
        expected = "She doesn't like ice cream."
        output, _ = correct_text(text)
        self.assertEqual(output, expected)

    def test_punctuation_errors(self):
        text = "Weve tested HubSpot."
        expected = "We've tested HubSpot."
        output, _ = correct_text(text)
        self.assertEqual(output, expected)

    def test_inconsistent_naming(self):
        text = "We use HubSpot and hubspot."
        expected = "We use HubSpot and HubSpot."
        output, _ = correct_text(text)
        self.assertEqual(output, expected)

    def test_inconsistent_spelling(self):
        text = "Her favourite colour is blue."
        expected = "Her favorite color is blue."
        
        output, errors = correct_text(text)
        print(output)
        print(errors)
        self.assertEqual(output, expected)
