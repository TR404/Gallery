# Generated by Django 3.2.4 on 2021-07-16 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cars', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Application.cars')),
                ('nature', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Application.nature')),
                ('portrait', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Application.portrait')),
                ('sketch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Application.sketch')),
                ('wildlife', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Application.wildlife')),
            ],
        ),
    ]
