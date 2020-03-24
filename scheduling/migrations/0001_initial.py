# Generated by Django 3.0.3 on 2020-03-22 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_auto_20200322_0458'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('start_time', models.CharField(max_length=50)),
                ('end_time', models.CharField(max_length=50)),
                ('note', models.CharField(max_length=200)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
            ],
        ),
    ]