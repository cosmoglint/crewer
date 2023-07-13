# Generated by Django 4.2.3 on 2023-07-13 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskManager', '0005_remove_task_skill_task_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='proficiency',
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
