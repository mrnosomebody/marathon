# Generated by Django 3.1.4 on 2020-12-11 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marathon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='status_id',
            field=models.ManyToManyField(to='marathon.Status'),
        ),
        migrations.DeleteModel(
            name='PersonStatus',
        ),
    ]
