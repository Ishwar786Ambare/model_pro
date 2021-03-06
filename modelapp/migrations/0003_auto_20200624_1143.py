# Generated by Django 3.0.7 on 2020-06-24 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0002_auto_20200624_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
