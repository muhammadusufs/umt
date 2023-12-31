# Generated by Django 5.0 on 2024-01-01 06:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0038_alter_preproductionhistory_production'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSalesCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=255)),
                ('card_id', models.CharField(max_length=1000)),
                ('cost', models.CharField(default=0, max_length=255)),
                ('given_cost', models.CharField(default=0, max_length=255)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSalesHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taken_cost', models.CharField(default=0, max_length=255)),
                ('end_cost', models.CharField(default=0, max_length=255)),
                ('status', models.CharField(choices=[('start', 'Savdo boshlandi'), ('process', 'Pul olindi'), ('end', 'Qarz tugadi'), ('complete', 'Savdo yakunlandi')], max_length=255)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='materials.productsalescard')),
            ],
        ),
        migrations.CreateModel(
            name='ProductStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_amount', models.IntegerField(max_length=255)),
                ('product_per_set', models.IntegerField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('confirmed_price', models.CharField(max_length=255)),
                ('price_type', models.CharField(choices=[('uzs', 'UZS'), ('usd', 'USD')], max_length=255)),
                ('comment', models.CharField(max_length=255)),
                ('is_active', models.CharField(choices=[('active', 'Faol'), ('inactive', 'Nofaol'), ('deleted', 'O`chirilgan'), ('pending', 'Kutilmoqda')], default='pending', max_length=8)),
                ('design', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='materials.design')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.CharField(default=0, max_length=255)),
                ('discount', models.CharField(default=0, max_length=255)),
                ('amount', models.CharField(max_length=255)),
                ('per_set', models.CharField(max_length=255)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='materials.productsalescard')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='materials.productstock')),
            ],
        ),
        migrations.CreateModel(
            name='ProductStockHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=255)),
                ('action', models.CharField(choices=[('import', 'Kirim'), ('export', 'Chiqim'), ('update', 'Yangilash'), ('delete', "O'chirish"), ('cancel', 'Bekor qilish'), ('sold', 'Sotish'), ('confirm', 'Tasdiqlash')], max_length=15)),
                ('amount', models.CharField(default='0', max_length=255)),
                ('amount_type', models.CharField(choices=[('gram', 'Gramm'), ('liter', 'Litr'), ('kg', 'Kilogramm'), ('point', 'Dona'), ('meter', 'Metr')], default='point', max_length=5)),
                ('price', models.CharField(blank=True, max_length=255)),
                ('price_type', models.CharField(choices=[('uzs', 'UZS'), ('usd', 'USD')], default='uzs', max_length=5)),
                ('where', models.CharField(choices=[('null', '--------'), ('material', 'Homashyo ombori'), ('brak', 'Brak mahsulot'), ('label', 'Etiketika ombori'), ('production', 'Ishlab chiqarish'), ('spare', 'Ehtiyot qism ombori'), ('yaim', 'Yarim tayyor mahsulot'), ('product', 'Tayyor mahsulot ombori'), ('storage', 'Mahsulot ombori')], default='storage', max_length=16)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('executor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
