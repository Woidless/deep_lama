# Generated by Django 5.0.6 on 2024-06-06 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_cycle', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('education_form', models.CharField(max_length=255)),
                ('number_of_students', models.IntegerField()),
            ],
            options={
                'db_table': 'SubjectDetails',
            },
        ),
    ]