# Generated by Django 3.0.4 on 2020-03-06 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=1000)),
                ('date', models.TextField(max_length=1000)),
                ('content', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=1000)),
                ('username', models.TextField(max_length=1000)),
                ('year', models.TextField(max_length=1000)),
                ('city', models.TextField(max_length=1000)),
                ('car_image', models.ImageField(blank=True, null=True, upload_to="{% static 'img' %}")),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_type', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=1000)),
                ('username', models.TextField(max_length=1000)),
                ('year', models.TextField(max_length=1000)),
                ('city', models.TextField(max_length=1000)),
                ('date', models.TextField(max_length=1000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suv.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=1000)),
                ('message', models.TextField(max_length=1000)),
                ('created_date', models.TextField(max_length=1000)),
                ('rating', models.TextField(max_length=1000)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suv.Car')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suv.Category'),
        ),
    ]
