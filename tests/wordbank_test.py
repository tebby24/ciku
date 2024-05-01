import os
import sys
from datetime import datetime, timedelta

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.tebbytools import WordBank

TEST_BANK_DB = "tests/data/bank.db"

if __name__ == "__main__":
    if os.path.exists(TEST_BANK_DB):
        os.remove(TEST_BANK_DB)

    yesterday_datetime = datetime.now() - timedelta(days=1)
    yesterday_date = yesterday_datetime.date()

    wb = WordBank(file_path=TEST_BANK_DB)
    wb.add_word("hello", tags=["greeting", "english"])
    wb.add_word("hola", tags=["greeting", "spanish"])
    wb.add_word("yesterday", date_time=yesterday_datetime)
    wb.add_word("hello", date_time=yesterday_datetime)

    print("all words: ", wb.get_all_words())
    print("today's words: ", wb.get_todays_words())
    print("words with tag greeting: ", wb.get_words_by_tag("greeting"))
    print("words added yesterday: ", wb.get_words_by_date(yesterday_date))
    print("all unique words: ", wb.get_all_unique_words())
    print("today's new words: ", wb.get_todays_new_words())
