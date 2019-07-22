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

from .resource_py3 import Resource


class Pricing(Resource):
    """Azure Security Center is provided in two pricing tiers: free and standard,
    with the standard tier available with a trial period. The standard tier
    offers advanced security capabilities, while the free tier offers basic
    security features.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param pricing_tier: Required. The pricing tier value. Azure Security
     Center is provided in two pricing tiers: free and standard, with the
     standard tier available with a trial period. The standard tier offers
     advanced security capabilities, while the free tier offers basic security
     features. Possible values include: 'Free', 'Standard'
    :type pricing_tier: str or ~azure.mgmt.security.models.PricingTier
    :ivar free_trial_remaining_time: The duration left for the subscriptions
     free trial period - in ISO 8601 format (e.g. P3Y6M4DT12H30M5S).
    :vartype free_trial_remaining_time: timedelta
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'pricing_tier': {'required': True},
        'free_trial_remaining_time': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'pricing_tier': {'key': 'properties.pricingTier', 'type': 'str'},
        'free_trial_remaining_time': {'key': 'properties.freeTrialRemainingTime', 'type': 'duration'},
    }

    def __init__(self, *, pricing_tier, **kwargs) -> None:
        super(Pricing, self).__init__(**kwargs)
        self.pricing_tier = pricing_tier
        self.free_trial_remaining_time = None
