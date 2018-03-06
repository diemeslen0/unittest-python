'''
- Given a list of names and phone numbers,
make a Phonebook that allows you to look up
numbers by name.

- Determine if a given Phonebook is consistent.

- In a consistend phone list no number is
a prefix of another.

Examples:

Bob 91125426
Alice 97 625 992
Emergency 911

Bob and Emergency are inconsistent.
'''
import unittest

from phonebook import Phonebook

class PhonebookTest(unittest.TestCase):

    def test_create_phonebook(self):
        pronebook = Phonebook()
    
    def test_lookup_entry_by_name(self):
        phonebook = Phonebook()
        phonebook.add("Bob", "12345")
        self.assertEqual("12345", phonebook.lookup("Bob"))
    
    def test_missing_entry_raises_KeyError(self):
        phonebook = Phonebook()
        with self.assertRaises(KeyError):
            phonebook.lookup("missing")

