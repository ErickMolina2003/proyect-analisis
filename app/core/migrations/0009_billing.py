# Generated by Django 3.2.18 on 2023-04-19 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_freight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('id_freight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.freight')),
            ],
        ),
    ]