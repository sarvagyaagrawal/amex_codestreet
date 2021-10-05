# Generated by Django 3.1.3 on 2021-10-03 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankcustomer', '0002_auto_20211004_0057'),
    ]

    operations = [
        migrations.CreateModel(
            name='withdrawl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amt1', models.BigIntegerField()),
                ('amt2', models.BigIntegerField()),
                ('amt3', models.BigIntegerField()),
                ('amt4', models.BigIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='bank_customer',
            name='balance',
            field=models.BigIntegerField(null=True),
        ),
    ]
