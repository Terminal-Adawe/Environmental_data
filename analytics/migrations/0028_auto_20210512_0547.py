# Generated by Django 3.1.6 on 2021-05-12 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0027_notifications_notificationviewer_wastedetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wastedetails',
            name='waste_weightage',
            field=models.IntegerField(),
        ),
    ]
