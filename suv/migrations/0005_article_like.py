# Generated by Django 3.0.4 on 2020-05-14 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suv', '0004_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
