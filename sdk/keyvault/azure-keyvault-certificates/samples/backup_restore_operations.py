import time
import os
from azure.keyvault.certificates import CertificateClient, CertificatePolicy
from azure.keyvault.certificates._generated.v7_0.models import SecretProperties, IssuerParameters, \
    X509CertificateProperties, SubjectAlternativeNames, Trigger, Action, ActionType
from azure.keyvault.certificates._models import KeyProperties, LifetimeAction
from azure.identity import DefaultAzureCredential
from azure.core.exceptions import HttpResponseError

# ----------------------------------------------------------------------------------------------------------
# Prerequistes -
#
# 1. An Azure Key Vault-
#    https://docs.microsoft.com/en-us/azure/key-vault/quick-create-cli
#
#  2. Microsoft Azure Key Vault PyPI package -
#    https://pypi.python.org/pypi/azure-keyvault-certificates/
#
# 3. Microsoft Azure Identity package -
#    https://pypi.python.org/pypi/azure-identity/
#
# 4. Set Environment variables AZURE_CLIENT_ID, AZURE_TENANT_ID, AZURE_CLIENT_SECRET, VAULT_URL.
# How to do this - https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/keyvault/azure-keyvault-secrets#createget-credentials)
#
# ----------------------------------------------------------------------------------------------------------
# Sample - demonstrates the basic backup and restore operations on a vault(certificates) resource for Azure Key Vault
#
# 1. Create a certificate (create_certificate)
#
# 2. Backup a certificate (backup_certificate)
#
# 3. Delete a certificate (delete_certificate)
#
# 4. Restore a certificate (restore_certificate)
# ----------------------------------------------------------------------------------------------------------

def run_sample():
    # Instantiate a certificate client that will be used to call the service.
    # Notice that the client is using default Azure credentials.
    # To make default credentials work, ensure that environment variables 'AZURE_CLIENT_ID',
    # 'AZURE_CLIENT_SECRET' and 'AZURE_TENANT_ID' are set with the service principal credentials.
    VAULT_URL = os.environ["VAULT_URL"]
    credential = DefaultAzureCredential()
    client = CertificateClient(vault_url=VAULT_URL, credential=credential)
    try:

        print("\n1. Create Certificate")
        cert_name = 'yourCertificate'
        lifetime_actions = [LifetimeAction(
            lifetime_percentage=2,
            action_type=ActionType.email_contacts
        )]

        # Before creating your certificate, let's create the management policy for your certificate.
        # Here you specify the properties of the key, secret, and issuer backing your certificate,
        # the X509 component of your certificate, and any lifetime actions you would like to be taken
        # on your certificate
        cert_policy = CertificatePolicy(key_properties=KeyProperties(exportable=True,
                                                                     key_type='RSA',
                                                                     key_size=2048,
                                                                     reuse_key=False),
                                        content_type='application/x-pkcs12',
                                        issuer_name='Self',
                                        subject_name='CN=*.microsoft.com',
                                        san_dns_names=['onedrive.microsoft.com', 'xbox.microsoft.com'],
                                        validity_in_months=24,
                                        lifetime_actions=lifetime_actions
                                        )

        # Let's create a certificate for your key vault.
        # if the certificate already exists in the Key Vault, then a new version of the certificate is created.
        # A certificate operation is returned.
        certificate_operation = client.create_certificate(name=cert_name, policy=cert_policy)
        print("Certificate with name '{0}' created.".format(certificate_operation.name))

        # Backups are good to have, if in case certificates gets deleted accidentally.
        # For long term storage, it is ideal to write the backup to a file.
        print("\n2. Create a backup for an existing certificate")
        certificate_backup = client.backup_certificate(name=certificate_operation.name)
        print("Backup created for certificate with name '{0}'.".format(certificate_operation.name))

        # The storage account certificate is no longer in use, so you can delete it.
        client.delete_certificate(name=certificate_operation.name)

        # To ensure certificate is deleted on the server side.
        print("\nDeleting certificate...")
        time.sleep(20)
        print("Deleted Certificate with name '{0}'".format(certificate_operation.name))

        # In future, if the certificate is required again, we can use the backup value to restore it in the Key Vault.
        print("\n3. Restore the certificate using the backed up certificate bytes")
        certificate = client.restore_certificate(certificate_backup)
        print("Restored Certificate with name '{0}'".format(certificate.name))

    except HttpResponseError as e:
        print("\nrun_sample has caught an error. {0}".format(e.message))

    finally:
        print("\nrun_sample done")


if __name__ == "__main__":
    try:
        run_sample()

    except Exception as e:
        print("Top level Error: {0}".format(str(e)))