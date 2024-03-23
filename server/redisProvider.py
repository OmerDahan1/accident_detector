from server import REDIS_CONNECTION


class RedisProvider:
    def __init__(self):
        self.r = REDIS_CONNECTION
        self.key = "license_plate_numbers"

    def add_license_plate_number(self, license_plate_numbers):
        self.r.sadd(self.key, *license_plate_numbers)

    def get_license_plate_numbers(self):
        byte_data = self.r.smembers(self.key)
        return [data.decode("utf-8") for data in byte_data]

    def flush_license_plate_numbers(self):
        self.r.delete(self.key)
