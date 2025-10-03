class CollectConstants:
    class Lengths:
        MIN_LENGTH_NAME = 1
        MAX_LENGTH_NAME = 254
        MIN_VALUE_TARGET_AMOUNT = 1
        MIN_VALUE_TOTAL_GOAL_AMOUNT = 1
        MAX_LENGTH_REASON = 30

    class Cache:
        class Collect:
            KEY = 'collect_list_{search}'
            LIFETIME = 3600

    class Pagination:
        class Collect:
            PAGE_SIZE = 10
            MAX_PAGE_SIZE = 100
