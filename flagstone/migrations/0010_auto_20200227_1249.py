# Generated by Django 3.0.2 on 2020-02-27 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flagstone', '0009_auto_20200227_0951'),
    ]

    operations = [
        migrations.CreateModel(
            name='PRAASA_March2020',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.DecimalField(decimal_places=2, default=55.0, max_digits=5)),
                ('name', models.CharField(blank=True, max_length=256)),
                ('phone', models.CharField(blank=True, max_length=28)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('z_code', models.CharField(blank=True, max_length=16)),
                ('cc_num', models.CharField(blank=True, max_length=56)),
                ('cc_exp', models.CharField(blank=True, max_length=56)),
                ('cc_cv', models.CharField(blank=True, max_length=6)),
                ('arrival_date', models.DateField(blank=True)),
                ('arrival_time', models.TimeField(blank=True)),
                ('arrival_airport', models.CharField(blank=True, choices=[('TIA', 'Tucson'), ('SKY', 'SkyHarbor')], default='TIA', max_length=9)),
                ('arrival_airline', models.CharField(blank=True, choices=[('Advanced Air', 'Advanced Air'), ('Air Canada', 'Air Canada'), ('Alaska Airlines', 'Alaska Airlines'), ('Allegiant', 'Allegiant'), ('American Airlines', 'American Airlines'), ('Boutique Air', 'Boutique Air'), ('British Airways', 'British Airways'), ('Condor Airlines', 'Condor Airlines'), ('Contour Airlines', 'Contour Airlines'), ('Delta Air Lines', 'Delta Air Lines'), ('Eurowings', 'Eurowings'), ('Frontier Airlines', 'Frontier Airlines'), ('Hawaiian Airlines', 'Hawaiian Airlines'), ('JetBlue Airways', 'JetBlue Airways'), ('JSX-Swift Aviation', 'JSX-Swift Aviation'), ('Southwest Airlines', 'Southwest Airlines'), ('Spirit Airlines', 'Spirit Airlines'), ('Sun Country Airlines', 'Sun Country Airlines'), ('United Airlines', 'United Airlines'), ('Volaris', 'Volaris'), ('WestJet', 'WestJet'), ('Other', 'Other')], max_length=25)),
                ('arrival_flight', models.CharField(blank=True, max_length=16)),
                ('drop_location', models.CharField(default='Westin La Paloma', max_length=256)),
                ('arrival_notes', models.TextField(blank=True)),
                ('pickup_location', models.CharField(blank=True, max_length=256)),
                ('pickup_time', models.TimeField(blank=True)),
                ('departure_date', models.DateField(blank=True)),
                ('departure_time', models.TimeField(blank=True)),
                ('departure_airport', models.CharField(blank=True, choices=[('TIA', 'Tucson'), ('SKY', 'SkyHarbor')], default='Tucson', max_length=9)),
                ('departure_airline', models.CharField(blank=True, choices=[('Advanced Air', 'Advanced Air'), ('Air Canada', 'Air Canada'), ('Alaska Airlines', 'Alaska Airlines'), ('Allegiant', 'Allegiant'), ('American Airlines', 'American Airlines'), ('Boutique Air', 'Boutique Air'), ('British Airways', 'British Airways'), ('Condor Airlines', 'Condor Airlines'), ('Contour Airlines', 'Contour Airlines'), ('Delta Air Lines', 'Delta Air Lines'), ('Eurowings', 'Eurowings'), ('Frontier Airlines', 'Frontier Airlines'), ('Hawaiian Airlines', 'Hawaiian Airlines'), ('JetBlue Airways', 'JetBlue Airways'), ('JSX-Swift Aviation', 'JSX-Swift Aviation'), ('Southwest Airlines', 'Southwest Airlines'), ('Spirit Airlines', 'Spirit Airlines'), ('Sun Country Airlines', 'Sun Country Airlines'), ('United Airlines', 'United Airlines'), ('Volaris', 'Volaris'), ('WestJet', 'WestJet'), ('Other', 'Other')], max_length=25)),
                ('departure_flight', models.CharField(blank=True, max_length=16)),
                ('departing_notes', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='affiliate_info',
            field=models.ForeignKey(default='Self', on_delete=django.db.models.deletion.CASCADE, to='flagstone.Organization'),
        ),
        migrations.AlterField(
            model_name='driverassignment',
            name='customer_info',
            field=models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, to='flagstone.Customer'),
        ),
        migrations.AlterField(
            model_name='driverassignment',
            name='driver',
            field=models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, to='flagstone.AdobeDriver'),
        ),
        migrations.AlterField(
            model_name='driverassignment',
            name='org_name',
            field=models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, to='flagstone.Organization'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='customer',
            field=models.ForeignKey(default='NaaN', on_delete=django.db.models.deletion.CASCADE, to='flagstone.Customer'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='org_name',
            field=models.ForeignKey(default='NaaN', on_delete=django.db.models.deletion.CASCADE, to='flagstone.Organization'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='van_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flagstone.Van'),
        ),
        migrations.AlterField(
            model_name='shuttle',
            name='customer_info',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='flagstone.Customer'),
        ),
        migrations.AlterField(
            model_name='shuttle',
            name='driver_info',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='flagstone.AdobeDriver'),
        ),
        migrations.AlterField(
            model_name='shuttle',
            name='org_name',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='flagstone.Organization'),
        ),
        migrations.AlterField(
            model_name='shuttle',
            name='van_info',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='flagstone.Van'),
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flagstone.AdobeDriver'),
        ),
    ]