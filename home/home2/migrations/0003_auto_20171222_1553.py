# Generated by Django 2.0 on 2017-12-22 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home2', '0002_auto_20171222_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='ne_valuation',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='ng_valuation',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
