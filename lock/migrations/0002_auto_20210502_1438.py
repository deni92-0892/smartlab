# Generated by Django 3.0.6 on 2021-05-02 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(help_text='Наименование доступа', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='keyinfo',
            name='Status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lock.Access'),
        ),
    ]
