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

from msrest.service_client import SDKClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from msrest.exceptions import HttpOperationError
from .operations.features_operations import FeaturesOperations
from .operations.examples_operations import ExamplesOperations
from .operations.model_operations import ModelOperations
from .operations.apps_operations import AppsOperations
from .operations.versions_operations import VersionsOperations
from .operations.train_operations import TrainOperations
from .operations.permissions_operations import PermissionsOperations
from .operations.pattern_operations import PatternOperations
from .operations.settings_operations import SettingsOperations
from .operations.azure_accounts_operations import AzureAccountsOperations
from . import models


class LUISAuthoringClientConfiguration(Configuration):
    """Configuration for LUISAuthoringClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param endpoint: Supported Cognitive Services endpoints (protocol and
     hostname, for example: https://westus.api.cognitive.microsoft.com).
    :type endpoint: str
    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    """

    def __init__(
            self, endpoint, credentials):

        if endpoint is None:
            raise ValueError("Parameter 'endpoint' must not be None.")
        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        base_url = '{Endpoint}/luis/api/v2.0'

        super(LUISAuthoringClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-cognitiveservices-language-luis/{}'.format(VERSION))

        self.endpoint = endpoint
        self.credentials = credentials


class LUISAuthoringClient(SDKClient):
    """LUISAuthoringClient

    :ivar config: Configuration for client.
    :vartype config: LUISAuthoringClientConfiguration

    :ivar features: Features operations
    :vartype features: azure.cognitiveservices.language.luis.authoring.operations.FeaturesOperations
    :ivar examples: Examples operations
    :vartype examples: azure.cognitiveservices.language.luis.authoring.operations.ExamplesOperations
    :ivar model: Model operations
    :vartype model: azure.cognitiveservices.language.luis.authoring.operations.ModelOperations
    :ivar apps: Apps operations
    :vartype apps: azure.cognitiveservices.language.luis.authoring.operations.AppsOperations
    :ivar versions: Versions operations
    :vartype versions: azure.cognitiveservices.language.luis.authoring.operations.VersionsOperations
    :ivar train: Train operations
    :vartype train: azure.cognitiveservices.language.luis.authoring.operations.TrainOperations
    :ivar permissions: Permissions operations
    :vartype permissions: azure.cognitiveservices.language.luis.authoring.operations.PermissionsOperations
    :ivar pattern: Pattern operations
    :vartype pattern: azure.cognitiveservices.language.luis.authoring.operations.PatternOperations
    :ivar settings: Settings operations
    :vartype settings: azure.cognitiveservices.language.luis.authoring.operations.SettingsOperations
    :ivar azure_accounts: AzureAccounts operations
    :vartype azure_accounts: azure.cognitiveservices.language.luis.authoring.operations.AzureAccountsOperations

    :param endpoint: Supported Cognitive Services endpoints (protocol and
     hostname, for example: https://westus.api.cognitive.microsoft.com).
    :type endpoint: str
    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    """

    def __init__(
            self, endpoint, credentials):

        self.config = LUISAuthoringClientConfiguration(endpoint, credentials)
        super(LUISAuthoringClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.features = FeaturesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.examples = ExamplesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.model = ModelOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.apps = AppsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.versions = VersionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.train = TrainOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.permissions = PermissionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.pattern = PatternOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.settings = SettingsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.azure_accounts = AzureAccountsOperations(
            self._client, self.config, self._serialize, self._deserialize)