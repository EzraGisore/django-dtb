# Generated by Django 4.1.7 on 2023-03-01 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ezradjango_dtbregistration', '0003_alter_student_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
