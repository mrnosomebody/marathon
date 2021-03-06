# Generated by Django 3.1.4 on 2020-12-11 09:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('marathon', '0002_auto_20201211_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.RenameField(
            model_name='run',
            old_name='rook_place',
            new_name='took_place',
        ),
        migrations.AddField(
            model_name='event',
            name='place',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sponsor',
            name='event_id',
            field=models.ManyToManyField(to='marathon.Event'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='event',
            name='distance_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='marathon.distance'),
            preserve_default=False,
        ),
    ]
