"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class Rectangle(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/sands/Rectangle"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v2.0"

    properties = [
        Property(
            "length",
            "openminds.v2.core.QuantitativeValue",
            "length",
            required=True,
            description="no description available",
            instructions="Enter the length of this rectangle.",
        ),
        Property(
            "width",
            "openminds.v2.core.QuantitativeValue",
            "width",
            required=True,
            description="no description available",
            instructions="Enter the width of this rectangle.",
        ),
    ]

    def __init__(self, id=None, length=None, width=None):
        return super().__init__(
            id=id,
            length=length,
            width=width,
        )
