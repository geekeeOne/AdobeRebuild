# Generated by Django 3.0.2 on 2020-03-03 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flagstone', '0023_auto_20200303_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='praasa_march2020',
            name='departure_airport',
            field=models.CharField(blank=True, default='Tucson International', max_length=29),
        ),
    ]
