# Generated by Django 4.0.3 on 2022-04-15 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_product_category_id_product_category_id_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category_id_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category'),
        ),
    ]
