"""
<description not available>
"""

# this file was auto-generated!

from numbers import Real

from openminds.base import LinkedMetadata
from openminds.properties import Property


class MRIScannerUsage(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/MRIScannerUsage"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "mr_acquisition_type",
            "openminds.latest.controlled_terms.MRAcquisitionType",
            "MRAcquisitionType",
            description="no description available",
            instructions="Add the type of sequence readout (2D or 3D).",
        ),
        Property(
            "mt_state",
            bool,
            "MTState",
            description="no description available",
            instructions="Boolean stating whether the magnetization transfer pulse is applied.",
        ),
        Property(
            "b_values",
            "openminds.latest.core.File",
            "bValues",
            description="no description available",
            instructions="Add the b values coresponding to this acquisition.",
        ),
        Property(
            "b_vectors",
            "openminds.latest.core.File",
            "bVectors",
            description="no description available",
            instructions="Add the b vectors coresponding to this acquisition.",
        ),
        Property(
            "device",
            "openminds.latest.neuroimaging.MRIScanner",
            "device",
            required=True,
            description="Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function.",
            instructions="Add the MRI Scanner used.",
        ),
        Property(
            "dwell_time",
            "openminds.latest.core.QuantitativeValue",
            "dwellTime",
            description="no description available",
            instructions="Enter the dwell time of this aquistion.",
        ),
        Property(
            "echo_times",
            "openminds.latest.core.QuantitativeValue",
            "echoTime",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Enter the echo times of this acquisition (TE).",
        ),
        Property(
            "field_of_view",
            ["openminds.latest.sands.Circle", "openminds.latest.sands.Ellipse", "openminds.latest.sands.Rectangle"],
            "fieldOfView",
            description="no description available",
            instructions="Add the field of view of this image.",
        ),
        Property(
            "flip_angle",
            "openminds.latest.core.QuantitativeValue",
            "flipAngle",
            description="no description available",
            instructions="Enter the flip angle of this scan (preferred units: degrees).",
        ),
        Property(
            "inter_slice_gap",
            ["openminds.latest.core.QuantitativeValue", "openminds.latest.core.QuantitativeValueRange"],
            "interSliceGap",
            description="no description available",
            instructions="Enter the inter slice distance of this scan.",
        ),
        Property(
            "inversion_time",
            "openminds.latest.core.QuantitativeValue",
            "inversionTime",
            description="no description available",
            instructions="Enter the inversion time of this aquistion.",
        ),
        Property(
            "lookup_label",
            str,
            "lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this device usage that may help you to find this instance more easily.",
        ),
        Property(
            "metadata_locations",
            ["openminds.latest.core.File", "openminds.latest.core.FileBundle"],
            "metadataLocation",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all files or file bundles containing additional information about the usage of this device.",
        ),
        Property(
            "nonlinear_gradient_correction",
            bool,
            "nonlinearGradientCorrection",
            description="no description available",
            instructions="Has this scan, been corrected for gradient nonlinearities by the scanner sequence?",
        ),
        Property(
            "number_of_volumes_discarded_by_scanner",
            Real,
            "numberOfVolumesDiscardedByScanner",
            description="no description available",
            instructions="Enter number of volumes discarded by scanner before the first volume.",
        ),
        Property(
            "parallel_acquisition_technique",
            str,
            "parallelAcquisitionTechnique",
            formatting="text/plain",
            description="no description available",
            instructions="no instructions available",
        ),
        Property(
            "phase_encoding_direction",
            "openminds.latest.types.CartesianDirectionVector",
            "phaseEncodingDirection",
            description="no description available",
            instructions="Add the direction along which phase is modulated which may result in visible distortions.",
        ),
        Property(
            "pulse_sequence_type",
            "openminds.latest.controlled_terms.MRIPulseSequence",
            "pulseSequenceType",
            description="no description available",
            instructions="Add the type pulse sequence used for this scan.",
        ),
        Property(
            "radiofrequency_coil_type",
            "openminds.latest.types.MRIRadiofrequencyCoilType",
            "radiofrequencyCoilType",
            description="no description available",
            instructions="Add the type of radiofrequency coil.",
        ),
        Property(
            "repetition_time",
            "openminds.latest.core.QuantitativeValue",
            "repetitionTime",
            description="no description available",
            instructions="Enter the echo time of this acquisition (TR).",
        ),
        Property(
            "slice_order",
            "openminds.latest.core.QuantitativeValueArray",
            "sliceOrder",
            description="no description available",
            instructions="Enter the time in which each slice have been acquired within each volume.",
        ),
        Property(
            "slice_timing",
            "openminds.latest.core.QuantitativeValueArray",
            "sliceTiming",
            description="no description available",
            instructions="Enter the time in which each slice have been acquired within each volume.",
        ),
        Property(
            "spoiling_state",
            bool,
            "spoilingState",
            description="no description available",
            instructions="Boolean stating whether the pulse sequence uses any type of spoiling strategy to suppress residual transverse magnetization.",
        ),
        Property(
            "used_specimen",
            ["openminds.latest.core.SubjectState", "openminds.latest.core.TissueSampleState"],
            "usedSpecimen",
            description="no description available",
            instructions="Add the state of the tissue sample or subject that this device was used on.",
        ),
        Property(
            "voxel_size",
            "openminds.latest.core.QuantitativeValueArray",
            "voxelSize",
            description="Extent of the discrete elements comprising a three-dimensional entity.",
            instructions="Enter voxel size this image: in this order x,y,z.",
        ),
    ]

    def __init__(
        self,
        id=None,
        mr_acquisition_type=None,
        mt_state=None,
        b_values=None,
        b_vectors=None,
        device=None,
        dwell_time=None,
        echo_times=None,
        field_of_view=None,
        flip_angle=None,
        inter_slice_gap=None,
        inversion_time=None,
        lookup_label=None,
        metadata_locations=None,
        nonlinear_gradient_correction=None,
        number_of_volumes_discarded_by_scanner=None,
        parallel_acquisition_technique=None,
        phase_encoding_direction=None,
        pulse_sequence_type=None,
        radiofrequency_coil_type=None,
        repetition_time=None,
        slice_order=None,
        slice_timing=None,
        spoiling_state=None,
        used_specimen=None,
        voxel_size=None,
    ):
        return super().__init__(
            id=id,
            mr_acquisition_type=mr_acquisition_type,
            mt_state=mt_state,
            b_values=b_values,
            b_vectors=b_vectors,
            device=device,
            dwell_time=dwell_time,
            echo_times=echo_times,
            field_of_view=field_of_view,
            flip_angle=flip_angle,
            inter_slice_gap=inter_slice_gap,
            inversion_time=inversion_time,
            lookup_label=lookup_label,
            metadata_locations=metadata_locations,
            nonlinear_gradient_correction=nonlinear_gradient_correction,
            number_of_volumes_discarded_by_scanner=number_of_volumes_discarded_by_scanner,
            parallel_acquisition_technique=parallel_acquisition_technique,
            phase_encoding_direction=phase_encoding_direction,
            pulse_sequence_type=pulse_sequence_type,
            radiofrequency_coil_type=radiofrequency_coil_type,
            repetition_time=repetition_time,
            slice_order=slice_order,
            slice_timing=slice_timing,
            spoiling_state=spoiling_state,
            used_specimen=used_specimen,
            voxel_size=voxel_size,
        )
