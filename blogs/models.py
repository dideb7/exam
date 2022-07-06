from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Статья')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фотография')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='articles', null=True, verbose_name='Категория')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='адрес')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Публикацию'
        verbose_name_plural = 'Публикации'
        ordering = ['time_create', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='адрес')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('categ', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'