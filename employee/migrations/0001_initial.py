# Generated by Django 4.1 on 2022-09-04 15:50

import birthday.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=30)),
                ('Surname', models.CharField(max_length=30)),
                ('DOB_dayofyear_internal', models.PositiveSmallIntegerField(default=None, editable=False, null=True)),
                ('DOB', birthday.fields.BirthdayField()),
                ('DOJ', models.CharField(max_length=10)),
                ('Department', models.CharField(choices=[('D1', 'DEPARTMENT1'), ('D2', 'DEPARTMENT2'), ('D3', 'DEPARTMENT3'), ('D4', 'DEPARTMENT4'), ('D5', 'DEPARTMENT5')], max_length=100)),
                ('Post', models.IntegerField()),
                ('Address', models.CharField(max_length=50)),
            ],
        ),
    ]