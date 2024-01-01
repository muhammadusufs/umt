# Generated by Django 5.0 on 2024-01-01 05:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0037_alter_labelstoragehistory_where_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preproductionhistory',
            name='production',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='materials.production'),
        ),
    ]
