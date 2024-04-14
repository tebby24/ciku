import json
import os


class LangBank:
    """
    A class for managing a word bank for language learning.
    """

    def __init__(self, file_path=None):
        """
        Initialize LangBank with an optional file path.
        If no file path is provided, a default one will be used.
        """
        if file_path is None:
            # Default file path: ~/langbank/bank.json
            self.file_path = os.path.expanduser("~/langbank/bank.json")
        else:
            self.file_path = file_path

    def set_file_path(self, file_path):
        """
        Set the file path for the word bank.
        """
        self.file_path = file_path

    def get_bank(self):
        """
        Get the contents of the word bank from the JSON file.
        Returns:
            The word bank (list).
        """
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Error: File '{self.file_path}' not found.")

    def write_bank(self, bank):
        """
        Write the contents of the word bank to the JSON file.
        Args:
            bank: The word bank (list) to write.
        """
        with open(self.file_path, "w") as f:
            json.dump(bank, f, indent=4)
