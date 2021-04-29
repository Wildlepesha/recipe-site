from django.db import models
from django.urls import reverse


# Create your models here.
class Recipie_Model(models.Model):
    title = models.CharField(verbose_name='Title', max_length=255, default='')
    ingred = models.CharField(verbose_name='Ingredients', max_length=255, default='')
    rec_body = models.TextField(verbose_name='Body', default='')
    slug = models.CharField(verbose_name='Slug', max_length=100, blank=True, unique=True)
    img = models.ImageField(verbose_name='Превью', default='main/313poeatlas.jpg', upload_to='main')
    yt_link = models.CharField(verbose_name='YT link', max_length=255, default='', blank=True)

    def save(self, *args, **kwargs):
        super().save()
        self.slug = "%s-%s" % (self.title, str(self.pk))
        self.ingred = self.ingred.lower()
        self.title = self.title.capitalize()
        if 'embed' not in self.yt_link:
            if len(str(self.yt_link)) >= 1:
                a = str(self.yt_link)
                a = a.split('/')
                b = '/'.join(a[:3])
                try:
                    c = a[3].split('=')
                    self.yt_link = b + '/embed/' + c[1]
                except IndexError:
                    b = '/'.join(a[:2])
                    d = 'www.youtube.com'
                    self.yt_link = b + d + '/embed/' + a[3]
        else:
            pass
        super().save()

    def __str__(self):
        return f'Рецепт {self.title}'

    def get_absolute_url(self):
        return reverse('Show', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class Image_Model(models.Model):
    image = models.ImageField(verbose_name='превью', default='main/313poeatlas.jpg', upload_to='main')