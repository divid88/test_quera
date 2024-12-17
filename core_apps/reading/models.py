from django.db import models
from core_apps.common.models import BaseModel


class Subject(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'
    
    


class SubSubject(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, 
                                related_name="subs")
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'


class Concept(models.Model):
    sub = models.ForeignKey(SubSubject, on_delete=models.CASCADE, 
                            related_name="concepts")
    describe = models.TextField(max_length=1000, null=None, blank=None)
    code = models.TextField(max_length=1000, null=None, blank=None)

    def __str__(self):
        return f'{self.sub.title} '
