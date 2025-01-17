# Generated by Django 3.2.4 on 2022-12-06 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drevo', '0032_merge_20221130_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='admin',
            field=models.CharField(default='', max_length=512, verbose_name='Админ'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='comment',
            field=models.CharField(default='', max_length=512, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='contribution',
            field=models.IntegerField(default=0, verbose_name='Вклад в проект'),
        ),
        migrations.AlterField(
            model_name='glossaryterm',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Термин'),
        ),
        migrations.AlterField(
            model_name='tr',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='znanie',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Тема'),
        ),
    ]
