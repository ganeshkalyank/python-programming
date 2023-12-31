# Generated by Django 4.2.7 on 2023-11-26 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('contact_number', models.IntegerField()),
                ('vehicle_type', models.TextField()),
                ('brand', models.TextField()),
                ('model_name', models.TextField()),
                ('year_of_purchase', models.TextField()),
                ('kilometers', models.IntegerField()),
                ('color', models.TextField()),
                ('registered_state', models.TextField()),
                ('no_of_owners', models.IntegerField()),
                ('base_price', models.IntegerField()),
                ('mode_of_payment', models.TextField()),
            ],
        ),
    ]
