# Generated by Django 3.0.4 on 2020-05-15 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suv', '0007_remove_transaction_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
