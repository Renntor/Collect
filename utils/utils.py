import hashlib
from functools import wraps
from typing import Callable

from django.core.cache import cache
from rest_framework.response import Response


class BaseService:
    @staticmethod
    def generate_cache_key(key: str) -> str:
        """Генерирует хешированный ключ для кэша."""
        return hashlib.md5(key.strip().lower().encode()).hexdigest()

    @staticmethod
    def cache_response_decorator(
            generate_cache_key_func: Callable[..., str],
            timeout: int = 3600
    ):
        """
        Декоратор для кеширования ответа с возможностью ручной генерации ключа.
        """

        def decorator(func):
            @wraps(func)
            def wrapped(self, request, *args, **kwargs):
                cache_key = generate_cache_key_func(
                    self, request, *args, **kwargs
                )
                cached_data = cache.get(cache_key)

                if cached_data is not None:
                    return Response(cached_data)

                response = func(self, request, *args, **kwargs)

                cache.set(cache_key, response.data, timeout)

                return response

            return wrapped

        return decorator
