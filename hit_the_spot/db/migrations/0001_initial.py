# Generated by Django 5.1.3 on 2024-12-09 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('singer', models.CharField(max_length=100)),
                ('composer', models.CharField(max_length=100)),
                ('star', models.BooleanField(default=False)),
            ],
        ),
    ]