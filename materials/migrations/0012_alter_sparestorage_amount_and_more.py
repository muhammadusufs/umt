# Generated by Django 5.0 on 2023-12-24 05:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0011_sparestorage_barcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sparestorage',
            name='amount',
            field=models.CharField(max_length=255, verbose_name='Miqdori'),
        ),
        migrations.AlterField(
            model_name='sparestorage',
            name='amount_type',
            field=models.CharField(choices=[('gram', 'Gramm'), ('liter', 'Litr'), ('kg', 'Kilogramm'), ('point', 'Dona'), ('meter', 'Metr')], default='meter', max_length=16, verbose_name='Miqdor turi'),
        ),
        migrations.AlterField(
            model_name='sparestorage',
            name='barcode',
            field=models.CharField(max_length=255, verbose_name='Barkod'),
        ),
        migrations.AlterField(
            model_name='sparestorage',
            name='confirmed_price',
            field=models.CharField(default=0, max_length=600, verbose_name='Tasdiqlangan narxi'),
        ),
        migrations.AlterField(
            model_name='sparestorage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti"),
        ),
        migrations.AlterField(
            model_name='sparestorage',
            name='import_comment',
            field=models.CharField(max_length=255, verbose_name='Izoh'),
        ),
        migrations.AlterField(
            model_name='sparestorage',
            name='is_active',
            field=models.CharField(choices=[('active', 'Faol'), ('inactive', 'Nofaol'), ('pending', 'Kutilmoqda')], default='pending', max_length=8, verbose_name='Holati'),
        ),
        migrations.AlterField(
            model_name='sparestorage',
            name='price',
            field=models.CharField(default=0, max_length=600, verbose_name='Narxi'),
        ),
        migrations.AlterField(
            model_name='sparestorage',
            name='price_type',
            field=models.CharField(choices=[('uzs', 'UZS'), ('usd', 'USD')], default='usd', max_length=3, verbose_name='Pul birligi'),
        ),
        migrations.AlterField(
            model_name='sparestorage',
            name='spare',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='materials.sparetype', verbose_name='Ehtiyot qism'),
        ),
        migrations.AlterField(
            model_name='sparestorage',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Oxirgi yangilanish'),
        ),
    ]
