# Generated by Django 2.0.1 on 2018-01-17 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('short', models.URLField(blank=True, unique=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('visited', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
