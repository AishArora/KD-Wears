# Generated by Django 4.1.3 on 2023-04-19 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_order_address_order_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
    ]