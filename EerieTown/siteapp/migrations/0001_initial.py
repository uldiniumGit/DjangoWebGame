# Generated by Django 4.2.4 on 2023-08-11 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatchNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.FloatField(max_length=16, unique=True)),
                ('description', models.TextField(blank=True)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
