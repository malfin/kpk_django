# Generated by Django 2.2 on 2020-10-31 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_web_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='static/img', verbose_name='Картинка'),
        ),
    ]