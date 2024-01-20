from django.db import models
from django.urls import reverse


class Cars(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, "DRAFT"
        PUBLISHED = 1, "PUBLISHED"
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    content = models.TextField(blank=True)
    slug = models.SlugField(max_length=255,unique=True ,db_index=True)
    data_create = models.DateTimeField(auto_now_add=True)
    data_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices ,default=Status.PUBLISHED)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags')

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"\ntitle:{self.title}\ndescribe:{self.year}"

    def get_absolute_url(self):
        return reverse("carinfo", kwargs={"car_slug":self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("dcat", kwargs={"cat_slug":self.slug})

class TagPost(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tag_slug_path", kwargs={"tag_slug":self.slug})