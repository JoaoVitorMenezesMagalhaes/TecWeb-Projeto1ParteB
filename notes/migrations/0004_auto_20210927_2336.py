# Generated by Django 3.2.7 on 2021-09-28 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_alter_note_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='notas',
            field=models.CharField(default='oi', max_length=40),
        ),
    ]
