# Generated by Django 4.1.3 on 2022-11-27 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.IntegerField(null=True)),
                ('deleted_by', models.IntegerField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
        ),
    ]
