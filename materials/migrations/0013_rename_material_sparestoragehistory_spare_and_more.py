# Generated by Django 5.0 on 2023-12-24 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0012_alter_sparestorage_amount_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sparestoragehistory',
            old_name='material',
            new_name='spare',
        ),
        migrations.AlterField(
            model_name='materialstoragehistory',
            name='where',
            field=models.CharField(choices=[('null', '--------'), ('material', 'Homashyo ombori'), ('spare', 'Ehtiyot qism ombori'), ('yaim', 'Yarim tayyor mahsulot'), ('production', 'Tayyor mahsulot ombori'), ('storage', 'Mahsulot ombori')], default='null', max_length=16),
        ),
        migrations.AlterField(
            model_name='sparestoragehistory',
            name='where',
            field=models.CharField(choices=[('null', '--------'), ('material', 'Homashyo ombori'), ('spare', 'Ehtiyot qism ombori'), ('yaim', 'Yarim tayyor mahsulot'), ('production', 'Tayyor mahsulot ombori'), ('storage', 'Mahsulot ombori')], default='null', max_length=16),
        ),
    ]