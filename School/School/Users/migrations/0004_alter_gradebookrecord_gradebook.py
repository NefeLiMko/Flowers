# Generated by Django 4.1.7 on 2023-03-29 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_alter_gradebookrecord_pupil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradebookrecord',
            name='gradebook',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='gradebooks', to='Users.gradebook'),
        ),
    ]