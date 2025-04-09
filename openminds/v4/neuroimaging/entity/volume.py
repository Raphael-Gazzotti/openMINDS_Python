"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class Volume(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Volume"
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
            instructions="Enter any additional remarks concerning this volume.",
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
            instructions="Add the device used to capture this volume.",
        ),
        Property(
            "coordinate_space",
            ["openminds.v4.sands.CommonCoordinateSpaceVersion", "openminds.v4.sands.CustomCoordinateSpace"],
            "coordinateSpace",
            required=True,
            description="Two or three dimensional geometric setting.",
            instructions="Add the coordinate space in which this volume exists.",
        ),
        Property(
            "data_location",
            "openminds.v4.core.File",
            "dataLocation",
            required=True,
            description="no description available",
            instructions="Add the location of the file or file bundle in which the volume is stored.",
        ),
        Property(
            "dimensions",
            int,
            "dimension",
            multiple=True,
            unique_items=False,
            min_items=3,
            max_items=3,
            required=True,
            description="no description available",
            instructions="Enter the dimension of this volume.",
        ),
        Property(
            "lookup_label",
            str,
            "lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this volume that may help you to find this instance more easily.",
        ),
        Property(
            "number_of_slices",
            int,
            "numberOfSlices",
            description="no description available",
            instructions="Enter number of slices in this volume.",
        ),
        Property(
            "voxel_sizes",
            "openminds.v4.core.QuantitativeValue",
            "voxelSize",
            multiple=True,
            unique_items=False,
            min_items=3,
            max_items=3,
            required=True,
            description="Extent of the discrete elements comprising a three-dimensional entity.",
            instructions="Enter the physical voxel size for this image (in x,y,z order).",
        ),
    ]

    def __init__(
        self,
        id=None,
        additional_remarks=None,
        captured_with=None,
        coordinate_space=None,
        data_location=None,
        dimensions=None,
        lookup_label=None,
        number_of_slices=None,
        voxel_sizes=None,
    ):
        return super().__init__(
            id=id,
            additional_remarks=additional_remarks,
            captured_with=captured_with,
            coordinate_space=coordinate_space,
            data_location=data_location,
            dimensions=dimensions,
            lookup_label=lookup_label,
            number_of_slices=number_of_slices,
            voxel_sizes=voxel_sizes,
        )
