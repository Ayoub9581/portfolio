# Generated by Django 2.2.12 on 2020-05-23 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='tagstechnology',
            options={'ordering': ['-updated']},
        ),
    ]