# Generated by Django 2.2.12 on 2020-05-23 13:16

from django.db import migrations, models
import portfolio.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('about', '0002_auto_20200523_1316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=50)),
                ('project_image', models.ImageField(upload_to=portfolio.models.upload_to)),
                ('project_description', models.TextField()),
                ('link_visite', models.URLField()),
                ('link_source', models.URLField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('technologies', models.ManyToManyField(to='about.TagsTechnology')),
            ],
            options={
                'db_table': 'portfolio',
            },
        ),
    ]
