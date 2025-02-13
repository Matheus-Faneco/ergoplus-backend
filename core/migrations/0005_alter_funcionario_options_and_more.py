# Generated by Django 5.1.6 on 2025-02-13 21:11

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0004_rename_id_funcionario_camera_funcionario_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='funcionario',
            options={'ordering': ['nome'], 'verbose_name': 'Funcionário', 'verbose_name_plural': 'Funcionários'},
        ),
        migrations.AlterModelOptions(
            name='registropostura',
            options={'ordering': ['-inicio'], 'verbose_name': 'Registro de Postura', 'verbose_name_plural': 'Registros de Postura'},
        ),
        migrations.AddField(
            model_name='funcionario',
            name='created_at',
            field=models.DateTimeField(db_column='dt_created', default=django.utils.timezone.now, verbose_name='Data de criação'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='registropostura',
            name='funcionario',
            field=models.ForeignKey(db_column='id_funcionario', on_delete=django.db.models.deletion.CASCADE, to='core.funcionario', verbose_name='Funcionário'),
        ),
    ]
