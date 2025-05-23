"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class LivePaper(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/LivePaper"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v4.0"

    properties = [
        Property(
            "authors",
            ["openminds.v4.core.Consortium", "openminds.v4.core.Organization", "openminds.v4.core.Person"],
            "author",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Creator of a literary or creative work, as well as a dataset publication.",
            instructions="Add all parties that contributed to this live paper as authors.",
        ),
        Property(
            "custodians",
            ["openminds.v4.core.Consortium", "openminds.v4.core.Organization", "openminds.v4.core.Person"],
            "custodian",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product.",
            instructions="Add all parties that fulfill the role of a custodian for this research product (e.g., a research group leader or principle investigator). Custodians are typically the main contact in case of misconduct, obtain permission from the contributors to publish personal information, and maintain the content and quality of the data, metadata, and/or code of the research product. Unless specified differently, this custodian will be responsible for all attached research product versions.",
        ),
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            required=True,
            description="Longer statement or account giving the characteristics of the live paper.",
            instructions="Enter a description (or abstract) of this research product. Note that this should be a suitable description for all attached research product versions.",
        ),
        Property(
            "digital_identifier",
            "openminds.v4.core.DOI",
            "digitalIdentifier",
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the globally unique and persistent digital identifier of this research product. Note that this digital identifier will be used to reference all attached research product versions.",
        ),
        Property(
            "full_name",
            str,
            "fullName",
            formatting="text/plain",
            required=True,
            description="Whole, non-abbreviated name of the live paper.",
            instructions="Enter a descriptive full name (or title) for this research product. Note that this should be a suitable full name for all attached research product versions.",
        ),
        Property(
            "has_versions",
            "openminds.v4.publications.LivePaperVersion",
            "hasVersion",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Reference to variants of an original.",
            instructions="Add all versions of this live paper.",
        ),
        Property(
            "homepage",
            IRI,
            "homepage",
            description="Main website of the live paper.",
            instructions="Enter the internationalized resource identifier (IRI) to the homepage of this research product.",
        ),
        Property(
            "how_to_cite",
            str,
            "howToCite",
            formatting="text/markdown",
            multiline=True,
            description="Preferred format for citing a particular object or legal person.",
            instructions="Enter the preferred citation text for this research product. Leave blank if citation text can be extracted from the assigned digital identifier.",
        ),
        Property(
            "short_name",
            str,
            "shortName",
            formatting="text/plain",
            required=True,
            description="Shortened or fully abbreviated name of the live paper.",
            instructions="Enter a short name (or alias) for this research product that could be used as a shortened display title (e.g., for web services with too little space to display the full name).",
        ),
    ]

    def __init__(
        self,
        id=None,
        authors=None,
        custodians=None,
        description=None,
        digital_identifier=None,
        full_name=None,
        has_versions=None,
        homepage=None,
        how_to_cite=None,
        short_name=None,
    ):
        return super().__init__(
            id=id,
            authors=authors,
            custodians=custodians,
            description=description,
            digital_identifier=digital_identifier,
            full_name=full_name,
            has_versions=has_versions,
            homepage=homepage,
            how_to_cite=how_to_cite,
            short_name=short_name,
        )
