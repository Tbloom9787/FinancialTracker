# Generated by Django 3.0.3 on 2020-03-09 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200309_0121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10)),
                ('price', models.FloatField()),
                ('change', models.FloatField()),
                ('volume', models.CharField(max_length=10)),
            ],
        ),
    ]
