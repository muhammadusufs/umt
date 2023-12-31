# Generated by Django 5.0 on 2023-12-23 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0006_materialstoragehistory_amount_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialstorage',
            name='confirmed_price',
            field=models.CharField(default=0, max_length=600, verbose_name='Tasdiqlangan narx'),
        ),
        migrations.AlterField(
            model_name='materialstorage',
            name='price',
            field=models.CharField(default=0, max_length=600, verbose_name='Narx'),
        ),
        migrations.AlterField(
            model_name='materialstorage',
            name='price_type',
            field=models.CharField(choices=[('uzs', 'UZS'), ('usd', 'USD')], default='usd', max_length=3, verbose_name='Pul birligi'),
        ),
        migrations.AlterField(
            model_name='materialstoragehistory',
            name='action',
            field=models.CharField(choices=[('import', 'Kirim'), ('export', 'Chiqim'), ('update', 'Yangilash'), ('delete', "O'chirish"), ('cancel', 'Bekor qilish'), ('sold', 'Sotish'), ('confirmed', 'Tasdiqlash')], max_length=9),
        ),
    ]
