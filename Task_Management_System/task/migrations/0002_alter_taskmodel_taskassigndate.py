# Generated by Django 5.0.6 on 2025-03-20 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='taskAssignDate',
            field=models.DateField(),
        ),
    ]
