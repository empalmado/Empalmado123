# Generated by Django 3.2.6 on 2021-08-08 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AoeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='free_quotation',
            name='Contact',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='free_quotation',
            name='Details',
            field=models.TextField(),
        ),
    ]
