# Generated by Django 3.2.5 on 2021-08-07 07:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='student_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 7, 7, 30, 45, 852147, tzinfo=utc)),
        ),
    ]
