# Generated by Django 2.0 on 2018-01-02 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home2', '0009_remove_house_freehold'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='called_on',
            field=models.DateField(blank=True, null=True),
        ),
    ]
