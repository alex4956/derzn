# Generated by Django 3.2.4 on 2022-04-19 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drevo', '0008_remove_tz_is_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='tz',
            name='is_group',
            field=models.BooleanField(default=False, verbose_name='Вид является группой?'),
        ),
    ]
