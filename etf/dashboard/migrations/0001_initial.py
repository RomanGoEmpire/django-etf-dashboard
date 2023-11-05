# Generated by Django 4.2.7 on 2023-11-05 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CLient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birthday', models.DateTimeField()),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'female')], max_length=2)),
                ('adress', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=30)),
            ],
        ),
    ]
