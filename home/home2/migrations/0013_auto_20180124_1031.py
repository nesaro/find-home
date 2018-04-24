# Generated by Django 2.0.1 on 2018-01-24 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home2', '0012_auto_20180107_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='land_registry_price_sold',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='postcode',
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='house',
            name='ne_valuation',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='ng_valuation',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]