import unittest
from sum_numbers_per_sentence import (
    sum_numbers_per_sentence,
)


class TestSumNumbersPerSentence(unittest.TestCase):
    def test_single_sentence_with_no_number(self):
        para = "The weather is hot in San Francisco today."
        result = sum_numbers_per_sentence(para)
        self.assertEqual(result, [0])

    def test_single_sentence_with_single_positive_number(self):
        para = "The weather is 60 degrees in San Francisco today."
        result = sum_numbers_per_sentence(para)
        self.assertEqual(result, [60])

    def test_single_sentence_with_single_negative_number(self):
        para = "The weather is minus 60 degrees in San Francisco today."
        result = sum_numbers_per_sentence(para)
        self.assertEqual(result, [-60])

    def test_single_sentence_with_multiple_positive_numbers(self):
        para = "The weather is 60 degrees in San Francisco today and there's a 50% chance of precipitation and a 10% chance of rain."
        result = sum_numbers_per_sentence(para)
        self.assertEqual(result, [120])

    def test_single_sentence_with_multiple_negative_numbers(self):
        para = "The weather is -60 degrees in San Francisco today and there's a minus 50% chance of precipitation and a minus 10% chance of rain."
        result = sum_numbers_per_sentence(para)
        self.assertEqual(result, [-120])

    def test_single_sentence_with_single_positive_spelled_out_number(self):
        para = "The weather is seven degrees in San Francisco today."
        result = sum_numbers_per_sentence(para)
        self.assertEqual(result, [7])

    def test_single_sentence_with_single_negative_spelled_out_number(self):
        para = "The weather is - three degrees in San Francisco today."
        result = sum_numbers_per_sentence(para)
        self.assertEqual(result, [-3])

    def test_single_sentence_with_multiple_positive_spelled_out_numbers(self):
        para = "The weather is ten degrees in San Francisco today and there's a five % chance of precipitation and a two% chance of rain."
        result = sum_numbers_per_sentence(para)
        self.assertEqual(result, [17])

    def test_single_sentence_with_multiple_negative_spelled_out_numbers(self):
        para = "The weather is -ten degrees in San Francisco today and there's a minus five % chance of precipitation and a -two% chance of rain."
        result = sum_numbers_per_sentence(para)
        self.assertEqual(result, [-17])

    def test_multiple_sentences_with_mix_of_numbers(self):
        para = "The weather is 70 degrees in San Francisco today and there's a minus five % chance of precipitation. There is a -35% chance of rain and a one percent chance of snow."
        result = sum_numbers_per_sentence(para)
        self.assertEqual(result, [65, -34])

    def test_given_example_input(self):
        para = "The weather is 60 degrees in San Francisco today and there's a 50% chance of precipitation. The weather tomorrow is going to be colder than today. The weather in New York is 15 degrees today and ten degrees tomorrow. A temperature of minus 10 is too cold for me (I prefer 20 degrees and above)!"
        result = sum_numbers_per_sentence(para)
        self.assertEqual(result, [110, 0, 25, 10])


if __name__ == "__main__":
    unittest.main()
