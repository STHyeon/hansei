# Generated by Django 2.2.3 on 2019-07-25 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_auto_20190726_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='day',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='store',
            name='park',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]