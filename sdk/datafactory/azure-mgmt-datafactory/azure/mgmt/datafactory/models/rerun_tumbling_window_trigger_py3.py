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

from .trigger_py3 import Trigger


class RerunTumblingWindowTrigger(Trigger):
    """Trigger that schedules pipeline reruns for all fixed time interval windows
    from a requested start time to requested end time.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param description: Trigger description.
    :type description: str
    :ivar runtime_state: Indicates if trigger is running or not. Updated when
     Start/Stop APIs are called on the Trigger. Possible values include:
     'Started', 'Stopped', 'Disabled'
    :vartype runtime_state: str or
     ~azure.mgmt.datafactory.models.TriggerRuntimeState
    :param annotations: List of tags that can be used for describing the
     trigger.
    :type annotations: list[object]
    :param type: Required. Constant filled by server.
    :type type: str
    :param parent_trigger: The parent trigger reference.
    :type parent_trigger: object
    :param requested_start_time: Required. The start time for the time period
     for which restatement is initiated. Only UTC time is currently supported.
    :type requested_start_time: datetime
    :param requested_end_time: Required. The end time for the time period for
     which restatement is initiated. Only UTC time is currently supported.
    :type requested_end_time: datetime
    :param max_concurrency: Required. The max number of parallel time windows
     (ready for execution) for which a rerun is triggered.
    :type max_concurrency: int
    """

    _validation = {
        'runtime_state': {'readonly': True},
        'type': {'required': True},
        'requested_start_time': {'required': True},
        'requested_end_time': {'required': True},
        'max_concurrency': {'required': True, 'maximum': 50, 'minimum': 1},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'description': {'key': 'description', 'type': 'str'},
        'runtime_state': {'key': 'runtimeState', 'type': 'str'},
        'annotations': {'key': 'annotations', 'type': '[object]'},
        'type': {'key': 'type', 'type': 'str'},
        'parent_trigger': {'key': 'typeProperties.parentTrigger', 'type': 'object'},
        'requested_start_time': {'key': 'typeProperties.requestedStartTime', 'type': 'iso-8601'},
        'requested_end_time': {'key': 'typeProperties.requestedEndTime', 'type': 'iso-8601'},
        'max_concurrency': {'key': 'typeProperties.maxConcurrency', 'type': 'int'},
    }

    def __init__(self, *, requested_start_time, requested_end_time, max_concurrency: int, additional_properties=None, description: str=None, annotations=None, parent_trigger=None, **kwargs) -> None:
        super(RerunTumblingWindowTrigger, self).__init__(additional_properties=additional_properties, description=description, annotations=annotations, **kwargs)
        self.parent_trigger = parent_trigger
        self.requested_start_time = requested_start_time
        self.requested_end_time = requested_end_time
        self.max_concurrency = max_concurrency
        self.type = 'RerunTumblingWindowTrigger'
