# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" Playground gRPC service. """

from google.cloud.security.iam.inventory import inventory_pb2
from google.cloud.security.iam.inventory import inventory_pb2_grpc
from google.cloud.security.iam.inventory import inventory


# TODO: The next editor must remove this disable and correct issues.
# pylint: disable=missing-type-doc,missing-return-type-doc,missing-return-doc
# pylint: disable=missing-param-doc


# pylint: disable=no-self-use
class GrpcInventory(inventory_pb2_grpc.InventoryServicer):
    """Inventory gRPC handler."""

    def __init__(self, inventory_api):
        super(GrpcInventory, self).__init__()
        self.inventory = inventory_api

    def Ping(self, request, _):
        """Ping implemented to check service availability."""

        return inventory_pb2.PingReply(data=request.data)

    def Create(self, request, context):
        """Creates a new inventory."""

        raise NotImplementedError()

    def List(self, request, context):
        """Lists existing inventory."""

        raise NotImplementedError()

    def Get(self, request, context):
        """Gets existing inventory."""

        raise NotImplementedError()

    def Delete(self, request, context):
        """Deletes existing inventory."""

        raise NotImplementedError()


class GrpcInventoryFactory(object):
    """Factory class for Inventory service gRPC interface"""

    def __init__(self, config):
        self.config = config

    def create_and_register_service(self, server):
        """Creates an inventory service and registers it in the server"""

        service = GrpcInventory(
            playgrounder_api=inventory.Inventory(
                self.config))
        inventory_pb2_grpc.add_InventoryServicer_to_server(service, server)
        return service