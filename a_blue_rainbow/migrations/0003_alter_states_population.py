# Generated by Django 4.2 on 2023-04-11 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_blue_rainbow', '0002_alter_states_population'),
    ]

    operations = [
        migrations.AlterField(
            model_name='states',
            name='population',
            field=models.IntegerField(null=True),
        ),
    ]
