# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, producerProp, creatorProp, publishingPrinciplesProp, textProp, citationProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, mainEntityProp, accessibilityFeatureProp, interactivityTypeProp, publicationProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, characterProp, contentRatingProp, hasPartProp, exampleOfWorkProp, editorProp, providerProp, isPartOfProp, recordedAtProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, translatorProp, offersProp, copyrightHolderProp, releasedEventProp, positionProp, genreProp, schemaVersionProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, licenseProp, aggregateRatingProp, workExampleProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class SoftwareApplicationSchema(SchemaObject):

    """Schema Mixin for SoftwareApplication
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A software application.
    """

    def __init__(self):
        self.schema = 'SoftwareApplication'


class screenshotProp(SchemaProperty):

    """
    SchemaField for screenshot
    Usage: Include in SchemaObject SchemaFields as your_django_field = screenshotProp()  
    schema.org description:A link to a screenshot image of the app.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference ImageObject"""

    _prop_schema = 'screenshot'
    _expected_schema = 'ImageObject'
    _enum = False
    _format_as = "URLField"


class releaseNotesProp(SchemaProperty):

    """
    SchemaField for releaseNotes
    Usage: Include in SchemaObject SchemaFields as your_django_field = releaseNotesProp()  
    schema.org description:Description of what changed in this version.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'releaseNotes'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class memoryRequirementsProp(SchemaProperty):

    """
    SchemaField for memoryRequirements
    Usage: Include in SchemaObject SchemaFields as your_django_field = memoryRequirementsProp()  
    schema.org description:Minimum memory requirements.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'memoryRequirements'
    _expected_schema = None
    _enum = False
    _format_as = "URLField"


class processorRequirementsProp(SchemaProperty):

    """
    SchemaField for processorRequirements
    Usage: Include in SchemaObject SchemaFields as your_django_field = processorRequirementsProp()  
    schema.org description:Processor architecture required to run the application (e.g. IA64).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'processorRequirements'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class softwareAddOnProp(SchemaProperty):

    """
    SchemaField for softwareAddOn
    Usage: Include in SchemaObject SchemaFields as your_django_field = softwareAddOnProp()  
    schema.org description:Additional content for a software application.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference SoftwareApplication"""

    _prop_schema = 'softwareAddOn'
    _expected_schema = 'SoftwareApplication'
    _enum = False
    _format_as = "ForeignKey"


class storageRequirementsProp(SchemaProperty):

    """
    SchemaField for storageRequirements
    Usage: Include in SchemaObject SchemaFields as your_django_field = storageRequirementsProp()  
    schema.org description:Storage requirements (free space required).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'storageRequirements'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class featureListProp(SchemaProperty):

    """
    SchemaField for featureList
    Usage: Include in SchemaObject SchemaFields as your_django_field = featureListProp()  
    schema.org description:Features or modules provided by this application (and possibly required by other applications).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'featureList'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class availableOnDeviceProp(SchemaProperty):

    """
    SchemaField for availableOnDevice
    Usage: Include in SchemaObject SchemaFields as your_django_field = availableOnDeviceProp()  
    schema.org description:Device required to run the application. Used in cases where a specific make/model is required to run the application. Supersedes device.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'availableOnDevice'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class applicationSubCategoryProp(SchemaProperty):

    """
    SchemaField for applicationSubCategory
    Usage: Include in SchemaObject SchemaFields as your_django_field = applicationSubCategoryProp()  
    schema.org description:Subcategory of the application, e.g. &quot;Arcade Game&quot;.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'applicationSubCategory'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class fileFormatProp(SchemaProperty):

    """
    SchemaField for fileFormat
    Usage: Include in SchemaObject SchemaFields as your_django_field = fileFormatProp()  
    schema.org description:MIME format of the binary (e.g. application/zip).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'fileFormat'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class applicationSuiteProp(SchemaProperty):

    """
    SchemaField for applicationSuite
    Usage: Include in SchemaObject SchemaFields as your_django_field = applicationSuiteProp()  
    schema.org description:The name of the application suite to which the application belongs (e.g. Excel belongs to Office).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'applicationSuite'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class permissionsProp(SchemaProperty):

    """
    SchemaField for permissions
    Usage: Include in SchemaObject SchemaFields as your_django_field = permissionsProp()  
    schema.org description:Permission(s) required to run the app (for example, a mobile app may require full internet access or may run only on wifi).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'permissions'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class softwareHelpProp(SchemaProperty):

    """
    SchemaField for softwareHelp
    Usage: Include in SchemaObject SchemaFields as your_django_field = softwareHelpProp()  
    schema.org description:Software application help.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference CreativeWork"""

    _prop_schema = 'softwareHelp'
    _expected_schema = 'CreativeWork'
    _enum = False
    _format_as = "ForeignKey"


