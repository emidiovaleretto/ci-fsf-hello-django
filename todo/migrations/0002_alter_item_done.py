# Generated by Django 3.2 on 2022-02-21 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
