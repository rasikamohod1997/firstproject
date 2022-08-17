from django.test import TestCase
from .models import Author, Book
# Create your tests here.

class BaseModelTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super(BaseModelTestCase, cls).setUpClass()
        cls.author = Author(name = "Aditi")
        cls.author.save()
        cls.first_book = Book(author=cls.author, name = "short_history_of_time")
        cls.first_book.save()
        cls.second_book = Book(author=cls.author, name="long_history_of_time")
        cls.second_book.save()

class AuthorModelTestCase(BaseModelTestCase):
    def test_created_properly(self):
        self.assertEqual(self.author.name, "Aditi")
        self.assertEqual(True, self.first_book in self.author.book_set.all())

class BookModelTestCase(BaseModelTestCase):
    def test_created_properly(self):
        self.assertEqual(1, len(Book.objects.filter(name__startswith='long')))