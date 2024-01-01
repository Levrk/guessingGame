# Generated by Django 5.0 on 2024-01-01 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('publisher', models.CharField(max_length=200)),
                ('platform', models.CharField(max_length=400)),
                ('rating', models.IntegerField()),
                ('series', models.IntegerField(null=True)),
                ('genre1', models.CharField(max_length=100)),
                ('genre2', models.CharField(max_length=100)),
                ('setting', models.CharField(max_length=100)),
                ('period', models.CharField(max_length=100)),
                ('multiplayer', models.CharField(max_length=200)),
                ('playtime', models.IntegerField()),
            ],
        ),
    ]
