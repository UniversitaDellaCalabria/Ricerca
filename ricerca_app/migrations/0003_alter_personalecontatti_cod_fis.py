# Generated by Django 3.2.4 on 2021-06-23 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ricerca_app', '0002_personalecontatti_personaletipocontatto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalecontatti',
            name='cod_fis',
            field=models.ForeignKey(blank=True, db_column='COD_FIS', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ricerca_app.personale'),
        ),
    ]
