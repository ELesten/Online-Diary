from django.db.models import signals, F
from django.dispatch import receiver
from apps.homeworks.models import Homework
from .models import CustomUser


@receiver(signals.post_save, sender=Homework)
def currency_accrual(instance, **kwargs):
    if instance.homework_status == 'Completed' and instance.connection_with_task.deadline < instance.created_at:
        CustomUser.objects.filter(id=instance.author.id).update(currency=F("currency") + 200)
    else:
        pass
