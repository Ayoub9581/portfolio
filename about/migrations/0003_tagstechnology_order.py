# Generated by Django 2.2.12 on 2020-05-24 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20200523_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='tagstechnology',
            name='order',
            field=models.IntegerField(default=60),
        ),
    ]
