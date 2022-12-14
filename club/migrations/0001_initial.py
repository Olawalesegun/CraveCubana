# Generated by Django 4.1.2 on 2022-11-05 21:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=40)),
                ('seat_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Drinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('brand', models.CharField(max_length=40)),
                ('manufacture_date', models.DateField(default=datetime.datetime.today)),
                ('drinks_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.customers')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=40)),
                ('food_class', models.CharField(max_length=40)),
                ('food_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.drinks')),
            ],
        ),
    ]
