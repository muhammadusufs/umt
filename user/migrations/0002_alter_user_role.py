# Generated by Django 4.2 on 2024-01-03 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('SALES', 'Savdo'), ('MATERIAL', 'Material'), ('SPARE', 'Ehtiyot qism'), ('DIRECTOR', 'Nazoratchi')], max_length=32),
        ),
    ]
