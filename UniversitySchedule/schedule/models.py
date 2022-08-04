from django.db import models


class Teacher(models.Model):
    """"
    Модель преподователя. Содержит фамилию и имя преподователя. Имеется контакная информация
    """
    teacher_name = models.CharField('Имя', max_length=70)
    teacher_lastname = models.CharField('Фамилия', max_length=70)
    teacher_patronymic = models.CharField('Отчество', max_length=70, null=True)
    email = models.EmailField('Электронная почта')
    eeistu_url = models.CharField('Ссылка на профиль', max_length=250)

    def __str__(self):
        return f'{self.teacher_lastname} {self.teacher_name}'

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Lesson(models.Model):
    """"
    Модель пары
    """
    lesson_name = models.CharField('Пара', max_length=50)
    lesson_type = models.CharField('Тип пары', max_length=20)
    lesson_auditory = models.CharField('Кабинет', max_length=15)
    start_time = models.TimeField('Время начала пары')
    end_time = models.TimeField('Время конца пары')
    lesson_teacher = models.ManyToManyField(Teacher, verbose_name='Преподаватель', related_name='lessons_teachers')

    def __str__(self):
        return f'{self.lesson_type} {self.lesson_name}'

    class Meta:
        verbose_name = 'Пара'
        verbose_name_plural = 'Пары'


class Day(models.Model):
    """"
    Модель дня недели.
    """
    day = models.CharField('День недели', max_length=15)
    above_line = models.BooleanField('Неделя над чертой')
    lessons = models.ManyToManyField(Lesson, verbose_name='Пара', related_name='day_lesson')

    def __str__(self):
        return f'{self.day}'

    class Meta:
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'
