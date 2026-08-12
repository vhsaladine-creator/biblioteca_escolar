from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usuarios", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="aluno",
            name="digito_ra",
            field=models.CharField(default="", max_length=2),
        ),
        migrations.AddField(
            model_name="aluno",
            name="uf",
            field=models.CharField(default="SP", max_length=2),
        ),
        migrations.AlterField(
            model_name="professor",
            name="telefone",
            field=models.CharField(max_length=15),
        ),
    ]
