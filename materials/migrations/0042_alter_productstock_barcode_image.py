# Generated by Django 4.2 on 2024-01-02 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0041_alter_productstock_barcode_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productstock',
            name='barcode_image',
            field=models.ImageField(null=True, upload_to='barcodes'),
        ),
    ]