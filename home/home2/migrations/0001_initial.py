# Generated by Django 2.0 on 2017-12-22 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('n_bedrooms', models.PositiveSmallIntegerField()),
                ('reception', models.BooleanField()),
                ('distance_to_station_km', models.FloatField()),
                ('freehold', models.BooleanField()),
                ('garden', models.BooleanField()),
                ('carpet', models.BooleanField()),
                ('ng_valuation', models.FloatField()),
                ('ne_valuation', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='HousePrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('price', models.IntegerField()),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home2.House')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='houseprice',
            unique_together={('house', 'date')},
        ),
    ]
