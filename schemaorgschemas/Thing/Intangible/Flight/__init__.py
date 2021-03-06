# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class FlightSchema(SchemaObject):

    """Schema Mixin for Flight
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An airline flight.
    """

    def __init__(self):
        self.schema = 'Flight'


class flightDistanceProp(SchemaProperty):

    """
    SchemaField for flightDistance
    Usage: Include in SchemaObject SchemaFields as your_django_field = flightDistanceProp()  
    schema.org description:The distance of the flight.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'flightDistance'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class departureTimeProp(SchemaProperty):

    """
    SchemaField for departureTime
    Usage: Include in SchemaObject SchemaFields as your_django_field = departureTimeProp()  
    schema.org description:The expected departure time.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'departureTime'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"


class arrivalTerminalProp(SchemaProperty):

    """
    SchemaField for arrivalTerminal
    Usage: Include in SchemaObject SchemaFields as your_django_field = arrivalTerminalProp()  
    schema.org description:Identifier of the flight&#39;s arrival terminal.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'arrivalTerminal'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class mealServiceProp(SchemaProperty):

    """
    SchemaField for mealService
    Usage: Include in SchemaObject SchemaFields as your_django_field = mealServiceProp()  
    schema.org description:Description of the meals that will be provided or available for purchase.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'mealService'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class boardingPolicyProp(SchemaProperty):

    """
    SchemaField for boardingPolicy
    Usage: Include in SchemaObject SchemaFields as your_django_field = boardingPolicyProp()  
    schema.org description:The type of boarding policy used by the airline (e.g. zone-based or group-based).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference BoardingPolicyType"""

    _prop_schema = 'boardingPolicy'
    _expected_schema = 'BoardingPolicyType'
    _enum = False
    _format_as = "ForeignKey"


class providerProp(SchemaProperty):

    """
    SchemaField for provider
    Usage: Include in SchemaObject SchemaFields as your_django_field = providerProp()  
    schema.org description:The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller. Supersedes carrier.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'provider'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class webCheckinTimeProp(SchemaProperty):

    """
    SchemaField for webCheckinTime
    Usage: Include in SchemaObject SchemaFields as your_django_field = webCheckinTimeProp()  
    schema.org description:The time when a passenger can check into the flight online.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference DateTime"""

    _prop_schema = 'webCheckinTime'
    _expected_schema = 'DateTime'
    _enum = False
    _format_as = "ForeignKey"


class flightNumberProp(SchemaProperty):

    """
    SchemaField for flightNumber
    Usage: Include in SchemaObject SchemaFields as your_django_field = flightNumberProp()  
    schema.org description:The unique identifier for a flight including the airline IATA code. For example, if describing United flight 110, where the IATA code for United is &#39;UA&#39;, the flightNumber is &#39;UA110&#39;.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'flightNumber'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class sellerProp(SchemaProperty):

    """
    SchemaField for seller
    Usage: Include in SchemaObject SchemaFields as your_django_field = sellerProp()  
    schema.org description:An entity which offers (sells / leases / lends / loans) the services / goods. A seller may also be a provider. Supersedes vendor, merchant.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'seller'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class departureAirportProp(SchemaProperty):

    """
    SchemaField for departureAirport
    Usage: Include in SchemaObject SchemaFields as your_django_field = departureAirportProp()  
    schema.org description:The airport where the flight originates.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Airport"""

    _prop_schema = 'departureAirport'
    _expected_schema = 'Airport'
    _enum = False
    _format_as = "ForeignKey"


class aircraftProp(SchemaProperty):

    """
    SchemaField for aircraft
    Usage: Include in SchemaObject SchemaFields as your_django_field = aircraftProp()  
    schema.org description:The kind of aircraft (e.g., &quot;Boeing 747&quot;).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'aircraft'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class estimatedFlightDurationProp(SchemaProperty):

    """
    SchemaField for estimatedFlightDuration
    Usage: Include in SchemaObject SchemaFields as your_django_field = estimatedFlightDurationProp()  
    schema.org description:The estimated time the flight will take.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'estimatedFlightDuration'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class departureGateProp(SchemaProperty):

    """
    SchemaField for departureGate
    Usage: Include in SchemaObject SchemaFields as your_django_field = departureGateProp()  
    schema.org description:Identifier of the flight&#39;s departure gate.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'departureGate'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class departureTerminalProp(SchemaProperty):

    """
    SchemaField for departureTerminal
    Usage: Include in SchemaObject SchemaFields as your_django_field = departureTerminalProp()  
    schema.org description:Identifier of the flight&#39;s departure terminal.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'departureTerminal'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class arrivalTimeProp(SchemaProperty):

    """
    SchemaField for arrivalTime
    Usage: Include in SchemaObject SchemaFields as your_django_field = arrivalTimeProp()  
    schema.org description:The expected arrival time.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'arrivalTime'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"


class arrivalGateProp(SchemaProperty):

    """
    SchemaField for arrivalGate
    Usage: Include in SchemaObject SchemaFields as your_django_field = arrivalGateProp()  
    schema.org description:Identifier of the flight&#39;s arrival gate.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'arrivalGate'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class arrivalAirportProp(SchemaProperty):

    """
    SchemaField for arrivalAirport
    Usage: Include in SchemaObject SchemaFields as your_django_field = arrivalAirportProp()  
    schema.org description:The airport where the flight terminates.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Airport"""

    _prop_schema = 'arrivalAirport'
    _expected_schema = 'Airport'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
