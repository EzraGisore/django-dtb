# Generated by Django 4.1.7 on 2023-03-02 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ezradjango_dtbregistration', '0005_student_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='city',
            field=models.CharField(blank=True, default='Nairobi', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='country',
            field=models.CharField(blank=True, default='Kenya', max_length=50),
        ),
    ]