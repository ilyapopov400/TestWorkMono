# Generated by Django 4.2.7 on 2023-12-26 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0005_alter_client_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='cars',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='автотранспорт клиента'),
        ),
    ]
