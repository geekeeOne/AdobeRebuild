# Generated by Django 3.0.2 on 2020-02-20 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flagstone', '0004_splashpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='shuttle',
            name='status_type',
            field=models.CharField(choices=[('INACTIVE', 'INACTIVE'), ('ACTIVE', 'ACTIVE'), ('COMPLETED', 'COMPLETED')], default='ACTIVE', max_length=26),
        ),
    ]