# Generated by Django 3.2.18 on 2023-04-19 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Freight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supervisor_client', models.CharField(max_length=255)),
                ('date', models.DateField(blank=True, null=True)),
                ('description', models.CharField(max_length=255)),
                ('sub_total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('importe_gravado', models.DecimalField(decimal_places=2, max_digits=6)),
                ('isv', models.DecimalField(decimal_places=2, max_digits=6)),
                ('total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('is_completed', models.BooleanField(default=False)),
                ('payment_method', models.CharField(max_length=255)),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.client')),
                ('id_motorist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.motorist')),
                ('id_partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.partner')),
                ('id_truck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.truck')),
            ],
        ),
    ]