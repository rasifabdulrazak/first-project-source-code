# Generated by Django 4.0.1 on 2022-01-22 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_order_placed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_placed',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('On the way', 'On the way'), ('Accepted', 'Accepted'), ('Packed', 'Packed'), ('Cancel', 'Cancel')], default='pending', max_length=100),
        ),
    ]
