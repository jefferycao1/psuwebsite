# Generated by Django 2.0 on 2018-01-16 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0013_alumni_major'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentteam',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
