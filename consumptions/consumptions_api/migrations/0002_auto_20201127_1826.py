# Generated by Django 3.1.3 on 2020-11-27 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumptions_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumptions',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
