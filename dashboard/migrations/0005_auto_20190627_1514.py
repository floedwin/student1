# Generated by Django 2.2.1 on 2019-06-27 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20190627_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='student_name',
            field=models.CharField(default='', max_length=200, verbose_name='student_name'),
        ),
    ]