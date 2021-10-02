# Generated by Django 3.1.3 on 2021-09-30 19:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20211001_0039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_details',
            name='id',
        ),
        migrations.AlterField(
            model_name='customer_details',
            name='U_Bank_Id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]