# Generated by Django 5.0.6 on 2024-06-14 16:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('positions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('photo', models.BinaryField(max_length='max', null=True)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='positions.positions')),
            ],
            options={
                'db_table': 'Teachers',
            },
        ),
    ]
