# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork.MediaObject import contentUrlProp, playerTypeProp, encodesCreativeWorkProp, productionCompanyProp, expiresProp, heightProp, encodingFormatProp, associatedArticleProp, requiresSubscriptionProp, uploadDateProp, durationProp, embedUrlProp, regionsAllowedProp, bitrateProp, widthProp, contentSizeProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, producerProp, creatorProp, publishingPrinciplesProp, textProp, citationProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, mainEntityProp, accessibilityFeatureProp, interactivityTypeProp, publicationProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, characterProp, contentRatingProp, hasPartProp, exampleOfWorkProp, editorProp, providerProp, isPartOfProp, recordedAtProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, translatorProp, offersProp, copyrightHolderProp, releasedEventProp, positionProp, genreProp, schemaVersionProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, licenseProp, aggregateRatingProp, workExampleProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ImageObjectSchema(SchemaObject):

    """Schema Mixin for ImageObject
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An image file.
    """

    def __init__(self):
        self.schema = 'ImageObject'


class captionProp(SchemaProperty):

    """
    SchemaField for caption
    Usage: Include in SchemaObject SchemaFields as your_django_field = captionProp()  
    schema.org description:The caption for this object.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'caption'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class exifDataProp(SchemaProperty):

    """
    SchemaField for exifData
    Usage: Include in SchemaObject SchemaFields as your_django_field = exifDataProp()  
    schema.org description:exif data for this object.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'exifData'
    _expected_schema = None
    _enum = False
    _format_as = "PropertyValueField"


class thumbnailProp(SchemaProperty):

    """
    SchemaField for thumbnail
    Usage: Include in SchemaObject SchemaFields as your_django_field = thumbnailProp()  
    schema.org description:Thumbnail image for an image or video.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference ImageObject"""

    _prop_schema = 'thumbnail'
    _expected_schema = 'ImageObject'
    _enum = False
    _format_as = "URLField"


class representativeOfPageProp(SchemaProperty):

    """
    SchemaField for representativeOfPage
    Usage: Include in SchemaObject SchemaFields as your_django_field = representativeOfPageProp()  
    schema.org description:Indicates whether this image is representative of the content of the page.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'representativeOfPage'
    _expected_schema = None
    _enum = False
    _format_as = "BooleanField"


# schema.org version 2.0
