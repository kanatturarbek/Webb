# Generated by Django 4.0.3 on 2022-04-15 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_product_category_id_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category_id_id',
            new_name='category_id_id_id',
        ),
    ]