# Generated by Django 3.0 on 2023-08-16 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrphanageApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role_type',
            field=models.CharField(choices=[('0', 'Guest'), ('1', 'Adoptent'), ('2', 'Manager')], default='0', max_length=5),
        ),
    ]
