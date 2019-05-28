# Generated by Django 2.2.1 on 2019-05-28 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndexWord',
            fields=[
                ('word', models.TextField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='processing.IndexWord')),
                ('document_name', models.TextField(max_length=255)),
                ('frequency', models.IntegerField()),
                ('indexes', models.TextField(max_length=255)),
            ],
            options={
                'unique_together': {('word', 'document_name')},
            },
        ),
    ]
