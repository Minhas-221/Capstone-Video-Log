# Generated by Django 3.0.5 on 2021-04-25 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20210425_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='fac1',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='courses',
            name='fac2',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='courses',
            name='fac3',
            field=models.BooleanField(default=None),
        ),
    ]
