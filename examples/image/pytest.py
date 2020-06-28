import openstack


# Initialize and turn on debug logging
openstack.enable_logging(debug=True)

# Initialize cloud
conn = openstack.connect(cloud='test_cloud')

for server in conn.compute.servers():
    print(server.to_dict())