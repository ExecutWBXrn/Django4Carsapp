from django.db import models
from django.urls import reverse


class Cars(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, "DRAFT"
        PUBLISHED = 1, "PUBLISHED"
    title = models.CharField(max_length=255, verbose_name="Назва машини")
    year = models.IntegerField(verbose_name="Рік випуску")
    content = models.TextField(blank=True, verbose_name="Додаткова інформація")
    slug = models.SlugField(max_length=255,unique=True ,db_index=True)
    data_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата публікації")
    data_update = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")
    is_published = models.BooleanField(choices=map(lambda x: (bool(x[0]), x[1]), Status.choices) ,default=Status.PUBLISHED, verbose_name="Статус")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name="cat", verbose_name="Категорії")
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags')

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"\ntitle:{self.title}\ndescribe:{self.year}"

    def get_absolute_url(self):
        return reverse("carinfo", kwargs={"car_slug":self.slug})

    class Meta:
        verbose_name = "Автомобіль"
        verbose_name_plural = "Автомобілі"
        ordering = ['data_update']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name = "Категорії")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("dcat", kwargs={"cat_slug":self.slug})

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

class TagPost(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tag_slug_path", kwargs={"tag_slug":self.slug})