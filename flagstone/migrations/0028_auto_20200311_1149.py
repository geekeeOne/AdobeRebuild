# Generated by Django 3.0.2 on 2020-03-11 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flagstone', '0027_customercarf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customercarf',
            name='arrival_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='customercarf',
            name='arrival_flight',
            field=models.CharField(blank=True, choices=[('SW-1350 (SAN)', 'SW-1350 (SAN)'), ('SW-1546 (LBB-DEN)', 'SW-1546 (LBB-DEN)'), ('SW-1948 (OAK-LAX)', 'SW-1948 (OAK-LAX)'), ('SW-2467 (MDW)', 'SW-2467 (MDW)'), ('SW-4112 (SNA-LAS)', 'SW-4112 (SNA-LAS)'), ('SW-2603 (SLC-LAX)', 'SW-2603 (SLC-LAX)'), ('SW-4183 (ONT-LAX)', 'SW-4183 (ONT-LAX)'), ('SW-1488 (MKE-SJC)', 'SW-1488 (MKE-SJC)'), ('SW-0364 (DEN)', 'SW-0364 (DEN)'), ('SW-1506 (LAX)', 'SW-1506 (LAX)'), ('SW-2430 (SAN)', 'SW-2430 (SAN)'), ('AA-1998 (DFW)', 'AA-1998 (DFW)'), ('AA-2003 (PHX)', 'AA-2003 (PHX)'), ('AA-2710 (DFW)', 'AA-2710 (DFW)'), ('AA-5826 (PHX)', 'AA-5826 (PHX)'), ('AA-1162 (ORD)', 'AA-1162 (ORD)'), ('AA-2824 (DFW)', 'AA-2824 (DFW)'), ('AA-5820 (PHX)', 'AA-5820 (PHX)'), ('AA-1097 (DFW)', 'AA-1097 (DFW)'), ('AA-6063 (LAX)', 'AA-6063 (LAX)'), ('AA-1441 (DFW)', 'AA-1441 (DFW)'), ('AA-2017 (PHX)', 'AA-2017 (PHX)'), ('AA-1207 (DFW)', 'AA-1207 (DFW)'), ('AA-5737 (PHX)', 'AA-5737 (PHX)'), ('AA-5870 (PHX)', 'AA-5870 (PHX)'), ('AA-3046 (LAX)', 'AA-3046 (LAX)'), ('AA-2228 (ORD)', 'AA-2228 (ORD)'), ('AA-2732 (PHX)', 'AA-2732 (PHX)'), ('AA-0649 (DFW)', 'AA-0649 (DFW)'), ('UN-5572 (DEN)', 'UN-5572 (DEN)'), ('UN-5802 (SFO)', 'UN-5802 (SFO)'), ('UN-6121 (IAH)', 'UN-6121 (IAH)'), ('UN-2034 (ORD)', 'UN-2034 (ORD)'), ('UN-0440 (DEN)', 'UN-0440 (DEN)'), ('UN-5487 (IAH)', 'UN-5487 (IAH)'), ('UN-6177 (IAH)', 'UN-6177 (IAH)'), ('UN-4659 (DEN)', 'UN-4659 (DEN)'), ('UN-5678 (DEN)', 'UN-5678 (DEN)'), ('UN-5527 (SF0)', 'UN-5527 (SF0)'), ('UN-5307 (DEN)', 'UN-5307 (DEN)'), ('UN-5887 (SFO)', 'UN-5887 (SFO)'), ('UN-6100 (IAH)', 'UN-6100 (IAH)'), ('UN-5396 (SFO)', 'UN-5396 (SFO)'), ('UN-6215 (IAH)', 'UN-6215 (IAH)'), ('DL-3803 (SLC)', 'DL-3803 (SLC)'), ('DL-3589 (LAX)', 'DL-3589 (LAX)'), ('DL-2789 (ATL)', 'DL-2789 (ATL)'), ('DL-0780 (SEA)', 'DL-0780 (SEA)'), ('DL-2714 (MSP)', 'DL-2714 (MSP)'), ('DL-3880 (LAX)', 'DL-3880 (LAX)'), ('DL-3989 (LAX)', 'DL-3989 (LAX)'), ('DL-1739 (ATL)', 'DL-1739 (ATL)'), ('DL-4545 (SLC)', 'DL-4545 (SLC)'), ('AL-3446 (PDX)', 'AL-3446 (PDX)'), ('AL-0648 (SEA)', 'AL-0648 (SEA)'), ('AL-3437 (PDX)', 'AL-3437 (PDX)'), ('AL-1996 (SEA)', 'AL-1996 (SEA)'), ('SC-0663 (LAS)', 'SC-0663 (LAS)')], max_length=28),
        ),
        migrations.AlterField(
            model_name='customercarf',
            name='arrival_time',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='customercarf',
            name='cc_cv',
            field=models.CharField(blank=True, max_length=28),
        ),
        migrations.AlterField(
            model_name='customercarf',
            name='cc_exp',
            field=models.CharField(blank=True, max_length=28),
        ),
        migrations.AlterField(
            model_name='customercarf',
            name='cc_number',
            field=models.CharField(blank=True, max_length=28),
        ),
        migrations.AlterField(
            model_name='customercarf',
            name='departure_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='customercarf',
            name='departure_flight',
            field=models.CharField(blank=True, choices=[('SW-2595 (SAN)', 'SW-2595 (SAN)'), ('SW-2057 (DEN)', 'SW-2057 (DEN)'), ('SW-1948 (LAS)', 'SW-1948 (LAS)'), ('SW-2467 (LAX)', 'SW-2467 (LAX)'), ('SW-2394 (SJC)', 'SW-2394 (SJC)'), ('SW-2603 (DEN)', 'SW-2603 (DEN)'), ('SW-0683 (LAX)', 'SW-0683 (LAX)'), ('SW-2385 (SAN)', 'SW-2385 (SAN)'), ('AA-5899 (PHX)', 'AA-5899 (PHX)'), ('AA-2818 (DFW)', 'AA-2818 (DFW)'), ('AA-5805 (PHX)', 'AA-5805 (PHX)'), ('AA-2311 (ORD)', 'AA-2311 (ORD)'), ('AA-2047 (DFW)', 'AA-2047 (DFW)'), ('AA-2003 (PHX)', 'AA-2003 (PHX)'), ('AA-2486 (DFW)', 'AA-2486 (DFW)'), ('AA-5826 (PHX)', 'AA-5826 (PHX)'), ('AA-1162 (ORD)', 'AA-1162 (ORD)'), ('AA-2199 (DFW)', 'AA-2199 (DFW)'), ('AA-5820 (PHX)', 'AA-5820 (PHX)'), ('AA-1097 (DFW)', 'AA-1097 (DFW)'), ('AA-6063 (LAX)', 'AA-6063 (LAX)'), ('AA-2017 (PHX)', 'AA-2017 (PHX)'), ('UN-6126 (IAH)', 'UN-6126 (IAH)'), ('UN-5479 (DEN)', 'UN-5479 (DEN)'), ('UN-5626 (IAH)', 'UN-5626 (IAH)'), ('UN-2074 (ORD)', 'UN-2074 (ORD)'), ('UN-1629 (IAH)', 'UN-1629 (IAH)'), ('UN-5595 (SFO)', 'UN-5595 (SFO)'), ('UN-1618 (DEN)', 'UN-1618 (DEN)'), ('UN-6366 (IAH)', 'UN-6366 (IAH)'), ('UN-7411 (DEN)', 'UN-7411 (DEN)'), ('UN-5912 (SFO)', 'UN-5912 (SFO)'), ('DL-4440 (LAX)', 'DL-4440 (LAX)'), ('DL-3803 (SLC)', 'DL-3803 (SLC)'), ('DL-3589 (LAX)', 'DL-3589 (LAX)'), ('DL-2789 (ATL)', 'DL-2789 (ATL)'), ('DL-0780 (SEA)', 'DL-0780 (SEA)'), ('DL-2714 (MSP)', 'DL-2714 (MSP)'), ('DL-3556 (LAX)', 'DL-3556 (LAX)'), ('AL-1993 (SEA)', 'AL-1993 (SEA)'), ('AL-3447 (PDX)', 'AL-3447 (PDX)'), ('AL-0641 (SEA)', 'AL-0641 (SEA)'), ('AL-3497 (PDX)', 'AL-3497 (PDX)'), ('SC-0664 (MSP)', 'SC-0664 (MSP)')], max_length=28),
        ),
        migrations.AlterField(
            model_name='customercarf',
            name='departure_time',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='customercarf',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='customercarf',
            name='pickup_time',
            field=models.TimeField(blank=True),
        ),
    ]
