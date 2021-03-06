# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PaperbackSchema(SchemaObject):

    """Schema Mixin for Paperback
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Book format: Paperback.
    """

    def __init__(self):
        self.schema = 'Paperback'


# schema.org version 2.0
