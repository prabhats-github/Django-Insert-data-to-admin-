# Generated by Django 5.0.3 on 2024-03-30 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='res',
            name='adults',
        ),
        migrations.RemoveField(
            model_name='res',
            name='children',
        ),
        migrations.RemoveField(
            model_name='res',
            name='chkin',
        ),
        migrations.RemoveField(
            model_name='res',
            name='chkout',
        ),
        migrations.RemoveField(
            model_name='res',
            name='no_of_rooms',
        ),
        migrations.RemoveField(
            model_name='res',
            name='room_type',
        ),
    ]
