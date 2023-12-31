from pulumi_azure.appservice import Plan, PlanSkuArgs
from pulumi_azure.core import ResourceGroup
from pulumi_azure.storage import Account, Container
from pulumi import Config, ResourceOptions, export

from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient

config = Config("azure")
location = config.get("location") or "West Europe"

def setup_azure_console():
    resource_group_name = "resourcegroupconsole"
    storage_account_name = "storageaccfaasconsole"
    storage_container_name = "storagecontainerconsole"

    app_service_plan = Plan("appserviceplan",
                            name="appserviceplan",
                            resource_group_name=resource_group_name,
                            location=location,
                            kind="FunctionApp",
                            reserved=True,

                            sku=PlanSkuArgs(
                                tier="Dynamic",
                                size="Y1",
                            ),
                            opts=ResourceOptions(protect=False)
                            )
    return {
        "app_service_plan": app_service_plan,
        "resource_group_name": resource_group_name,
        "storage_account_name": storage_account_name,
        "storage_container_name": storage_container_name
        }

def setup_azure():
    resource_group_name = "resourcegroup"
    storage_account_name = "storageaccountfaasmonad"

    resource_group = ResourceGroup(resource_group_name,
                                   name=resource_group_name,
                                   location=location,
                                   opts=ResourceOptions(protect=False)
                                   )

    storage_account = Account(storage_account_name,
                              name=storage_account_name,
                              resource_group_name=resource_group.name,
                              location=resource_group.location,
                              account_tier="Standard",
                              account_replication_type="LRS",
                              opts=ResourceOptions(protect=False)
                              )

    storage_container = Container("storagecontainer",
                                  name="storagecontainer",
                                  storage_account_name=storage_account.name,
                                  container_access_type="private",
                                  opts=ResourceOptions(protect=False)
                                  )

    app_service_plan = Plan("appserviceplan",
                            name="appserviceplan",
                            resource_group_name=resource_group.name,
                            location=resource_group.location,
                            kind="FunctionApp",
                            reserved=True,

                            sku=PlanSkuArgs(
                                tier="Dynamic",
                                size="Y1",
                            ),
                            opts=ResourceOptions(protect=False)
                            )
    export("resource_group_name", resource_group.name)
    export("storage_account_name", storage_account.name)
    export("storage_account_primary_key", storage_account.primary_access_key)
    export("storage_account_connection_string", storage_account.primary_connection_string)
    export("app_service_plan_id", app_service_plan.id)
    export("location", resource_group.location)


    return {"resource_group": resource_group,
            "storage_account": storage_account,
            "storage_container": storage_container,
            "app_service_plan": app_service_plan,
            }

