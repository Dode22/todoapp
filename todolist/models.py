from django.db import models

# Create your models here.
# class Todolist(models.Model):
#     text = models.CharField(max_lenght=45)
#     completed = models.BooleanField(default=False)

#     # create a function that will return the todolist

#     def __str__(self):
#         return self.text
from django.utils import timezone

class Category(models.Model): # The category table name that inherits models.Model
    name = models.CharField(max_length=100) # Like a varchar

    class Meta:
        verbose_name = ("Category") 
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name   # name to be shown when called

class Todolist(models.Model): #Todolist able name that inherits models.Model
    title = models.CharField(max_length=250)    # a varchar
    content = models.TextField(blank=True)      # a text field
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))     # a date
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))    # a date
    category = models.ForeignKey(Category, on_delete=models.CASCADE)   # a foriegnkey

    class Meta:
        ordering = ["-created"]  # ordering by the created field

    def __str__(self):
        return self.title #name to be shown when called
