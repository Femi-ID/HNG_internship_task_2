# Generated by Django 4.0.6 on 2023-09-13 11:43

from django.db import migrations, models
import task2_crud_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('task2_crud_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=200, validators=[task2_crud_app.models.validate_string]),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=200, validators=[task2_crud_app.models.validate_string]),
        ),
    ]
