# Generated by Django 4.2.7 on 2023-11-05 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('cost', models.FloatField()),
                ('reason', models.CharField(max_length=50)),
                ('target', models.CharField(max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=30)),
                ('hire_date', models.DateField()),
                ('role', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ETF',
            fields=[
                ('id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('exchange', models.CharField(max_length=50)),
                ('ipo_date', models.DateField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='client',
            name='birthday',
            field=models.DateField(),
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('option', models.CharField(max_length=4)),
                ('amount', models.IntegerField()),
                ('frequency', models.CharField(max_length=20)),
                ('etf_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.etf')),
            ],
        ),
        migrations.CreateModel(
            name='Timestamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('open', models.FloatField()),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('close', models.FloatField()),
                ('volume', models.IntegerField()),
                ('etf_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.etf')),
            ],
        ),
        migrations.CreateModel(
            name='Consultations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('duration', models.SmallIntegerField()),
                ('cost', models.IntegerField()),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.client')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.employee')),
            ],
        ),
    ]
