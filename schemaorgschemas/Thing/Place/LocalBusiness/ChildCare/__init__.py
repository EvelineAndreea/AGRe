# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Place.LocalBusiness import currenciesAcceptedProp, openingHoursProp, paymentAcceptedProp, priceRangeProp, parentOrganizationProp
from schemaorgschemas.Thing.Place import isicV4Prop, openingHoursSpecificationProp, photoProp, reviewProp, telephoneProp, containedInProp, faxNumberProp, hasMapProp, aggregateRatingProp, additionalPropertyProp, addressProp, logoProp, geoProp, eventProp, globalLocationNumberProp
from schemaorgschemas.Thing.Organization import founderProp, foundingDateProp, telephoneProp, faxNumberProp, aggregateRatingProp, logoProp, eventProp, isicV4Prop, reviewProp, taxIDProp, memberProp, foundingLocationProp, locationProp, employeeProp, emailProp, seeksProp, numberOfEmployeesProp, subOrganizationProp, brandProp, ownsProp, awardProp, departmentProp, dissolutionDateProp, addressProp, dunsProp, contactPointProp, makesOfferProp, hasPOSProp, naicsProp, memberOfProp, legalNameProp, vatIDProp, globalLocationNumberProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ChildCareSchema(SchemaObject):

    """Schema Mixin for ChildCare
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A Childcare center.
    """

    def __init__(self):
        self.schema = 'ChildCare'


# schema.org version 2.0
