# Generated by Django 3.2 on 2023-03-07 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphql_api', '0004_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]
