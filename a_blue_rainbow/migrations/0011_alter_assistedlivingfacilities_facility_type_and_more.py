# Generated by Django 4.2 on 2023-04-14 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('a_blue_rainbow', '0010_providers_facility_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assistedlivingfacilities',
            name='facility_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='assisted_living', to='a_blue_rainbow.providers'),
        ),
        migrations.AlterField(
            model_name='homehealthfacilities',
            name='facility_type',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='home_health', to='a_blue_rainbow.providers'),
        ),
        migrations.AlterField(
            model_name='hospicefacilities',
            name='facility_type',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='hospice', to='a_blue_rainbow.providers'),
        ),
        migrations.AlterField(
            model_name='skillednursingfacilities',
            name='facility_type',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='skilled_nursing', to='a_blue_rainbow.providers'),
        ),
    ]
