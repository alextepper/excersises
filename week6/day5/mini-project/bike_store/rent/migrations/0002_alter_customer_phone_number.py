# Generated by Django 4.2.4 on 2023-08-19 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=30),
        ),
    ]