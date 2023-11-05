# Generated by Django 4.2.7 on 2023-11-05 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_cost_employee_etf_alter_client_birthday_transactions_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('duration', models.SmallIntegerField()),
                ('cost', models.IntegerField()),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.client')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('option', models.CharField(max_length=4)),
                ('amount', models.IntegerField()),
                ('frequency', models.CharField(max_length=20)),
                ('etf_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.etf')),
            ],
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='etf_id',
        ),
        migrations.DeleteModel(
            name='Consultations',
        ),
        migrations.DeleteModel(
            name='Transactions',
        ),
    ]