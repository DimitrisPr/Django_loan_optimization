# Generated by Django 3.1.5 on 2021-01-29 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lender', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LoanInstallmentPlans',
            new_name='LoanPlans',
        ),
    ]
