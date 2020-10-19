# Generated by Django 2.2 on 2020-10-19 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20201019_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='web',
            name='channel',
        ),
        migrations.AddField(
            model_name='web',
            name='cpu',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='web',
            name='ddos',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='web',
            name='location',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='web',
            name='traffic',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='dedic',
            name='channel',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='dedic',
            name='cpu',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='dedic',
            name='disk',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='dedic',
            name='ram',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='web',
            name='db',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='web',
            name='desk',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='web',
            name='nvme',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='web',
            name='sites',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.CreateModel(
            name='DDos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128)),
                ('desk', models.TextField(blank=True)),
                ('ports', models.CharField(blank=True, max_length=128)),
                ('protocol', models.CharField(blank=True, max_length=128)),
                ('ipv4', models.CharField(blank=True, max_length=128)),
                ('channel', models.CharField(blank=True, max_length=128)),
                ('is_active', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Catalog')),
            ],
        ),
    ]
