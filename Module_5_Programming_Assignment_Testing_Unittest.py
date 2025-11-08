import unittest
from Module_5_PA_Inputs import remove_letters as rm

class TestInputs(unittest.TestCase):
    def test_remove_vowels(self):
        self.assertEqual(
            rm("Hello, World!", tuple("aeiouAEIOU")),
            "Hll, Wrld!",
            "Still includes vowels"
        )

    def test_case_sensitive(self):
        self.assertEqual(
            rm(
                "'Aha!', he said, 'apparently capital A is not the same as "
                "lowercase a.'",
                ("a",)
            ),
            "'Ah!', he sid, 'pprently cpitl A is not the sme s lowercse .'",
            "Didn't remove lowercase A"
        )

    def test_empty_remove(self):
        self.assertEqual(
            rm("Heehee, I'm invulnerable", ()),
            "Heehee, I'm invulnerable",
            "Not so invulnerable after all"
        )

    def test_empty_string(self):
        self.assertEqual(
            rm("", tuple("RandomText")),
            "",
            "How can you remove something from an already empty string?"
        )

    def test_passing_words(self):
        self.assertEqual(
            rm("This is a sentence which is made of words", ("is",)),
            "Th  a sentence which  made of words",
            "'is' was not removed"
        )