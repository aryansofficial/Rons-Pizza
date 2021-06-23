# Generated by Django 3.2.4 on 2021-06-18 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='quantity',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='orders',
            name='progress',
            field=models.CharField(blank=True, choices=[('O', 'Ordered'), ('P', 'Prepearing'), ('C', 'Completed')], default='o', max_length=1),
        ),
    ]