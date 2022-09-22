import unittest
from match_parenthesis import (
    match_parens_per_sentence,
)


class TestMatchParenthesis(unittest.TestCase):
    def test_single_sentence_with_no_unmatched_paren(self):
        para = "(I prefer 20 degrees and above)!"
        result = match_parens_per_sentence(para)
        self.assertEqual(result, para)

    def test_single_sentence_with_single_unmatched_paren(self):
        para = "(I prefer 20 degrees and above!"
        result = match_parens_per_sentence(para)
        self.assertEqual(result, "(I prefer 20 degrees and above)!")

    def test_single_sentence_with_multiple_unmatched_paren(self):
        para = "(I prefer (20 degrees (and) above!"
        result = match_parens_per_sentence(para)
        self.assertEqual(result, "(I prefer (20 degrees (and) above))!")

    def test_multiple_sentences_with_single_unmatched_paren(self):
        para = "(I prefer 20 degrees and above)! (I like the beach and the sun."
        result = match_parens_per_sentence(para)
        self.assertEqual(
            result, "(I prefer 20 degrees and above)! (I like the beach and the sun)."
        )

    def test_multiple_sentences_with_multiple_unmatched_paren(self):
        para = "(I prefer (20 degrees and above! (I like the beach and (the sun)."
        result = match_parens_per_sentence(para)
        self.assertEqual(
            result,
            "(I prefer (20 degrees and above))! (I like the beach and (the sun)).",
        )


if __name__ == "__main__":
    unittest.main()
