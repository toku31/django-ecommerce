# Generated by Django 3.1.2 on 2020-10-24 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20201022_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Shirt'), ('OW', 'Outwear'), ('SW', 'SportWear')], max_length=2),
        ),
    ]