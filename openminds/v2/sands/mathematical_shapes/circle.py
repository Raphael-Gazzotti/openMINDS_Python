"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class Circle(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/sands/Circle"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v2.0"

    properties = [
        Property(
            "radius",
            "openminds.v2.core.QuantitativeValue",
            "radius",
            required=True,
            description="no description available",
            instructions="Enter the radius of this circle.",
        ),
    ]

    def __init__(self, id=None, radius=None):
        return super().__init__(
            id=id,
            radius=radius,
        )
