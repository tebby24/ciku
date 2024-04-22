import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.tebbytools import WordBank

TEST_BANK_JSON = "tests/data/bank.json"

if __name__ == "__main__":
    with open(TEST_BANK_JSON, "w") as f:
        f.write("[]")

    wb = WordBank(file_path=TEST_BANK_JSON)
    wb.add_word("hello", tags=["greeting", "english"])
    wb.add_word("hola", tags=["greeting", "spanish"])

    print("all words: ", wb.get_all_words())
    print("today's words", wb.get_todays_words())
