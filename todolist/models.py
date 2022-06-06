from django.db import models


#Class that inherits from models.Model and creates fiedls 
class Todo(models.Model):
    title = models.CharField(max_length=350)
    complete = models.BooleanField(default=False)
    #Create a string method to display accurate description.
    def __str__(self):
        return self.title
