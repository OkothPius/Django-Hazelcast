import hazelcast
from django.shortcuts import render, redirect, reverse
from .forms import EmployeeForm, ClientForm

client = hazelcast.HazelcastClient(
    cluster_name="pr-3072",
    cloud_discovery_token="o6TcbFzG7dFi0oReJ6f3rESCufkRxCf4rxvNEodGOnrgyj8u7Q",
    statistics_enabled=True,
)

# Using a Map in Hazelcast
personnel_map = client.get_map("personnel-map").blocking()

# Reading data from Hazelcast Map
def get_map(request):
    context_dict = {}
    for key, value in personnel_map.entry_set():
        context_dict[key] = value
    context = {
        'entries': context_dict
    }
    return render(request, 'core/index.html', context)

# Writing data to Hazelcast Map
def put_map(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save(request.POST)
            return redirect('names')
    else:
        form = EmployeeForm()
    return render(request, 'core/details.html', {'form' : form})


# Using a Queue in Hazelcast
queue = client.get_queue("queue").blocking()

def get_queue(request):
    context = {
        'entries': queue.take()
    }
    return render(request, 'core/queue.html', context)

def put_queue(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save(request.POST)
            return redirect('names')
    else:
        form = ClientForm()
    return render(request, 'core/queue_details.html', {'form' : form})


def create_topic(request):
    def on_message(msg):
        ("Got message:", msg.message)

        topic = client.get_topic("topic").blocking()
        topic.add_listener(on_message)

        for i in range(10):
            context = topic.publish("Message " + str(i))

        return render(request, 'core/topic.html', context)


client.shutdown()
