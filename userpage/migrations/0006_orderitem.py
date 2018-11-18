# Generated by Django 2.1 on 2018-11-18 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0005_auto_20181111_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('orderid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userpage.Order')),
            ],
        ),
    ]