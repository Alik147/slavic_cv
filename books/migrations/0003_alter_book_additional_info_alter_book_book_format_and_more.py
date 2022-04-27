# Generated by Django 4.0.4 on 2022-04-27 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_book_format_alter_book_book_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='additional_info',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_format',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_type',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='dating',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='exodus',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='file_path',
            field=models.CharField(blank=True, default=None, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='fond',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='handwriting',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='inventory',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='material',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='number',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='storage',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
