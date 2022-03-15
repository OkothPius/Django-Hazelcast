from django.db import models
# from .views import personnel_map
import hazelcast
client = hazelcast.HazelcastClient(
    cluster_name="pr-3072",
    cloud_discovery_token="eVT8mT5NIUr3xHXJPqpvpemEYajXsE8T7PFD2XOoclLuqGgqwb",
    statistics_enabled=True,
)
personnel_map = client.get_map("personnel-map").blocking()

class Customer(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.key}'

    # @classmethod
    # def get_val(value, key):
    #     key, value in personnel_map.entry_set()

class Client(models.Model):
    value = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.key}'
