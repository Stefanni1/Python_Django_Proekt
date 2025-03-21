from django.db import models

class Ad(models.Model):
    CURRENCY_CHOICES = [
        ('MKD', 'ден.'),
        ('EUR', 'е'),
    ]

    CATEGORY_CHOICES = [
        ('AVTOMOBILI', 'Автомобили'),
        ('MOBILNI', 'Мобилни телефони'),
        ('ELEKTRONIKA', 'Електроника'),
        ('DOM', 'Дом и градина'),
        ('MODA', 'Мода'),
        ('USLUGI', 'Услуги'),
        ('DRUGO', 'Друго'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='DRUGO')
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='MKD')
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title