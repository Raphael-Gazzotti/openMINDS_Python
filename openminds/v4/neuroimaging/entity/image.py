"""
Structured information on an image.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class Image(LinkedMetadata):
    """
    Structured information on an image.
    """

    type_ = "https://openminds.om-i.org/types/Image"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v4.0"

    properties = [
        Property(
            "additional_remarks",
            str,
            "additionalRemarks",
            formatting="text/markdown",
            multiline=True,
            description="Mention of what deserves additional attention or notice.",
            instructions="Enter any additional remarks concerning this image.",
        ),
        Property(
            "captured_with",
            [
                "openminds.v4.ephys.ElectrodeArrayUsage",
                "openminds.v4.ephys.ElectrodeUsage",
                "openminds.v4.ephys.PipetteUsage",
                "openminds.v4.neuroimaging.MRIScannerUsage",
                "openminds.v4.specimen_prep.SlicingDeviceUsage",
            ],
            "capturedWith",
            description="no description available",
            instructions="Add the device used to capture this image.",
        ),
        Property(
            "color_depth",
            "openminds.v4.core.QuantitativeValue",
            "colorDepth",
            description="no description available",
            instructions="Enter the number of bits used to represent the color of each pixel.",
        ),
        Property(
            "coordinate_space",
            "openminds.v4.sands.CustomCoordinateSpace",
            "coordinateSpace",
            required=True,
            description="Two or three dimensional geometric setting.",
            instructions="Add the coordinate space in which this image exists.",
        ),
        Property(
            "data_location",
            "openminds.v4.core.File",
            "dataLocation",
            required=True,
            description="no description available",
            instructions="Add the location of the file or file bundle in which the image is stored.",
        ),
        Property(
            "dimensions",
            int,
            "dimension",
            multiple=True,
            unique_items=False,
            min_items=2,
            max_items=2,
            required=True,
            description="no description available",
            instructions="Enter the dimension of this image in pixels.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            description="Word or phrase that constitutes the distinctive designation of the image.",
            instructions="Enter a descriptive name for this image.",
        ),
        Property(
            "pixel_sizes",
            "openminds.v4.core.QuantitativeValue",
            "pixelSize",
            multiple=True,
            unique_items=False,
            min_items=2,
            max_items=2,
            required=True,
            description="no description available",
            instructions="Enter the physical pixel size for this image (in x,y order).",
        ),
    ]

    def __init__(
        self,
        id=None,
        additional_remarks=None,
        captured_with=None,
        color_depth=None,
        coordinate_space=None,
        data_location=None,
        dimensions=None,
        name=None,
        pixel_sizes=None,
    ):
        return super().__init__(
            id=id,
            additional_remarks=additional_remarks,
            captured_with=captured_with,
            color_depth=color_depth,
            coordinate_space=coordinate_space,
            data_location=data_location,
            dimensions=dimensions,
            name=name,
            pixel_sizes=pixel_sizes,
        )
