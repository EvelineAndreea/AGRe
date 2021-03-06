# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Organization import founderProp, foundingDateProp, telephoneProp, faxNumberProp, aggregateRatingProp, logoProp, eventProp, isicV4Prop, reviewProp, taxIDProp, memberProp, foundingLocationProp, locationProp, employeeProp, emailProp, seeksProp, numberOfEmployeesProp, subOrganizationProp, brandProp, ownsProp, awardProp, departmentProp, dissolutionDateProp, addressProp, dunsProp, contactPointProp, makesOfferProp, hasPOSProp, naicsProp, memberOfProp, legalNameProp, vatIDProp, globalLocationNumberProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class EducationalOrganizationSchema(SchemaObject):

    """Schema Mixin for EducationalOrganization
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An educational organization.
    """

    def __init__(self):
        self.schema = 'EducationalOrganization'


class alumniProp(SchemaProperty):

    """
    SchemaField for alumni
    Usage: Include in SchemaObject SchemaFields as your_django_field = alumniProp()  
    schema.org description:Alumni of educational organization. Inverse property: alumniOf.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'alumni'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
