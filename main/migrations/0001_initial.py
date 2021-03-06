# Generated by Django 3.2 on 2021-04-28 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipie_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255, verbose_name='Title')),
                ('ingred', models.CharField(default='', max_length=255, verbose_name='Ingredients')),
                ('rec_body', models.TextField(default='', verbose_name='Body')),
                ('slug', models.CharField(blank=True, max_length=100, unique=True, verbose_name='Slug')),
                ('img', models.ImageField(default='main/313poeatlas.jpg', upload_to='', verbose_name='Превью')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
            },
        ),
    ]
