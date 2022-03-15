import hazelcast

def connection():
    hazelcast.HazelcastClient(
        cluster_name="pr-3072",
        cloud_discovery_token="eVT8mT5NIUr3xHXJPqpvpemEYajXsE8T7PFD2XOoclLuqGgqwb",
        statistics_enabled=True,
    )
