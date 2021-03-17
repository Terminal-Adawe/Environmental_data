# Generated by Django 3.1.6 on 2021-02-28 09:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0003_compliancevalue'),
    ]

    operations = [
        migrations.AddField(
            model_name='compliancevalue',
            name='key_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
