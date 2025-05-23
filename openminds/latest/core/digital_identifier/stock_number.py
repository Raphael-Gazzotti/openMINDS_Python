"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class StockNumber(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/StockNumber"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "identifier",
            str,
            "identifier",
            formatting="text/plain",
            required=True,
            description="Term or code used to identify the stock number.",
            instructions="Enter the stock number of an item provided by a store or company.",
        ),
        Property(
            "vendor",
            "openminds.latest.core.Organization",
            "vendor",
            required=True,
            description="no description available",
            instructions="Add the vendor that has the item with this identifier in stock.",
        ),
    ]

    def __init__(self, identifier=None, vendor=None):
        return super().__init__(
            identifier=identifier,
            vendor=vendor,
        )
