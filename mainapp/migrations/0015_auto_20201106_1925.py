# Generated by Django 2.2 on 2020-11-06 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_auto_20201106_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='img', verbose_name='Картинка'),
        ),
    ]