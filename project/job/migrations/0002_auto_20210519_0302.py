# Generated by Django 3.2.2 on 2021-05-19 01:02

from django.db import migrations, models
import job.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='Job_Type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], max_length=15),
        ),
        migrations.AlterField(
            model_name='job',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=job.models.upload_image),
        ),
    ]
