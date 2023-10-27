# Generated by Django 4.2.6 on 2023-10-24 17:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_shoppingcart'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Created'), (2, 'Wait for payment'), (3, 'Paid'), (4, 'Deliverning'), (5, 'Completed')])),
                ('count', models.IntegerField(default=1)),
                ('upload_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
