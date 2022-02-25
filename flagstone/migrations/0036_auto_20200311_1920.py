# Generated by Django 3.0.2 on 2020-03-12 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flagstone', '0035_auto_20200311_1556'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customercarf',
            options={'ordering': ['arrival_time']},
        ),
        migrations.AlterField(
            model_name='customercarf',
            name='reservation_status',
            field=models.CharField(choices=[('Reserved', 'Reserved'), ('Cancelled', 'Cancelled'), ('Paid-Self', 'Paid-Self'), ('Paid-Other', 'Paid-Other')], default='Reserved', max_length=28),
        ),
        migrations.AlterField(
            model_name='customercarf',
            name='reservation_type',
            field=models.CharField(choices=[('One Way Arrival', 'One Way Arrival'), ('One Way Departure', 'One Way Departure'), ('Round Trip', 'Round Trip')], default='Round Trip', max_length=28),
        ),
    ]