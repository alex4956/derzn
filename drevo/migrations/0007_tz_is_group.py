# Generated by Django 3.2.4 on 2022-04-16 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drevo', '0006_merge_0005_auto_20220401_2156_0005_visits'),
    ]

    operations = [
        migrations.AddField(
            model_name='tz',
            name='is_group',
            field=models.BooleanField(default=False, verbose_name='Вид является группой?'),
        ),
    ]
