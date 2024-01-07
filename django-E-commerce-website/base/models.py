from django.db import models
from django.contrib.auth.models import User



# all the item tabials

class tipe(models.Model):
    tipe=models.CharField(max_length=50)

    def __str__(self):
        return self.tipe


class brand(models.Model):
    brand=models.CharField(max_length=50)
    

    def __str__(self):
        return self.brand



class deal(models.Model):
    name=models.CharField(max_length=50)
    deal_img=models.ImageField(upload_to='static/deal_img',default='Null',)

    def __str__(self):
        return self.name




class  item (models.Model):


    item_name=models.CharField(max_length=50)
    item_price=models.CharField(max_length=50)
    item_type=models.ForeignKey(tipe,related_name='itekms_tipes',on_delete=models.CASCADE)
    item_desc=models.TextField()
    item_created_at = models.DateTimeField(auto_now_add=True)
    is_solde = models.BooleanField(default=False)
    item_brand=models.ForeignKey(brand,related_name='itekms_brand',on_delete=models.CASCADE)
    item_deal=models.ForeignKey(deal,related_name='itekms_deal',on_delete=models.CASCADE)

    image1=models.ImageField(upload_to='static/items_images',default='Null',)
    image2=models.ImageField(upload_to='static/items_images',default='Null')
    image3=models.ImageField(upload_to='static/items_images',default='Null')
    image4=models.ImageField(upload_to='static/items_images',default='Null')
    image5=models.ImageField(upload_to='static/items_images',default='Null')
    image6=models.ImageField(upload_to='static/items_images',default='Null')
    image7=models.ImageField(upload_to='static/items_images',default='Null')
    image8=models.ImageField(upload_to='static/items_images',default='Null')
    image9=models.ImageField(upload_to='static/items_images',default='Null')
    image10=models.ImageField(upload_to='static/items_images',default='Null')


    xs = models.BooleanField(default=False)
    xs_amaont=models.IntegerField(default=0)

    s = models.BooleanField(default=False)
    s_amaont=models.IntegerField(default=0)

    m = models.BooleanField(default=False)
    m_amaont=models.IntegerField(default=0)

    l = models.BooleanField(default=False)
    l_amaont=models.IntegerField(default=0)
 
    xl = models.BooleanField(default=False)
    xl_amaont=models.IntegerField(default=0)

    xxl = models.BooleanField(default=False)
    xxl_amaont=models.IntegerField(default=0)

    xxxl = models.BooleanField(default=False)
    xxxl_amaont=models.IntegerField(default=0)


    
    def __str__(self):
        return self.item_name

    

# en items tabals





class user_pro(models.Model):
    user=models.ForeignKey(User,related_name='user_prof',on_delete=models.CASCADE)
    user_phon_number=models.CharField(max_length=11)
    user_near_living=models.CharField(max_length=60)
    user_imge=models.ImageField(upload_to='static/user_imag',default='lol/static/user.png',null=True , blank=True)

class orders(models.Model):
    user_ord=models.ForeignKey(User,related_name='user_orders',on_delete=models.CASCADE, blank=True, null=True)
    item_ord=models.ForeignKey(item,related_name='item_orderd',on_delete=models.CASCADE, blank=True, null=True)
    amaont = models.IntegerField(default=0, blank=True, null=True)
    size = models.TextField(default='', blank=True, null=True)
    ok = models.BooleanField(default=False)


class messegis(models.Model):
    messegis_user=models.ForeignKey(User,related_name='user_messegis',on_delete=models.CASCADE)
    desc=models.TextField()
    items_messegis=models.ForeignKey(item,related_name='items_messegis',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.desc




