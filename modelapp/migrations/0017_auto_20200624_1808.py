# Generated by Django 3.0.7 on 2020-06-24 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0016_products_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='file',
        ),
        migrations.AddField(
            model_name='vendor',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='file/'),
        ),
    ]
