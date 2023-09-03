from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'stacticmedia' # Must be replaced by your <storage_account_name>
    account_key = 'areR2+3aN5LhkFkW21X7njFNXFA7Q62XAubt+Peni/i/n1UODzmLy43lxNQ9el+UhzKgceiJH275+AStlcKA8g==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'stacticmedia' # Must be replaced by your storage_account_name
    account_key = 'areR2+3aN5LhkFkW21X7njFNXFA7Q62XAubt+Peni/i/n1UODzmLy43lxNQ9el+UhzKgceiJH275+AStlcKA8g==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None