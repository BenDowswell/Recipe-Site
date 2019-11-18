# Generated by Django 2.2.6 on 2019-10-18 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_auto_20191017_2047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_category_name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Measurements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measurement_name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=120)),
                ('recipe_description', models.CharField(max_length=120)),
                ('picture_item', models.CharField(max_length=120)),
                ('prep_time', models.DurationField()),
                ('cook_time', models.DurationField()),
                ('food_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Steps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_number', models.DecimalField(decimal_places=1, max_digits=5)),
                ('step_description', models.CharField(max_length=120)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('Ingredients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.Ingredients')),
                ('measurement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.Measurements')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.Recipe')),
            ],
        ),
    ]