# Generated by Django 3.2.4 on 2021-06-23 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='size',
            field=models.TextField(choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large'), ('Extra-Large', 'Extra Large')]),
        ),
    ]
