"""
Structured information about a process of validating a computational model.
"""

# this file was auto-generated!

from datetime import datetime, time
from numbers import Real

from openminds.base import LinkedMetadata
from openminds.properties import Property


class ModelValidation(LinkedMetadata):
    """
    Structured information about a process of validating a computational model.
    """

    type_ = "https://openminds.om-i.org/types/ModelValidation"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v4.0"

    properties = [
        Property(
            "custom_property_sets",
            "openminds.v4.core.CustomPropertySet",
            "customPropertySet",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add any user-defined parameters grouped in context-specific sets that are not covered in the standardized properties of this activity.",
        ),
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            description="Longer statement or account giving the characteristics of the model validation.",
            instructions="Enter a description of this activity.",
        ),
        Property(
            "end_time",
            [datetime, time],
            "endTime",
            description="no description available",
            instructions="Enter the date and/or time on when this activity ended, formatted as either '2023-02-07T16:00:00+00:00' (date-time) or '16:00:00+00:00' (time).",
        ),
        Property(
            "environment",
            ["openminds.v4.computation.Environment", "openminds.v4.core.WebServiceVersion"],
            "environment",
            required=True,
            description="no description available",
            instructions="Add the computational environment in which this computation was executed.",
        ),
        Property(
            "inputs",
            [
                "openminds.v4.computation.LocalFile",
                "openminds.v4.computation.ValidationTestVersion",
                "openminds.v4.core.File",
                "openminds.v4.core.FileBundle",
                "openminds.v4.core.ModelVersion",
                "openminds.v4.core.SoftwareVersion",
            ],
            "input",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Something or someone that is put into or participates in a process or machine.",
            instructions="Add all inputs used by this activity.",
        ),
        Property(
            "launch_configuration",
            "openminds.v4.computation.LaunchConfiguration",
            "launchConfiguration",
            description="no description available",
            instructions="Add the launch configuration of this computation (e.g., command-line arguments).",
        ),
        Property(
            "lookup_label",
            str,
            "lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this activity that may help you to find this instance more easily.",
        ),
        Property(
            "outputs",
            ["openminds.v4.computation.LocalFile", "openminds.v4.core.File", "openminds.v4.core.FileBundle"],
            "output",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Something or someone that comes out of, is delivered or produced by a process or machine.",
            instructions="Add all outputs generated by this activity.",
        ),
        Property(
            "performed_by",
            ["openminds.v4.computation.SoftwareAgent", "openminds.v4.core.Person"],
            "performedBy",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all agents that performed this activity.",
        ),
        Property(
            "recipe",
            "openminds.v4.computation.WorkflowRecipeVersion",
            "recipe",
            description="no description available",
            instructions="Add the workflow recipe version used for this computation.",
        ),
        Property(
            "resource_usages",
            ["openminds.v4.core.QuantitativeValue", "openminds.v4.core.QuantitativeValueRange"],
            "resourceUsage",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Enter all resources used during this computation (e.g., core-hours or energy).",
        ),
        Property(
            "score",
            Real,
            "score",
            description="no description available",
            instructions="Enter the numerical score generated by this model validation.",
        ),
        Property(
            "start_time",
            [datetime, time],
            "startTime",
            required=True,
            description="no description available",
            instructions="Enter the date and/or time on when this activity started, formatted as either '2023-02-07T16:00:00+00:00' (date-time) or '16:00:00+00:00' (time).",
        ),
        Property(
            "started_by",
            ["openminds.v4.computation.SoftwareAgent", "openminds.v4.core.Person"],
            "startedBy",
            description="no description available",
            instructions="Add the agent that started this computation.",
        ),
        Property(
            "status",
            "openminds.v4.controlled_terms.ActionStatusType",
            "status",
            description="no description available",
            instructions="Enter the current status of this computation.",
        ),
        Property(
            "study_targets",
            [
                "openminds.v4.controlled_terms.AuditoryStimulusType",
                "openminds.v4.controlled_terms.BiologicalOrder",
                "openminds.v4.controlled_terms.BiologicalSex",
                "openminds.v4.controlled_terms.BreedingType",
                "openminds.v4.controlled_terms.CellCultureType",
                "openminds.v4.controlled_terms.CellType",
                "openminds.v4.controlled_terms.Disease",
                "openminds.v4.controlled_terms.DiseaseModel",
                "openminds.v4.controlled_terms.ElectricalStimulusType",
                "openminds.v4.controlled_terms.GeneticStrainType",
                "openminds.v4.controlled_terms.GustatoryStimulusType",
                "openminds.v4.controlled_terms.Handedness",
                "openminds.v4.controlled_terms.MolecularEntity",
                "openminds.v4.controlled_terms.OlfactoryStimulusType",
                "openminds.v4.controlled_terms.OpticalStimulusType",
                "openminds.v4.controlled_terms.Organ",
                "openminds.v4.controlled_terms.OrganismSubstance",
                "openminds.v4.controlled_terms.OrganismSystem",
                "openminds.v4.controlled_terms.Species",
                "openminds.v4.controlled_terms.SubcellularEntity",
                "openminds.v4.controlled_terms.TactileStimulusType",
                "openminds.v4.controlled_terms.TermSuggestion",
                "openminds.v4.controlled_terms.TissueSampleType",
                "openminds.v4.controlled_terms.UBERONParcellation",
                "openminds.v4.controlled_terms.VisualStimulusType",
                "openminds.v4.sands.CustomAnatomicalEntity",
                "openminds.v4.sands.ParcellationEntity",
                "openminds.v4.sands.ParcellationEntityVersion",
            ],
            "studyTarget",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Structure or function that was targeted within a study.",
            instructions="Add all study targets of this activity.",
        ),
        Property(
            "tags",
            str,
            "tag",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="no description available",
            instructions="Enter any custom tags for this computation.",
        ),
        Property(
            "techniques",
            "openminds.v4.controlled_terms.AnalysisTechnique",
            "technique",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Method of accomplishing a desired aim.",
            instructions="Add all analysis techniques that were used in this computation.",
        ),
        Property(
            "was_informed_by",
            [
                "openminds.v4.computation.DataAnalysis",
                "openminds.v4.computation.DataCopy",
                "openminds.v4.computation.GenericComputation",
                "openminds.v4.computation.ModelValidation",
                "openminds.v4.computation.Optimization",
                "openminds.v4.computation.Simulation",
                "openminds.v4.computation.Visualization",
            ],
            "wasInformedBy",
            description="no description available",
            instructions="Add another computation that sent data to this one during runtime.",
        ),
    ]

    def __init__(
        self,
        id=None,
        custom_property_sets=None,
        description=None,
        end_time=None,
        environment=None,
        inputs=None,
        launch_configuration=None,
        lookup_label=None,
        outputs=None,
        performed_by=None,
        recipe=None,
        resource_usages=None,
        score=None,
        start_time=None,
        started_by=None,
        status=None,
        study_targets=None,
        tags=None,
        techniques=None,
        was_informed_by=None,
    ):
        return super().__init__(
            id=id,
            custom_property_sets=custom_property_sets,
            description=description,
            end_time=end_time,
            environment=environment,
            inputs=inputs,
            launch_configuration=launch_configuration,
            lookup_label=lookup_label,
            outputs=outputs,
            performed_by=performed_by,
            recipe=recipe,
            resource_usages=resource_usages,
            score=score,
            start_time=start_time,
            started_by=started_by,
            status=status,
            study_targets=study_targets,
            tags=tags,
            techniques=techniques,
            was_informed_by=was_informed_by,
        )
