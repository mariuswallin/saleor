# Generated by Django 3.0.4 on 2020-03-10 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0080_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='language_code',
            field=models.CharField(default='nb', max_length=35),
        ),
    ]
