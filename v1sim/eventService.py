# Copyright Notice:
# Copyright 2016 Distributed Management Task Force, Inc. All rights reserved.
# License: BSD 3-Clause License. For full text see link: https://github.com/DMTF/Redfish-Profile-Simulator/blob/master/LICENSE.md

import os

from .common_services import RfLogServiceCollection
from .network import RfEthernetCollection, RfNetworkInterfaceCollection
from .resource import RfResource, RfCollection
from .storage import RfSimpleStorageCollection, RfSmartStorage


class RfEventServiceCollection(RfCollection):
    def element_type(self):
        return RfEventServiceObj


class RfEventServiceObj(RfResource):
    def create_sub_objects(self, base_path, rel_path):
        resource_path = os.path.join(base_path, rel_path)
        contents = os.listdir(resource_path)
