import unittest
from main import correct_text, uk_to_us

class TestCorrectText(unittest.TestCase):
    def test_spelling_errors(self):
        text = "She go to shcool every day."
        expected = "She goes to school every day."
        self.assertEqual(correct_text(text), expected)

    def test_grammatical_errors(self):
        text = "She don't like ice cream."
        expected = "She doesn't like ice cream."
        self.assertEqual(correct_text(text), expected)

    def test_punctuation_errors(self):
        text = "Weve tested HubSpot."
        expected = "We've tested HubSpot."
        self.assertEqual(correct_text(text), expected)

    def test_inconsistent_naming(self):
        text = "We use HubSpot and hubspot."
        expected = "We use HubSpot and HubSpot."
        self.assertEqual(correct_text(text), expected)

    def test_inconsistent_spelling(self):
        text = "Her favourite colour is blue."
        expected = "Her favorite color is blue."
        self.assertEqual(correct_text(text), expected)


class TestUkToUs(unittest.TestCase):
    def test_grey_to_gray(self):
        self.assertEqual(uk_to_us("grey"), "gray")
    
    def test_realised_to_realized(self):
        self.assertEqual(uk_to_us("realised"), "realized")
    
    def test_materialised_to_materialized(self):
        self.assertEqual(uk_to_us("materialised"), "materialized")
    
    def test_theatre_to_theater(self):
        self.assertEqual(uk_to_us("theatre"), "theater")
    
    def test_centre_to_center(self):
        self.assertEqual(uk_to_us("centre"), "center")
    
    def test_harbour_to_harbor(self):
        self.assertEqual(uk_to_us("harbour"), "harbor")
    
    def test_neighbours_to_neighbors(self):
        self.assertEqual(uk_to_us("neighbours"), "neighbors")
    
    def test_practised_to_practiced(self):
        self.assertEqual(uk_to_us("practised"), "practiced")
    
    def test_defence_to_defense(self):
        self.assertEqual(uk_to_us("defence"), "defense")
    
    def test_manoeuvres_to_maneuvers(self):
        self.assertEqual(uk_to_us("manoeuvres"), "maneuvers")
    
    def test_analysed_to_analyzed(self):
        self.assertEqual(uk_to_us("analysed"), "analyzed")
    
    def test_dialogue_to_dialog(self):
        self.assertEqual(uk_to_us("dialogue"), "dialog")
    
    def test_flavoured_to_flavored(self):
        self.assertEqual(uk_to_us("flavoured"), "flavored")
    
    def test_paediatrician_to_pediatrician(self):
        self.assertEqual(uk_to_us("paediatrician"), "pediatrician")
    
    def test_specialises_to_specializes(self):
        self.assertEqual(uk_to_us("specialises"), "specializes")
    
    def test_behavioural_to_behavioral(self):
        self.assertEqual(uk_to_us("behavioural"), "behavioral")
    
    def test_travelling_to_traveling(self):
        self.assertEqual(uk_to_us("travelling"), "traveling")
    
    def test_labour_to_labor(self):
        self.assertEqual(uk_to_us("labour"), "labor")
    
    def test_programme_to_program(self):
        self.assertEqual(uk_to_us("programme"), "program")
    
    def test_demoralised_to_demoralized(self):
        self.assertEqual(uk_to_us("demoralised"), "demoralized")
    
    def test_case_sensitivity(self):
        self.assertEqual(uk_to_us("colour"), "color")
    
    def test_multiple_words_in_sentence(self):
        self.assertEqual(
            uk_to_us("The colour of the theatre"),
            "The color of the theater"
        )
    
    def test_word_boundaries(self):
        """Test that words are only converted when they are complete words"""
        self.assertEqual(uk_to_us("colourful"), "colorful")
        self.assertEqual(uk_to_us("colouring"), "coloring")
    
    def test_preserves_punctuation(self):
        self.assertEqual(
            uk_to_us("The theatre, with its colour."),
            "The theater, with its color."
        )
    
