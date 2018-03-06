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
    
    def setUp(self):
        '''
        Método executado antes de cada Test Case.
        O atributo phonebook ficará disponível 
        para todos os Test Cases.
        '''
        self.phonebook = Phonebook()
    
    def tearDown(self):
        '''
        Método executado após cada Test Case.
        '''
        pass
    
    def test_lookup_entry_by_name(self):
        self.phonebook.add("Bob", "12345")
        self.assertEqual("12345", self.phonebook.lookup("Bob"))
    
    def test_missing_entry_raises_KeyError(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    '''
    # Com o decorator abaixo, é possível configurar
    este Test Case para não ser executado durante
    o Test Runner. Isso é útil quanto ainda não
    finalizamos a implementação de um Test Case
    mas queremos executar o Test Runner e verificar
    se os outros testes estão passando.
    @unittest.skip("WIP")
    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())
    '''

    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())
    
    @unittest.skip("poor example")
    def test_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add("Bob", "12345")
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add("Mary", "012345")
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add("Sue", "12345") # identical to Bob
        self.assertFalse(self.phonebook.is_consistent())
        self.phonebook.add("Sue", "123") # prefix of Bob
        self.assertFalse(self.phonebook.is_consistent())
    
    def test_phonebook_with_normal_entried_is_consistent(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Mary", "012345")
        self.assertTrue(self.phonebook.is_consistent())
    
    def test_phonebook_with_duplicate_entried_is_inconsistent(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Mary", "12345")
        self.assertFalse(self.phonebook.is_consistent())
    
    def test_phonebook_with_numbers_that_prefix_one_another_is_inconsistent(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Mary", "123")
        self.assertFalse(self.phonebook.is_consistent())

    def test_phonebook_adds_names_and_numbers(self):
        self.phonebook.add("Sue", "12345")
        self.assertIn("Sue", self.phonebook.get_names())
        self.assertIn("12345", self.phonebook.get_numbers())
