# Generated by Django 2.2.5 on 2019-09-09 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_auto_20190909_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='text',
            field=models.CharField(max_length=2000),
        ),
    ]
