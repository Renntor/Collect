from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver

from payments.models import Payment

from .constatns import CollectConstants
from .models import Collect


@receiver(post_save, sender=Collect)
@receiver(post_save, sender=Payment)
def delete_cache_list_collect(sender, **kwargs):
    key = cache.keys(CollectConstants.Cache.Collect.KEY.format(search='*'))
    cache.delete_many(key)
