# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ParcelServiceSchema(SchemaObject):

    """Schema Mixin for ParcelService
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A private parcel service as the delivery mode available for a certain offer.

    Commonly used values:

    http://purl.org/goodrelations/v1#DHL 
    http://purl.org/goodrelations/v1#FederalExpress 
    http://purl.org/goodrelations/v1#UPS 

    """

    def __init__(self):
        self.schema = 'ParcelService'


# schema.org version 2.0
