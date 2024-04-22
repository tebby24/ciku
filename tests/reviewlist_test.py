import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.tebbytools import ReviewList

TEST_rl_TXT = "tests/data/rl.txt"

if __name__ == "__main__":
    rl = ReviewList(file_path=TEST_rl_TXT, size=3)
    rl.add_word("hello")
    rl.add_word("hola")
    rl.add_word("bonjour")

    print("review list: ", rl.get_list())

    rl.add_word("ciao")

    print("review list: ", rl.get_list())
