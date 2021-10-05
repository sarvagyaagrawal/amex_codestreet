# Generated by Django 3.1.3 on 2021-10-04 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bankcustomer', '0004_bank_customer_amt_withdraw'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdrawl',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bank_customer',
            name='UBI',
            field=models.UUIDField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bank_customer',
            name='balance',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='credit_card',
            name='due_amt',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='credit_card',
            name='int_rate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='credit_card',
            name='mini_amt',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='loan_details',
            name='due_amt',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='loan_details',
            name='int_rate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='loan_details',
            name='loan_amt',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='loan_details',
            name='mini_amt',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='withdrawl',
            name='amt1',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='withdrawl',
            name='amt2',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='withdrawl',
            name='amt3',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='withdrawl',
            name='amt4',
            field=models.IntegerField(),
        ),
    ]