# Generated by Django 4.2.7 on 2023-11-11 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_rename_total_revenue_company_total_profit_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='total_profit',
            new_name='profit',
        ),
    ]
