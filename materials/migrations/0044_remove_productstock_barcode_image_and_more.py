# Generated by Django 4.2 on 2024-01-02 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0043_alter_productstock_barcode_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productstock',
            name='barcode_image',
        ),
        migrations.AddField(
            model_name='productstock',
            name='barcode',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
