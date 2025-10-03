from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver

from .constatns import PaymentConstants
from .models import Payment


@receiver(post_save, sender=Payment)
def delete_cache_list_payment(sender, **kwargs):
    key = cache.keys(PaymentConstants.Cache.Payment.KEY.format(search='*'))
    cache.delete_many(key)
