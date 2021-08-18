from django.db import models

class title(models.Model):
    content = models.TextFild()
    create_date = models.DateTimeField()

class diary(models.Model):
    link = models.ForeignKey(title, on_delete=models.CASCADE)
    content = models.TextFild()
    create_date = models.DateTimeField()