# Generated by Django 4.1.7 on 2023-04-04 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teazen', '0009_alter_order_options_alter_orderitem_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='teazen.orderitem'),
        ),
    ]
