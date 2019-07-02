from django.db import models

# Create your models here.
class DaZhong(models.Model):
    id = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=100,null=False)
    shop_reviewcount = models.IntegerField(max_length=200, null=False)
    shop_avgpricetitle = models.IntegerField(max_length=200,null=False)
    shop_effect = models.FloatField(null=False)
    shop_service = models.FloatField(null=False)
    shop_surroundings = models.FloatField(null=False)
    shop_address = models.CharField(max_length=200, null=False)
    shop_telephonenumber = models.CharField(max_length=200, null=False)
    shop_businesshours = models.CharField(max_length=200, null=False)
    shop_url = models.CharField(max_length=200, null=False)
    shop_star = models.CharField(max_length=200, null=False)

    def __str__(self):
        return "<Emp:({id},{shop_name},{shop_reviewcount},{shop_avgpricetitle},{shop_effect},{shop_service},{shop_surroundings},{shop_address},{shop_telephonenumber},{shop_businesshours},{shop_url},{shop_star})>".format(id=self.id, shop_name=self.shop_name, shop_reviewcount=self.shop_reviewcount, shop_avgpricetitle=self.shop_avgpricetitle ,shop_effect=self.shop_effect, shop_service=self.shop_service, shop_surroundings=self.shop_surroundings, shop_address=self.shop_address, shop_telephonenumber=self.shop_telephonenumber, shop_businesshours=self.shop_businesshours, shop_url=self.shop_url, shop_star=self.shop_star)
