# Generated by Django 5.1.2 on 2024-11-11 16:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 1, 1, 0, 0)),
            preserve_default=False,
        ),
    ]
