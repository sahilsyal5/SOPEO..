# Generated by Django 4.1 on 2022-09-04 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_employee_city_employee_state_alter_employee_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='State',
            field=models.CharField(choices=[('Active', 'ACTIVE'), ('Leave_count', 'LEAVE COUNT'), ('On_leave', 'ON LEAVE')], default='Leave_count', max_length=100),
        ),
    ]