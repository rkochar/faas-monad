from pulumi import ResourceOptions, Input, Output

from pulumi_azure_native import storage, resources


def merge_opts(opts1: ResourceOptions, opts2: ResourceOptions):
    if opts1 is None and opts2 is None:
        return None
    elif opts1 is None:
        return opts2
    elif opts2 is None:
        return opts1
    return ResourceOptions.merge(opts1, opts2)


def get_connection_string(resource_group, account):
    # Retrieve the primary storage account key.
    storage_account_keys = Output.all(resource_group.name, account.name).apply(lambda args:  storage.list_storage_account_keys(resource_group_name=args[0],account_name=args[1]))

    primary_storage_key = storage_account_keys.apply(lambda accountKeys: accountKeys.keys[0].value)

    # Build the connection string to the storage account.
    return Output.concat("DefaultEndpointsProtocol=https;AccountName=",
                         account.name,
                         ";AccountKey=",
                         primary_storage_key
                         )


def signed_blob_read_url(blob_name, container_name, account_name, resource_group_name):
    blob_sas = storage.list_storage_account_service_sas(account_name=account_name,
                                                        resource_group_name=resource_group_name,
                                                        protocols=storage.HttpProtocol.HTTPS,
                                                        shared_access_expiry_time="2030-01-01",
                                                        shared_access_start_time="2021-01-01",
                                                        resource=storage.SignedResource.C,
                                                        permissions=storage.Permissions.R,
                                                        canonicalized_resource=f"/blob/{account_name}/{container_name}",
                                                        content_type="application/json",
                                                        cache_control="max-age=5",
                                                        content_disposition="inline",
                                                        content_encoding="deflate")
    return Output.concat("https://", account_name,
                         ".blob.core.windows.net/",
                         container_name, "/", blob_name, "?", blob_sas.service_sas_token)
