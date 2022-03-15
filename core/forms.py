from django import forms
from django.forms import ModelForm
from .models import Customer, Client

import hazelcast
client = hazelcast.HazelcastClient(
    cluster_name="pr-3072",
    cloud_discovery_token="eVT8mT5NIUr3xHXJPqpvpemEYajXsE8T7PFD2XOoclLuqGgqwb",
    statistics_enabled=True,
)
personnel_map = client.get_map("personnel-map").blocking()

# Using a Queue in Hazelcast
queue = client.get_queue("queue").blocking()

# from core.views import personnel_map

class CustomerForm(forms.ModelForm):
    key = forms.CharField(max_length=100)
    value = forms.CharField(max_length=100)

    class Meta:
        model = Customer
        fields = ('key', 'value')


    def save(self, POST):
        context_dict = {}
        for key, value in personnel_map.entry_set():
            personnel_map.put(key=POST['value'], value=POST['key'])
            context_dict[key] = value


class ClientForm(forms.ModelForm):
    value = forms.CharField(max_length=100)

    class Meta:
        model = Client
        fields = ('value',)

    def save(self, POST):
        context_dict = {}
        for key in queue.take():
            queue.offer(key=POST['key'])
        context_dict[key] = key
