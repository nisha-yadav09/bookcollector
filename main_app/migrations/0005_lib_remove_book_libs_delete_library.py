# Generated by Django 4.0.3 on 2022-05-24 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_library_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lib',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='libs',
        ),
        migrations.DeleteModel(
            name='Library',
        ),
    ]
