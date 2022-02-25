# Generated by Django 3.0.2 on 2020-02-28 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flagstone', '0016_auto_20200227_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='date_returned',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='rental',
            name='rental_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='rental',
            name='rental_time',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='rental',
            name='return_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='rental',
            name='return_time',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='rental',
            name='time_returned',
            field=models.TimeField(blank=True),
        ),
    ]