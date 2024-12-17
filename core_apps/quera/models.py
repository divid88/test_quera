
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class LevelUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='levels')
    level = models.PositiveSmallIntegerField()
    code_program = models.FileField()
    success = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class SubjectTestProgram(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self) -> str:
        return f'{self.title}'

class ProgramTest(models.Model):
    subjects = models.ForeignKey(SubjectTestProgram, on_delete=models.CASCADE,
                                 related_name='tests', null=True, blank=True)
    level = models.PositiveSmallIntegerField()
    test_result = models.TextField(null=True, blank=True)
    test_code = models.FileField(upload_to='test')

    inputs = models.TextField(max_length=1000, null=True, blank=True)
    outputs = models.TextField(max_length=1000, null=True, blank=True)
    example_code = models.TextField(max_length=1000, null=True, blank=True)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.description}'


# class Tutorial(models.Model):
#     upc = models.CharField(max_length=5, unique=True)
#     title = models.CharField(max_length=250)
#     body = models.TextField()

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title


# class QuestionTutorial(models.Model):
#     tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE,
#                                  related_name='questions')
#     question = models.TextField()
#     number_one = models.CharField(max_length=250)
#     number_two = models.CharField(max_length=250)
#     number_three = models.CharField(max_length=250)
#     number_four = models.CharField(max_length=250)
#     answer = models.PositiveSmallIntegerField()

#     def __str__(self):
#         return f'{self.question} >>> {self.answer}'

