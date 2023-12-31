# Generated by Django 4.1.2 on 2023-08-20 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("pedidos", "0003_alter_itempedido_pedido"),
    ]

    operations = [
        migrations.AddField(
            model_name="detalleitem",
            name="cantidad",
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="detalleitem",
            name="item_pedido",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="detalles",
                to="pedidos.itempedido",
            ),
        ),
    ]
