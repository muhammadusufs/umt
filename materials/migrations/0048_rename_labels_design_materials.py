# Generated by Django 4.2 on 2024-01-03 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0047_designpricehistory_exchange'),
    ]

    operations = [
        migrations.RenameField(
            model_name='design',
            old_name='labels',
            new_name='materials',
        ),
    ]
