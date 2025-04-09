"""
Structured information about a short text expressing an opinion on, or giving information about some entity.
"""

# this file was auto-generated!

from datetime import datetime

from openminds.base import LinkedMetadata
from openminds.properties import Property


class Comment(LinkedMetadata):
    """
    Structured information about a short text expressing an opinion on, or giving information about some entity.
    """

    type_ = "https://openminds.ebrains.eu/core/Comment"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v1.0"

    properties = [
        Property(
            "about",
            [
                "openminds.v1.core.Dataset",
                "openminds.v1.core.DatasetVersion",
                "openminds.v1.core.MetaDataModel",
                "openminds.v1.core.MetaDataModelVersion",
                "openminds.v1.core.Model",
                "openminds.v1.core.ModelVersion",
                "openminds.v1.core.Software",
                "openminds.v1.core.SoftwareVersion",
                "openminds.v1.core.WebService",
                "openminds.v1.core.WebServiceVersion",
                "openminds.v1.sands.BrainAtlas",
                "openminds.v1.sands.BrainAtlasVersion",
                "openminds.v1.sands.CommonCoordinateSpace",
                "openminds.v1.sands.CommonCoordinateSpaceVersion",
            ],
            "about",
            required=True,
            description="no description available",
            instructions="Add the research product (version) that this comment is about.",
        ),
        Property(
            "comment",
            str,
            "comment",
            formatting="text/plain",
            multiline=True,
            required=True,
            description="no description available",
            instructions="Enter the comment about the research product (version) stated under 'about'.",
        ),
        Property(
            "commenter",
            "openminds.v1.core.Person",
            "commenter",
            required=True,
            description="no description available",
            instructions="Add the person that created this comment.",
        ),
        Property(
            "timestamp",
            datetime,
            "timestamp",
            required=True,
            description="no description available",
            instructions="Enter the date and time on which this comment was made, formatted as '2023-02-07T16:00:00+00:00'.",
        ),
    ]

    def __init__(self, id=None, about=None, comment=None, commenter=None, timestamp=None):
        return super().__init__(
            id=id,
            about=about,
            comment=comment,
            commenter=commenter,
            timestamp=timestamp,
        )
