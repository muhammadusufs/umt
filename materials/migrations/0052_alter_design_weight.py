# Generated by Django 4.2 on 2024-01-04 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0051_alter_design_another_percent_alter_design_building_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='weight',
            field=models.FloatField(default=0.0),
        ),
    ]
