from django.db import models
# import hazelcast
#
# client = hazelcast.HazelcastClient(
#     cluster_name="pr-3072",
#     cloud_discovery_token="o6TcbFzG7dFi0oReJ6f3rESCufkRxCf4rxvNEodGOnrgyj8u7Q",
#     statistics_enabled=True,
# )
# personnel_map = client.get_map("personnel-map").blocking()

class Employee(models.Model):
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


client.shutdown()
