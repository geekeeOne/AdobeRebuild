# Generated by Django 3.0.2 on 2020-02-27 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flagstone', '0008_auto_20200225_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='customer',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='flagstone.Customer'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='org_name',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='flagstone.Organization'),
        ),
    ]
