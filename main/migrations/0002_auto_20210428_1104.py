# Generated by Django 3.2 on 2021-04-28 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='main/313poeatlas.jpg', upload_to='main', verbose_name='превью')),
            ],
        ),
        migrations.AlterField(
            model_name='recipie_model',
            name='img',
            field=models.ImageField(default='main/313poeatlas.jpg', upload_to='main', verbose_name='Превью'),
        ),
    ]
