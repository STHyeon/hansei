# Generated by Django 2.2.3 on 2019-07-25 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_store_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='price',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
