# Generated by Django 3.1.6 on 2021-05-18 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0040_modules_default_report_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationviewer',
            name='notificationsId',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, related_name='notificationviewerNotifications', to='analytics.notifications'),
            preserve_default=False,
        ),
    ]