class countriesNotSupportedProp(SchemaProperty):

    """
    SchemaField for countriesNotSupported
    Usage: Include in SchemaObject SchemaFields as your_django_field = countriesNotSupportedProp()  
    schema.org description:Countries for which the application is not supported. You can also provide the two-letter ISO 3166-1 alpha-2 country code.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'countriesNotSupported'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class installUrlProp(SchemaProperty):

    """
    SchemaField for installUrl
    Usage: Include in SchemaObject SchemaFields as your_django_field = installUrlProp()  
    schema.org description:URL at which the app may be installed, if different from the URL of the item.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference URL"""

    _prop_schema = 'installUrl'
    _expected_schema = 'URL'
    _enum = False
    _format_as = "ForeignKey"


class fileSizeProp(SchemaProperty):

    """
    SchemaField for fileSize
    Usage: Include in SchemaObject SchemaFields as your_django_field = fileSizeProp()  
    schema.org description:Size of the application / package (e.g. 18MB). In the absence of a unit (MB, KB etc.), KB will be assumed.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Integer"""

    _prop_schema = 'fileSize'
    _expected_schema = 'Integer'
    _enum = False
    _format_as = "ForeignKey"


class countriesSupportedProp(SchemaProperty):

    """
    SchemaField for countriesSupported
    Usage: Include in SchemaObject SchemaFields as your_django_field = countriesSupportedProp()  
    schema.org description:Countries for which the application is supported. You can also provide the two-letter ISO 3166-1 alpha-2 country code.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'countriesSupported'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class downloadUrlProp(SchemaProperty):

    """
    SchemaField for downloadUrl
    Usage: Include in SchemaObject SchemaFields as your_django_field = downloadUrlProp()  
    schema.org description:If the file can be downloaded, URL to download the binary.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference URL"""

    _prop_schema = 'downloadUrl'
    _expected_schema = 'URL'
    _enum = False
    _format_as = "ForeignKey"


class applicationCategoryProp(SchemaProperty):

    """
    SchemaField for applicationCategory
    Usage: Include in SchemaObject SchemaFields as your_django_field = applicationCategoryProp()  
    schema.org description:Type of software application, e.g. &quot;Game, Multimedia&quot;.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'applicationCategory'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class softwareVersionProp(SchemaProperty):

    """
    SchemaField for softwareVersion
    Usage: Include in SchemaObject SchemaFields as your_django_field = softwareVersionProp()  
    schema.org description:Version of the software instance.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'softwareVersion'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class operatingSystemProp(SchemaProperty):

    """
    SchemaField for operatingSystem
    Usage: Include in SchemaObject SchemaFields as your_django_field = operatingSystemProp()  
    schema.org description:Operating systems supported (Windows 7, OSX 10.6, Android 1.6).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'operatingSystem'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class softwareRequirementsProp(SchemaProperty):

    """
    SchemaField for softwareRequirements
    Usage: Include in SchemaObject SchemaFields as your_django_field = softwareRequirementsProp()  
    schema.org description:Component dependency requirements for application. This includes runtime environments and shared libraries that are not included in the application distribution package, but required to run the application (Examples: DirectX, Java or .NET runtime). Supersedes requirements.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'softwareRequirements'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
