# Generated by Django 3.0.7 on 2020-06-24 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0012_auto_20200624_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(default='customer@gmail.com', max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.BigIntegerField(default=9066371333),
        ),
    ]
