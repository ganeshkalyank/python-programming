# Generated by Django 4.2.7 on 2023-11-25 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AadharNumber', models.TextField()),
                ('Name', models.TextField()),
                ('Age', models.TextField()),
                ('Address', models.TextField()),
                ('NativePlace', models.TextField()),
                ('MobileNumber', models.TextField()),
            ],
        ),
    ]
