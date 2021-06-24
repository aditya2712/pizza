# Generated by Django 3.2.4 on 2021-06-24 03:52

"""
    - Create model PizzaTopping
    - Alter field size on pizza
    - Add field toppings to pizza
"""

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaTopping',
            fields=[
                ('topping', models.TextField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='pizza',
            name='size',
            field=models.TextField(choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large'), ('Jumbo', 'Jumbo')]),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(to='pizzaAPI.PizzaTopping'),
        ),
    ]