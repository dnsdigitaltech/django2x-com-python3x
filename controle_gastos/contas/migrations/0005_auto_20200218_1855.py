# Generated by Django 3.0.3 on 2020-02-18 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0004_auto_20200218_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
