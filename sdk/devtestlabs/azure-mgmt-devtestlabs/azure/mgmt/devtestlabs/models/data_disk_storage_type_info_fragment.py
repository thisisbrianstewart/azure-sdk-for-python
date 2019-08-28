# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DataDiskStorageTypeInfoFragment(Model):
    """Storage information about the data disks present in the custom image.

    :param lun: Disk Lun
    :type lun: str
    :param storage_type: Disk Storage Type. Possible values include:
     'Standard', 'Premium'
    :type storage_type: str or ~azure.mgmt.devtestlabs.models.StorageType
    """

    _attribute_map = {
        'lun': {'key': 'lun', 'type': 'str'},
        'storage_type': {'key': 'storageType', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DataDiskStorageTypeInfoFragment, self).__init__(**kwargs)
        self.lun = kwargs.get('lun', None)
        self.storage_type = kwargs.get('storage_type', None)