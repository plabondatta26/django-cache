# Generated by Django 4.2.7 on 2023-11-25 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_authormodel_created_at_authormodel_publish_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='publish_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='publish_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
