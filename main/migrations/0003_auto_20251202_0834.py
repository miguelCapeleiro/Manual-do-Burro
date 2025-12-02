from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('main', 'NÚMERO_DA_ULTIMA_MIGRATION'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Assuntos',
            new_name='Assunto',
        ),
        migrations.AlterModelTable(
            name='Assunto',
            table='main_assuntos',  # mantém o nome antigo temporariamente
        ),
    ]
