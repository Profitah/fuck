# Generated by Django 4.0.4 on 2022-09-24 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashbookapp', '0005_alter_cashbook_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashbook',
            name='title',
            field=models.CharField(blank='제목을 입력하세요', max_length=200),
        ),
    ]
