# Generated by Django 4.1.7 on 2023-04-02 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teazen', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'Продукция', 'verbose_name_plural': 'Продукция'},
        ),
        migrations.AlterModelOptions(
            name='tea',
            options={'ordering': ('name',), 'verbose_name': 'Чай', 'verbose_name_plural': 'Чай'},
        ),
    ]