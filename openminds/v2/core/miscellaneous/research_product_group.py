"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class ResearchProductGroup(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/core/ResearchProductGroup"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v2.0"

    properties = [
        Property(
            "context",
            str,
            "context",
            formatting="text/plain",
            required=True,
            description="no description available",
            instructions="Enter the common context for this research product group.",
        ),
        Property(
            "has_parts",
            [
                "openminds.v2.core.Dataset",
                "openminds.v2.core.DatasetVersion",
                "openminds.v2.core.MetaDataModel",
                "openminds.v2.core.MetaDataModelVersion",
                "openminds.v2.core.Model",
                "openminds.v2.core.ModelVersion",
                "openminds.v2.core.Software",
                "openminds.v2.core.SoftwareVersion",
                "openminds.v2.core.WebService",
                "openminds.v2.core.WebServiceVersion",
                "openminds.v2.sands.BrainAtlas",
                "openminds.v2.sands.BrainAtlasVersion",
                "openminds.v2.sands.CommonCoordinateSpace",
                "openminds.v2.sands.CommonCoordinateSpaceVersion",
            ],
            "hasPart",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="no description available",
            instructions="Add all research products (research product versions) that should be grouped under the given 'context'.",
        ),
    ]

    def __init__(self, id=None, context=None, has_parts=None):
        return super().__init__(
            id=id,
            context=context,
            has_parts=has_parts,
        )
