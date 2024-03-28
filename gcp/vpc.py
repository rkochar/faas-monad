from pulumi_gcp.compute import Network, Subnetwork
from pulumi_gcp.vpcaccess import Connector
from pulumi_gcp.servicenetworking import Connection
from pulumi import Config, ResourceOptions

config = Config("gcp")
region = config.require("region")

def create_vpc_and_subnet(name):
    vpc = Network(f"vpc-{name}",
                  auto_create_subnetworks=True
                  )
    subnet = None
    #subnet = Subnetwork(f"subnet-{name}",
    #                    ip_cidr_range="10.0.0.0/24",
    #                    region=region,
    #                    network=vpc.self_link,
    #                    private_ip_google_access=True
    #                    )
    #vpc_connection = Connection("vpc-connection",
    #    network=vpc,
    #    reserved_peering_ranges=[reserved_range_name],
    #    service="servicenetworking.googleapis.com"
    #)

    connector = Connector(f'vpcconnector{name.replace("-", "")}',
                          ip_cidr_range="10.0.0.0/24",
                          network="default"
                          )
    return vpc, subnet, connector
