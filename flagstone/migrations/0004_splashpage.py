# Generated by Django 3.0.2 on 2020-02-20 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flagstone', '0003_auto_20200219_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='SplashPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rogerDodger', models.CharField(default='o', max_length=1)),
            ],
        ),
    ]
