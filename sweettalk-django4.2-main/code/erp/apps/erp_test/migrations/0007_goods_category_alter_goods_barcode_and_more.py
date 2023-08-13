# Generated by Django 4.2.2 on 2023-07-02 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp_test', '0006_remove_goods_category_alter_goods_barcode_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='goods_set', to='erp_test.goodscategory', verbose_name='产品分类'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='barcode',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='条码'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='number',
            field=models.CharField(max_length=32, verbose_name='产品编号'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='remark',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='spec',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='规格'),
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='name',
            field=models.CharField(max_length=64, verbose_name='分类名称'),
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='remark',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='备注'),
        ),
    ]