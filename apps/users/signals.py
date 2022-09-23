from django.db.models import signals, F
from django.dispatch import receiver
from apps.homeworks.models import Homework
from .models import CustomUser
from apps.merch.models import Purchase, Merch


@receiver(signals.post_save, sender=Homework)
def currency_accrual(instance, **kwargs):
    if instance.homework_status == 'Completed' and instance.connection_with_task.deadline < instance.created_at:
        CustomUser.objects.filter(id=instance.author.id).update(currency=F("currency") + 200)
    else:
        pass


@receiver(signals.m2m_changed, sender=Purchase.purchased_item.through)
def currency_debit(instance, action, **kwargs):
    if action == "post_add":
        purchase_amount = sum(instance.purchased_item.values_list("price", flat=True))
        CustomUser.objects.filter(id=instance.purchaser.id).update(currency=F("currency") - purchase_amount)


@receiver(signals.pre_delete, sender=Purchase)
def currency_return(instance, **kwargs):
    purchases = Merch.objects.filter(id__in=instance.purchased_item.values_list("id"))
    purchase_amount = 0
    for purchase in purchases:
        purchase_amount += purchase.price
    CustomUser.objects.filter(id=instance.purchaser.id).update(currency=F("currency") + purchase_amount)

### Разобраться до конца