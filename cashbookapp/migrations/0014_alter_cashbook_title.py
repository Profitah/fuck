# Generated by Django 4.0.4 on 2022-09-25 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashbookapp', '0013_alter_cashbook_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashbook',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
