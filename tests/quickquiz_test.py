import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.tebbytools import QuickQuiz

if __name__ == "__main__":
    qq = QuickQuiz()
    qq.start()
