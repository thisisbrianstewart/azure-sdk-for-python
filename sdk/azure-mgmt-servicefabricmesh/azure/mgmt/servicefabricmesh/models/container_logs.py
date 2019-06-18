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


class ContainerLogs(Model):
    """Container logs.

    :param content: Container logs.
    :type content: str
    """

    _attribute_map = {
        'content': {'key': 'content', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ContainerLogs, self).__init__(**kwargs)
        self.content = kwargs.get('content', None)
