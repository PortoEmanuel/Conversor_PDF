# Generated by Django 5.1 on 2024-08-29 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arquivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.FileField(upload_to='uploads/')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='pdfs/')),
            ],
        ),
    ]
