# Generated by Django 3.2.4 on 2021-07-02 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ricerca_app', '0005_auto_20210625_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='didatticacdslingua',
            name='cdsord',
            field=models.ForeignKey(blank=True, db_column='CDSORD_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='didatticacdslingua', to='ricerca_app.didatticacds', to_field='cdsord_id'),
        ),
    ]
