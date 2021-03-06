# Generated by Django 3.1.3 on 2021-06-22 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photoupload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='nameAscendency',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='photo',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='photoupload.category'),
        ),
    ]
