# Generated by Django 3.0.2 on 2020-03-03 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flagstone', '0022_auto_20200303_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='praasa_march2020',
            name='arrival_airport',
            field=models.CharField(blank=True, default='Tucson International', max_length=9),
        ),
        migrations.AlterField(
            model_name='praasa_march2020',
            name='departure_airport',
            field=models.CharField(blank=True, default='Tucson International', max_length=9),
        ),
    ]