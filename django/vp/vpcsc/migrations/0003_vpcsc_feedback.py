# Generated by Django 3.2.3 on 2021-06-19 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpcsc', '0002_auto_20210603_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='vpcsc_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bad', models.CharField(max_length=122)),
                ('average', models.CharField(max_length=122)),
                ('good', models.CharField(max_length=122)),
                ('comments', models.TextField()),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('date', models.DateField()),
            ],
        ),
    ]
