# Generated by Django 5.0.1 on 2024-03-09 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_alter_category_options_alter_expense_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(max_length=266),
        ),
    ]
