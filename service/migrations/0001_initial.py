# Generated by Django 4.0.4 on 2022-05-27 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, verbose_name='Название услуги')),
                ('cost_price', models.PositiveIntegerField(verbose_name='Себестоимость')),
                ('price', models.PositiveIntegerField(verbose_name='Стоимость')),
                ('description', models.TextField(verbose_name='Стоимость')),
                ('duration', models.DurationField(verbose_name='Продолжительность')),
            ],
            options={
                'db_table': 'service',
            },
        ),
    ]
