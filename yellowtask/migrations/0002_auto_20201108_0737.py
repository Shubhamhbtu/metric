# Generated by Django 3.1.3 on 2020-11-08 07:37

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yellowtask', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mydata',
            name='input_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), blank=True, null=True, size=5),
        ),
    ]