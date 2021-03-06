# Generated by Django 3.0.3 on 2020-03-12 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictionAPI', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prediction',
            name='item',
        ),
        migrations.RemoveField(
            model_name='prediction',
            name='unit',
        ),
        migrations.AddField(
            model_name='prediction',
            name='month',
            field=models.IntegerField(default=1, max_length=50),
        ),
        migrations.AddField(
            model_name='prediction',
            name='product',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='category',
            field=models.CharField(default='Grocery', max_length=50),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='gross_sale',
            field=models.FloatField(default=0.0, max_length=50),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='qty',
            field=models.FloatField(default=0.0, max_length=50),
        ),
    ]
