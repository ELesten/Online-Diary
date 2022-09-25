from django.db import models
from apps.users.models import CustomUser

# CHOICES


class PurchaseStatus(models.TextChoices):
    IN_PROCESSING = "In processing"
    COMPLETED = "Completed"
    CANCELED = "Canceled"


# MODELS

class MerchShop(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="merch.images")
    count = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.title


class ShoppingCart(models.Model):
    purchaser = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, related_name="purchase", null=True)
    purchased_item = models.ManyToManyField(MerchShop, related_name="purchased")
    status = models.CharField(
        max_length=255,
        choices=PurchaseStatus.choices,
        default=PurchaseStatus.IN_PROCESSING
    )

    def __str__(self):
        return f"Purchase {self.id} purchaser {self.purchaser.username}"

