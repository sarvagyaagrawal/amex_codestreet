# Generated by Django 3.1.3 on 2021-10-03 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_auto_20211002_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='future_banking',
            name='b_risk_score',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='present_banking',
            name='b_debt_to_inc',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='present_banking',
            name='b_spend_to_save',
            field=models.FloatField(),
        ),
    ]