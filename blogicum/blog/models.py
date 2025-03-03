from django.db import models
from django.contrib.auth import get_user_model

from .constants import MAXLINELENGTH


User = get_user_model()

#нужно переоформить в forms.model? или в CBV
#создать класс Profile со связью с атрибутом posts.author
#и связать с user
class Category(models.Model):
    title = models.CharField(
        max_length=MAXLINELENGTH,
        verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    is_published = models.BooleanField(
        verbose_name="Опубликовано",
        help_text="Снимите галочку, чтобы скрыть публикацию.",
        default=True,
    )
    created_at = models.DateTimeField(
        verbose_name="Добавлено",
        auto_now_add=True)
    slug = models.SlugField(
        verbose_name="Идентификатор",
        help_text='''Идентификатор страницы для URL; '''
        '''разрешены символы латиницы, цифры, дефис и подчёркивание.''',
        unique=True,
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class Location(models.Model):
    name = models.CharField(
        max_length=MAXLINELENGTH,
        verbose_name="Название места")
    is_published = models.BooleanField(
        verbose_name="Опубликовано",
        help_text="Снимите галочку, чтобы скрыть публикацию.",
        default=True,
    )
    created_at = models.DateTimeField(
        verbose_name="Добавлено",
        auto_now_add=True)

    class Meta:
        verbose_name = "местоположение"
        verbose_name_plural = "Местоположения"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(
        max_length=MAXLINELENGTH,
        verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    is_published = models.BooleanField(
        verbose_name="Опубликовано",
        help_text="Снимите галочку, чтобы скрыть публикацию.",
        default=True,
    )
    created_at = models.DateTimeField(
        verbose_name="Добавлено",
        auto_now_add=True)

    pub_date = models.DateTimeField(
        verbose_name="Дата и время публикации",
        help_text='''Если установить дату и время в будущем'''
        ''' — можно делать отложенные публикации.''',
    )
    author = models.ForeignKey(
        User,
        verbose_name="Автор публикации",
        on_delete=models.CASCADE,
        related_name='posts'
    )
    location = models.ForeignKey(
        Location,
        verbose_name="Местоположение",
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts'
    )
    category = models.ForeignKey(
        Category,
        verbose_name="Категория",
        on_delete=models.CASCADE,
        null=True,
        related_name='posts'
    )

    class Meta:
        verbose_name = "публикация"
        verbose_name_plural = "Публикации"

    def __str__(self):
        return self.title
