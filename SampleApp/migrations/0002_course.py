# Generated by Django 3.1.2 on 2023-05-04 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SampleApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('publications', models.ManyToManyField(related_name='courses', to='SampleApp.Student')),
            ],
            options={
                'db_table': 'courses',
            },
        ),
    ]
