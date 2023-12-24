# Generated by Django 5.0 on 2023-12-24 16:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0016_labeltype_alter_materialstoragehistory_where_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labelstorage',
            name='amount',
            field=models.IntegerField(default=0, verbose_name='Miqdori'),
        ),
        migrations.AlterField(
            model_name='labelstorage',
            name='amount_type',
            field=models.CharField(choices=[('gram', 'Gramm'), ('liter', 'Litr'), ('kg', 'Kilogramm'), ('point', 'Dona'), ('meter', 'Metr')], default='point', max_length=5, verbose_name='Miqdor turi'),
        ),
        migrations.AlterField(
            model_name='labelstorage',
            name='confirmed_price',
            field=models.CharField(default=0, max_length=600, verbose_name='Tasdiqlangan narxi'),
        ),
        migrations.AlterField(
            model_name='labelstorage',
            name='import_comment',
            field=models.CharField(max_length=255, verbose_name='Izoh'),
        ),
        migrations.AlterField(
            model_name='labelstorage',
            name='is_active',
            field=models.CharField(choices=[('active', 'Faol'), ('inactive', 'Nofaol'), ('pending', 'Kutilmoqda')], default='active', max_length=8, verbose_name='Aktiv'),
        ),
        migrations.AlterField(
            model_name='labelstorage',
            name='label',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='materials.labeltype', verbose_name='Etiketika turi'),
        ),
        migrations.AlterField(
            model_name='labelstorage',
            name='price',
            field=models.CharField(max_length=255, verbose_name='Narxi'),
        ),
        migrations.AlterField(
            model_name='labelstorage',
            name='price_type',
            field=models.CharField(choices=[('uzs', 'UZS'), ('usd', 'USD')], default='usd', max_length=3, verbose_name='Pul birligi'),
        ),
        migrations.AlterField(
            model_name='labelstoragehistory',
            name='label',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='materials.labeltype'),
        ),
    ]
