import re
from nltk import tokenize

number_mappings = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "ten": "10",
}


def convert_number(num_match: str):
    number = int(number_mappings.get(num_match[2], num_match[2]))
    minus_val = num_match[0].strip()
    if len(minus_val) == 0:
        minus_val = num_match[1].strip()

    if minus_val == "minus" or minus_val == "-":
        number = -number

    return number


def extract_and_sum_numbers(sentence: str):
    extracted_numbers = re.findall(r"(\bminus )?(- ?)?(\d+)\b", sentence)
    extracted_spelled_numbers = re.findall(
        r"(\bminus )?(- ?)?\b(one|two|three|four|five|six|seven|eight|nine|ten)\b",
        sentence,
    )

    numbers = list(map(lambda num: convert_number(num), extracted_numbers))
    numbers += list(map(lambda num: convert_number(num), extracted_spelled_numbers))

    return sum(numbers)


def sum_numbers_per_sentence(s: str):
    sentences = tokenize.sent_tokenize(s)

    return list(
        map(lambda sentence: extract_and_sum_numbers(sentence.lower()), sentences)
    )


if __name__ == "__main__":
    inp = "The weather is 60 degrees in San Francisco today and there's a 50% chance of precipitation. The weather tomorrow is going to be colder than today. The weather in New York is 15 degrees today and ten degrees tomorrow. A temperature of minus 10 is too cold for me (I prefer 20 degrees and above)!"
    sentence_sums = sum_numbers_per_sentence(inp)

    for i, sentence_sum in enumerate(sentence_sums):
        print(f"Sentence {i+1}: {sentence_sum}")
