# Generated by Django 4.0.4 on 2022-06-19 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entrevistas', '0007_rename_image_entrevistasmodel_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrevistasmodel',
            name='Imagen',
            field=models.ImageField(blank=True, null=True, upload_to='Fotos/'),
        ),
    ]
