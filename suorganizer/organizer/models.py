from django.db import models


# Model Field Reference
# https://docs.djangoproject.com/en/1.8/ref/models/fields


class Tag(models.Model):
    name = models.CharField(
        max_length=31, unique=True)
    slug = models.SlugField(
        max_length=31,
        unique=True,
        help_text='A label for URL config.')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Startup(models.Model):
    name = models.CharField(
        max_length=31, db_index=True)
    slug = models.SlugField(
        max_length=31,
        unique=True,
        help_text='A label for URL config. ')
    description = models.TextField()
    founded_date = models.DateField(
        'date founded')
    contact = models.EmailField()
    website = models.URLField(max_length=255)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ['name']
        get_latest_by = 'founded_date'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(
        max_length=63,
        help_text='A label for URL config',
        unique_for_month='pub_date')
    text = models.TextField()
    pub_date = models.DateField(
        'date published',
        auto_now_add=True)
    tags = models.ManyToManyField(
        Tag, related_name='blog_posts')
    startups = models.ManyToManyField(
        Startup, related_name='blog_post')

    def __str__(self):
        return "{} on {}".format(
            self.title,
            self.pub_date.strftime('%Y-%m-%d'))


class NewsLink(models.Model):
    title = models.CharField(max_length=63)
    pub_date = models.DateField('date published')
    link = models.URLField(max_length=255)
    startup = models.ForeignKey(Startup)

    def __str__(self):
        return "{}:{}".format(
            self.startup, self.title)
