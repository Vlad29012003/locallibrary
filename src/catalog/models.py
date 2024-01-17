from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length = 200, help_text ='Enter a book genre (e.g. Science Fiction, French Poetry etc.)')

#  предназначен для предоставления строкового представления объекта.
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
    


# Прмер модельки созлает обьект но не добавляет в базу данных но используются для других частях приложения 
# class SimpleModel:
#     def __init__(self, name):
#         self.name = name
