# Generated by Django 4.2.7 on 2023-11-26 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlantDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_name', models.TextField()),
                ('plant_type', models.TextField()),
                ('plant_price', models.TextField()),
                ('plant_benefits', models.TextField()),
            ],
        ),
    ]
