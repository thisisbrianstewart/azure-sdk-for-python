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


class ManagementGroupChildInfo(Model):
    """The child information of a management group.

    :param type: The type of child resource. The fully qualified resource type
     which includes provider namespace (e.g.
     /providers/Microsoft.Management/managementGroups). Possible values
     include: '/providers/Microsoft.Management/managementGroups',
     '/subscriptions'
    :type type: str or ~azure.mgmt.managementgroups.models.enum
    :param id: The fully qualified ID for the child resource (management group
     or subscription).  For example,
     /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000
    :type id: str
    :param name: The name of the child entity.
    :type name: str
    :param display_name: The friendly name of the child resource.
    :type display_name: str
    :param roles: The roles definitions associated with the management group.
    :type roles: list[str]
    :param children: The list of children.
    :type children:
     list[~azure.mgmt.managementgroups.models.ManagementGroupChildInfo]
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'roles': {'key': 'roles', 'type': '[str]'},
        'children': {'key': 'children', 'type': '[ManagementGroupChildInfo]'},
    }

    def __init__(self, **kwargs):
        super(ManagementGroupChildInfo, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.display_name = kwargs.get('display_name', None)
        self.roles = kwargs.get('roles', None)
        self.children = kwargs.get('children', None)
