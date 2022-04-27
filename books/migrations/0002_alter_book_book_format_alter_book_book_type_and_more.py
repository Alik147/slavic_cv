# Generated by Django 4.0.4 on 2022-04-27 10:09

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_format',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_type',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='dating',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(default=None, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='exodus',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='file_path',
            field=models.CharField(default=None, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='fond',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='handwriting',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='inventory',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='material',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='months',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=64), blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='book',
            name='number',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='storage',
            field=models.CharField(max_length=128),
        ),
    ]