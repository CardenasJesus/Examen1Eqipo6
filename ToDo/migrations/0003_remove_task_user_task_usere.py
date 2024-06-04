# Generated by Django 5.0.6 on 2024-06-04 05:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0002_rename_user_usere_task_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='User',
        ),
        migrations.AddField(
            model_name='task',
            name='UserE',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ToDo.usere'),
            preserve_default=False,
        ),
    ]
