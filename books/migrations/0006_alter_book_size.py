# Generated by Django 4.0.4 on 2022-05-02 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_book_months_alter_book_months_numbers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='size',
            field=models.IntegerField(default=None, null=True),
        ),
    ]