# Generated by Django 4.2 on 2023-04-11 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_blue_rainbow', '0003_alter_states_population'),
    ]

    operations = [
        migrations.AlterField(
            model_name='states',
            name='population',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]