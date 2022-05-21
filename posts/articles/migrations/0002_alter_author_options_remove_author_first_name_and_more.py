# Generated by Django 4.0.4 on 2022-05-20 09:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ('name',), 'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.RemoveField(
            model_name='author',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='patronymic',
        ),
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='Фамилия Имя Отчество полностью'),
            preserve_default=False,
        ),
    ]
