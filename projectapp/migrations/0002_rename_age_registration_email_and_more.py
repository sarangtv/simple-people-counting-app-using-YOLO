# Generated by Django 4.1.1 on 2022-12-31 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='age',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='name',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='phone',
        ),
    ]
