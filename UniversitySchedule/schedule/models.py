from django.db import models


class Teacher(models.Model):
    """"
    Модель преподователя. Содержит фамилию и имя преподователя. Имеется контакная информация
    """
    teacher_name = models.CharField('Имя', max_length=255)
    teacher_lastname = models.CharField('Фамилия', max_length=255)
    email = models.EmailField('Электронная почта', max_length=254)
    eeistu_url = models.SlugField(max_length=250)

    def __str__(self):
        return f'{self.teacher_lastname} {self.teacher_name}'

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'



class Lesson(models.Model):
    """"
    Модель пары
    """
    lesson_name = models.CharField('Пара', max_length=255)
    lesson_type = models.CharField('Тип пары', max_length=255)
    lesson_auditory = models.CharField('Кабинет', max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f'{self.lesson_type} {self.lesson_name}'

    class Meta:
        verbose_name = 'Пара'
        verbose_name_plural = 'Пары'