# Generated by Django 3.0 on 2023-09-06 03:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OrphanageApp', '0007_auto_20230905_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_orphan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.PositiveIntegerField(default=0)),
                ('father_name', models.CharField(max_length=50)),
                ('mother_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AddoptentForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Alocation', models.CharField(max_length=100)),
                ('Adsg', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.CharField(max_length=100)),
                ('Asd', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
