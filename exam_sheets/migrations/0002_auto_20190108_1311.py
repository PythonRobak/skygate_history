# Generated by Django 2.1.5 on 2019-01-08 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_sheets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='completedexaminationsheet',
            old_name='is_checked',
            new_name='checked',
        ),
        migrations.AddField(
            model_name='completedexaminationsheet',
            name='archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examsheet',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]