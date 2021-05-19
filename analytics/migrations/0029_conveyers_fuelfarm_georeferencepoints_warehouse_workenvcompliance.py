# Generated by Django 3.1.6 on 2021-05-14 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('analytics', '0028_auto_20210512_0547'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkEnvCompliance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_name', models.CharField(blank=True, default='REPORT_15', max_length=100, null=True)),
                ('first_aid', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], max_length=10)),
                ('safety_stickers', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], max_length=10)),
                ('estinquishers', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], max_length=10)),
                ('no_of_estinquishers', models.CharField(blank=True, max_length=10, null=True)),
                ('fire_alarm', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], max_length=10)),
                ('flooding', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], max_length=10)),
                ('flammables', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], max_length=10)),
                ('location', models.CharField(default='0,0', max_length=200)),
                ('comment', models.TextField(blank=True, null=True)),
                ('module', models.CharField(default='15', max_length=50)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_name', models.CharField(blank=True, default='REPORT_16', max_length=100, null=True)),
                ('eye_wash', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], max_length=10)),
                ('shower', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], max_length=10)),
                ('location', models.CharField(default='0,0', max_length=200)),
                ('comment', models.TextField(blank=True, null=True)),
                ('module', models.CharField(default='16', max_length=50)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GeoReferencePoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_name', models.CharField(blank=True, default='REPORT_13', max_length=100, null=True)),
                ('location', models.CharField(default='0,0', max_length=200)),
                ('comment', models.TextField(blank=True, null=True)),
                ('module', models.CharField(default='13', max_length=50)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FuelFarm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_name', models.CharField(blank=True, default='REPORT_14', max_length=100, null=True)),
                ('spillage_status', models.CharField(choices=[('NO SPILLAGE', 'No Spillage'), ('HIGH SPILLAGE', 'High Spillage'), ('LOW SPILLAGE', 'Low Spillage')], max_length=100)),
                ('impervious_status', models.CharField(choices=[('NOT IMPERVIOUS', 'Not Impervious'), ('IMPERVIOUS', 'Impervious'), ('SEMI IMPERVIOUS', 'Semi Impervious')], max_length=100)),
                ('location', models.CharField(default='0,0', max_length=200)),
                ('comment', models.TextField(blank=True, null=True)),
                ('module', models.CharField(default='14', max_length=50)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Conveyers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_name', models.CharField(blank=True, default='REPORT_17', max_length=100, null=True)),
                ('electrical_safety_insulation', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], max_length=10)),
                ('shower', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], max_length=100)),
                ('location', models.CharField(default='0,0', max_length=200)),
                ('comment', models.TextField(blank=True, null=True)),
                ('module', models.CharField(default='17', max_length=50)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
