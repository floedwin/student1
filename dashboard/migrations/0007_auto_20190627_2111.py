# Generated by Django 2.2.1 on 2019-06-27 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20190627_2111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='study_material',
            old_name='subjecte',
            new_name='subject',
        ),
    ]
