# Generated by Django 2.2.13 on 2020-06-30 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv_entry',
            name='title',
            field=models.TextField(default=''),
        ),
    ]
