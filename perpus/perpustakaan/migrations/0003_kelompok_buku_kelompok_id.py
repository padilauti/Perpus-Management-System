# Generated by Django 5.1 on 2024-08-30 12:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0002_buku_jumlah'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kelompok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=9)),
                ('keterangan', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='buku',
            name='kelompok_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='perpustakaan.kelompok'),
        ),
    ]
