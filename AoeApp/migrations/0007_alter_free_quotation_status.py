# Generated by Django 3.2.6 on 2021-08-24 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AoeApp', '0006_free_quotation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='free_quotation',
            name='status',
            field=models.TextField(choices=[('Done', 'Done'), ('Pending', 'Pending')], default='pending', max_length=20, null=True, verbose_name='status'),
        ),
    ]
