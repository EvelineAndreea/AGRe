# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class RefurbishedConditionSchema(SchemaObject):

    """Schema Mixin for RefurbishedCondition
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Indicates that the item is refurbished.
    """

    def __init__(self):
        self.schema = 'RefurbishedCondition'


# schema.org version 2.0
