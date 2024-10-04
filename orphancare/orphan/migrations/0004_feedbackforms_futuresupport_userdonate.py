# Generated by Django 5.1 on 2024-09-03 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orphan', '0003_feedbform_delete_registers'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedbackforms',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('rating', models.CharField(max_length=50)),
                ('experience', models.CharField(max_length=200)),
                ('suggestions', models.CharField(max_length=300)),
                ('positive_aspects', models.CharField(max_length=300)),
                ('areas_for_improvement', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='futuresupport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=12)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='userdonate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('d_items', models.TextField()),
                ('address', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]