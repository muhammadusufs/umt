# Generated by Django 5.0 on 2023-12-23 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialstorage',
            name='amount_type',
            field=models.CharField(choices=[('gram', 'Gramm'), ('liter', 'Litr'), ('kg', 'Kilogramm'), ('point', 'Dona')], max_length=5),
        ),
    ]