# Generated by Django 3.1.3 on 2020-11-08 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('input_list', models.CharField(max_length=64, verbose_name='Input List')),
            ],
        ),
    ]
