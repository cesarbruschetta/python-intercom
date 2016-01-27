# -*- coding: utf-8 -*-

from intercom.api_operations.save import Save
from intercom.api_operations.find import Find
from intercom.traits.api_resource import Resource


class Contact(Resource, Save, Find):
    pass
