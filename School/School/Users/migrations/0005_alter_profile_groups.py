# Generated by Django 4.1.7 on 2023-03-29 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_alter_gradebookrecord_gradebook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='groups',
            field=models.ManyToManyField(related_name='students', to='Users.group'),
        ),
    ]
