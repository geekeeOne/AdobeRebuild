# Generated by Django 3.0.2 on 2020-03-03 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flagstone', '0019_auto_20200302_1304'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='praasa_march2020',
            options={'ordering': ['arrival_time']},
        ),
        migrations.AlterModelOptions(
            name='rental',
            options={'ordering': ['rental_date', 'rental_time']},
        ),
    ]
