# Generated by Django 2.1.7 on 2019-03-20 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190216_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlightNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='route',
            name='route_flight_numbers',
            field=models.ManyToManyField(to='api.FlightNumber'),
        ),
    ]
