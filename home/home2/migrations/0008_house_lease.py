# Generated by Django 2.0 on 2017-12-27 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home2', '0007_auto_20171223_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='lease',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
