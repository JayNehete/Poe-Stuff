# Generated by Django 3.1.3 on 2021-06-22 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoupload', '0004_category_gemname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='activePassive',
        ),
        migrations.RemoveField(
            model_name='category',
            name='gemName',
        ),
        migrations.AddField(
            model_name='photo',
            name='activePassive',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='photo',
            name='gemName',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]