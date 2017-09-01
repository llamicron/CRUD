servers = [
    {
        "username": "pi",
        "ip": "165.123.1258.28",
        "name": "brewpi-test",
        "location": "Texas A&M"
    },
    {
        "username": "pi",
        "ip": "192.168.0.134",
        "name": "sween",
        "location": "Dining Room"
    },
    # This one doesn't have a location for testing purposes. It's not required.
    # Don't delete the field, just leave it empty
    {
        "username": "luke",
        "ip": "192.168.0.123",
        "name": "No location",
        "location": ""
    },
    {
        "username": "pi",
        "ip": "192.168.0.169",
        "name": "brewpi-prod",
        "location": "Brew Rig"
    },
    {
        "username": "llamicron",
        "ip": "192.168.0.134",
        "name": "llaminator",
        "location": "Bedroom"
    }
]

# Invalid servers
bad_servers = [
    {
        "username": "luke",
        "ip": "",
        "name": "No location",
        "location": ""
    },
    {
        "username": "",
        "ip": "192.168.0.123",
        "name": "No location",
        "location": "Right over there"
    },
]

# These are servers that won't get put in the testing file
# For testing adding and removing servers
extra_servers = [
    {
        "name": "extra",
        "username": "pi",
        "ip": "190.213.48.34",
        "location": ""
    }
]
