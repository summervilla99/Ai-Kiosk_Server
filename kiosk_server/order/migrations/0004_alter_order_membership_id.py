# Generated by Django 5.0.6 on 2024-06-04 14:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_rename_createdat_customuser_created_at_and_more'),
        ('order', '0003_alter_options_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='membership_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.membership'),
        ),
    ]
