# Generated by Django 4.2.2 on 2023-07-02 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp_test', '0005_alter_goods_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='category',
        ),
        migrations.AlterField(
            model_name='goods',
            name='barcode',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='产品条码'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='number',
            field=models.CharField(max_length=64, verbose_name='产品编号'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='remark',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='spec',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='产品规格'),
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='name',
            field=models.CharField(max_length=64, verbose_name='产品分类名称'),
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='remark',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='产品分类备注'),
        ),
    ]
