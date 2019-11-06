from azure.datalake.store import core, lib, multithread
from azure.common.credentials import ServicePrincipalCredentials

token = lib.auth(tenant_id = '<your azure tenant id>'
, client_secret = '<your client secret>'
, client_id = '<your client id>'
) # Dont save the script with the values, we will implement secrets in future.

token = lib.auth()

