from django.test import TestCase 
from catalog.models import Author , Book , Genre , BookInstance
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

# Test model Author
class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Author.objects.create(first_name ='big',last_name ='bob')
        
    def test_first_name_label(self):
        # Получение объекта для тестирования
        author = Author.objects.get(id = 1)
        # Получение метаданных поля для получения необходимых значений
        field_label = author._meta.get_field('first_name').verbose_name
        # Сравнить значение с ожидаемым результатом
        self.assertEquals(field_label ,'first name')


    def test_date_of_death_label(self):
        author = Author.objects.get(id = 1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label ,'date_of_death')


    def test_first_name_max_length(self):
        author = Author.objects.get(id = 1)
        max_lenght = author._meta.get_field('first_name').max_length
        self.assertEquals(max_lenght,100)


    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = '%s, %s' % (author.first_name, author.last_name)
        self.assertEquals(expected_object_name, str(author))

    # def test_get_absolute_url(self):
    #     author = Author.objects.get(id = 1)
    #     self.assertEquals(author.get_absolute_url(),'/catalog/author/1')


class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        author = Author.objects.create(first_name ='big',last_name ='bob')
        genre = Genre.objects.create(name = 'Science Fiction')
        book = Book.objects.create(author = author,summary = 'Test_Summary' , isbn = '1234432345323')
        book.genre.add(genre)

     #test_title_label направлен на проверку того, что у поля title в модели Book атрибут max_lenght = 100
    def test_title_label(self):
        book = Book.objects.get(id = 1)
        max_lenght = book._meta.get_field('title').max_length
        self.assertEquals(max_lenght, 200)

    #test_author_label направлен на проверку того, что у поля author в модели Book атрибут verbose_name = author
    def test_author_lable(self):
        book = Book.objects.get(id = 1)
        field_labe = book._meta.get_field('author').verbose_name
        self.assertEquals(field_labe , 'author')

    #test_summary_label направлен на проверку того, что у поля summary в модели Book атрибут summary = summary
    def test_summary_label(self):
        book = Book.objects.get(id = 1 )
        field_label = book._meta.get_field('summary').verbose_name
        self.assertEquals(field_label,'summary')

    #test_isbn_label направлен на проверку того, что у поля summary в модели Book атрибут isbn = ISBN
    def test_isbn_label(self):
        book = Book.objects.get(id = 1)
        field_label = book._meta.get_field('isbn').verbose_name
        self.assertEquals(field_label ,'ISBN')

    #test_isbn_label направлен на проверку того, что у поля summary в модели Book атрибут isbn = ISBN
    def test_genre_label(self):
        book = Book.objects.get(id = 1)
        field_lable = book._meta.get_field('genre').help_text
        self.assertEquals(field_lable ,'Select a genre for this book')
        

    #test_object_str_method направлен на проверку того, что тип __str__ в модели Book принимают title
    def test_object_str_method(self):
        book = Book.objects.get(id = 1)
        self.assertEqual(str(book),'')


    # def test_get_absolute_url(self):
    #     book = Book.objects.get(id = 1)
    #     expected_url = f'/catalog/book/{book.id}'
    #     self.assertEqual(book.get_absolute_url(), expected_url)


class GenreModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Genre.objects.create(name = 'Genre')


    def test_name_lable(self):
        model = Genre.objects.get(id = 1)
        field_lable = model._meta.get_field('name').max_length
        self.assertEqual(field_lable ,200)

    def test_url_method(self):
        genre = Genre.objects.get(id = 1)
        self.assertEqual(str(genre),'Genre')



# class YourTestCase(TestCase):
#     @classmethod
#     def setUpTest_data(cls):
#         print('setUpTestData: Run once to set up non-modified data for all class methods')
#         pass


#     def  setUp(self):
#         print("setUp: Run once for every test method to setup clean data.")
#         pass


#     def test_false_is_false(self):
#         print("Method: test_false_is_false.")
#         self.assertFalse(False)


#     def test_false_is_true(self):
#         print('Method: test_false_is_true.')
#         self.assertTrue(True)


#     def test_one_plus_one_equals_two(self):
#         print("Method: test_one_plus_one_equals_two.")
#         self.assertEqual(1 + 1 , 2)

        
