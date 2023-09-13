# Generated by Django 4.0.6 on 2023-09-11 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('bio', models.TextField(blank=True, max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]