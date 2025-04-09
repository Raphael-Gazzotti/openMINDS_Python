"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class AnatomicalTargetPosition(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/sands/AnatomicalTargetPosition"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v2.0"

    properties = [
        Property(
            "additional_remarks",
            str,
            "additionalRemarks",
            formatting="text/markdown",
            multiline=True,
            description="Mention of what deserves additional attention or notice.",
            instructions="Enter any additional remarks concerning this anatomical target position.",
        ),
        Property(
            "anatomical_targets",
            [
                "openminds.v2.controlled_terms.CellType",
                "openminds.v2.controlled_terms.Organ",
                "openminds.v2.controlled_terms.OrganismSubstance",
                "openminds.v2.controlled_terms.SubcellularEntity",
                "openminds.v2.controlled_terms.UBERONParcellation",
                "openminds.v2.sands.CustomAnatomicalEntity",
                "openminds.v2.sands.ParcellationEntity",
                "openminds.v2.sands.ParcellationEntityVersion",
            ],
            "anatomicalTarget",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="no description available",
            instructions="Add all anatomical entities that describe the target position(s).",
        ),
        Property(
            "spatial_locations",
            "openminds.v2.sands.CoordinatePoint",
            "spatialLocation",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all coordinate points that describe the spatial location of the anatomical target structure(s).",
        ),
        Property(
            "target_identification_type",
            "openminds.v2.controlled_terms.AnatomicalIdentificationType",
            "targetIdentificationType",
            required=True,
            description="no description available",
            instructions="Add the target identification type that best describes how the this anatomical target position was identified.",
        ),
    ]

    def __init__(
        self,
        id=None,
        additional_remarks=None,
        anatomical_targets=None,
        spatial_locations=None,
        target_identification_type=None,
    ):
        return super().__init__(
            id=id,
            additional_remarks=additional_remarks,
            anatomical_targets=anatomical_targets,
            spatial_locations=spatial_locations,
            target_identification_type=target_identification_type,
        )
