# Generated by Django 4.1.7 on 2023-03-01 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ezradjango_dtbregistration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
    ]
