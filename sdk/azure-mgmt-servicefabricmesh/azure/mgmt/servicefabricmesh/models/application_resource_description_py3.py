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

from .tracked_resource_py3 import TrackedResource


class ApplicationResourceDescription(TrackedResource):
    """This type describes an application resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified identifier for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives
    :type location: str
    :ivar provisioning_state: State of the resource.
    :vartype provisioning_state: str
    :param description: User readable description of the application.
    :type description: str
    :param services: Describes the services in the application. This property
     is used to create or modify services of the application. On get only the
     name of the service is returned. The service description can be obtained
     by querying for the service resource.
    :type services:
     list[~azure.mgmt.servicefabricmesh.models.ServiceResourceDescription]
    :param diagnostics: Describes the diagnostics definition and usage for an
     application resource.
    :type diagnostics:
     ~azure.mgmt.servicefabricmesh.models.DiagnosticsDescription
    :param debug_params: Internal - used by Visual Studio to setup the
     debugging session on the local development environment.
    :type debug_params: str
    :ivar service_names: Names of the services in the application.
    :vartype service_names: list[str]
    :ivar status: Status of the application. Possible values include:
     'Unknown', 'Ready', 'Upgrading', 'Creating', 'Deleting', 'Failed'
    :vartype status: str or
     ~azure.mgmt.servicefabricmesh.models.ResourceStatus
    :ivar status_details: Gives additional information about the current
     status of the application.
    :vartype status_details: str
    :ivar health_state: Describes the health state of an application resource.
     Possible values include: 'Invalid', 'Ok', 'Warning', 'Error', 'Unknown'
    :vartype health_state: str or
     ~azure.mgmt.servicefabricmesh.models.HealthState
    :ivar unhealthy_evaluation: When the application's health state is not
     'Ok', this additional details from service fabric Health Manager for the
     user to know why the application is marked unhealthy.
    :vartype unhealthy_evaluation: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'provisioning_state': {'readonly': True},
        'service_names': {'readonly': True},
        'status': {'readonly': True},
        'status_details': {'readonly': True},
        'health_state': {'readonly': True},
        'unhealthy_evaluation': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'services': {'key': 'properties.services', 'type': '[ServiceResourceDescription]'},
        'diagnostics': {'key': 'properties.diagnostics', 'type': 'DiagnosticsDescription'},
        'debug_params': {'key': 'properties.debugParams', 'type': 'str'},
        'service_names': {'key': 'properties.serviceNames', 'type': '[str]'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'status_details': {'key': 'properties.statusDetails', 'type': 'str'},
        'health_state': {'key': 'properties.healthState', 'type': 'str'},
        'unhealthy_evaluation': {'key': 'properties.unhealthyEvaluation', 'type': 'str'},
    }

    def __init__(self, *, location: str, tags=None, description: str=None, services=None, diagnostics=None, debug_params: str=None, **kwargs) -> None:
        super(ApplicationResourceDescription, self).__init__(tags=tags, location=location, **kwargs)
        self.provisioning_state = None
        self.description = description
        self.services = services
        self.diagnostics = diagnostics
        self.debug_params = debug_params
        self.service_names = None
        self.status = None
        self.status_details = None
        self.health_state = None
        self.unhealthy_evaluation = None
