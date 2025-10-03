class PaymentConstants:
    class Lengths:
        MIN_VALUE_AMOUNT = 1

    class Cache:
        class Payment:
            KEY = 'payment_list_{search}'
            LIFETIME = 3600

    class Pagination:
        class Payment:
            PAGE_SIZE = 10
            MAX_PAGE_SIZE = 100
