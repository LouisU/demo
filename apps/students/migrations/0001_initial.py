# Generated by Django 2.0 on 2019-04-02 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('sex', models.BooleanField(choices=[(True, 'male'), (False, 'female')], default=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('enabled', models.BooleanField(default=True)),
                ('card_physicalID', models.CharField(max_length=50, null=True)),
                ('cardUid', models.CharField(max_length=50, null=True)),
                ('cardHpt', models.CharField(blank=True, max_length=50, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
