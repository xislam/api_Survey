import random

from django.contrib.auth import get_user_model
from django.db import models


class Survey(models.Model):
    name = models.CharField(max_length=50, verbose_name="name")
    date_start = models.DateField(auto_now_add=True, verbose_name="data start")
    date_end = models.DateField(verbose_name="date_end")
    description = models.TextField(verbose_name="description")


QUESTION_TYPES = (
    ('text', 'Ответ текстом'),
    ('one_option', 'Один вариант'),
    ('multiple_choice', 'Выбор нескольких вариантов'),
)


class Questions(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name="survey")
    text = models.TextField(verbose_name="text_questions")
    type_of_question = models.CharField(max_length=30, choices=QUESTION_TYPES,
                                        verbose_name='type of question')


class Choice(models.Model):
    name = models.TextField(verbose_name='Вариант ответа')
    question = models.ForeignKey(Questions, on_delete=models.CASCADE,
                                 related_name="choices")


class Answer(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                               null=True, blank=True)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE,
                                 related_name="answers")
    multiple_choice = models.ManyToManyField(Choice, blank=True)
    one_choice = models.ForeignKey(Choice, null=True, blank=True, on_delete=models.CASCADE,
                                   related_name="answers_one_choice")
    self_text = models.TextField(null=True, blank=True)

    def create_new_ref_number(self):
        not_unique = True
        while not_unique:
            unique_ref = random.randint(1000000000, 9999999999)
            if not Answer.objects.filter(Referrence_Number=unique_ref):
                not_unique = False
        return int(unique_ref)
