"""
Structured information on the operating device.
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class OperatingDevice(LinkedMetadata):
    """
    Structured information on the operating device.
    """

    type_ = "https://openminds.om-i.org/types/OperatingDevice"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "definition",
            str,
            "definition",
            formatting="text/markdown",
            multiline=True,
            description="Short, but precise statement of the meaning of a word, word group, sign or a symbol.",
            instructions="Enter one sentence for defining this term.",
        ),
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            description="Longer statement or account giving the characteristics of the operating device.",
            instructions="Enter a short text describing this term.",
        ),
        Property(
            "interlex_identifier",
            IRI,
            "interlexIdentifier",
            description="Persistent identifier for a term registered in the InterLex project.",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the integrated ontology entry in the InterLex project.",
        ),
        Property(
            "knowledge_space_link",
            IRI,
            "knowledgeSpaceLink",
            description="Persistent link to an encyclopedia entry in the Knowledge Space project.",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the wiki page of the corresponding term in the KnowledgeSpace.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of the operating device.",
            instructions="Controlled term originating from a defined terminology.",
        ),
        Property(
            "preferred_ontology_identifier",
            IRI,
            "preferredOntologyIdentifier",
            description="Persistent identifier of a preferred ontological term.",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the preferred ontological term.",
        ),
        Property(
            "synonyms",
            str,
            "synonym",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="Words or expressions used in the same language that have the same or nearly the same meaning in some or all senses.",
            instructions="Enter one or several synonyms (including abbreviations) for this controlled term.",
        ),
    ]

    def __init__(
        self,
        id=None,
        definition=None,
        description=None,
        interlex_identifier=None,
        knowledge_space_link=None,
        name=None,
        preferred_ontology_identifier=None,
        synonyms=None,
    ):
        return super().__init__(
            id=id,
            definition=definition,
            description=description,
            interlex_identifier=interlex_identifier,
            knowledge_space_link=knowledge_space_link,
            name=name,
            preferred_ontology_identifier=preferred_ontology_identifier,
            synonyms=synonyms,
        )

    @classmethod
    def instances(cls):
        return [value for value in cls.__dict__.values() if isinstance(value, cls)]

    @classmethod
    def by_name(cls, name):
        if cls._instance_lookup is None:
            cls._instance_lookup = {}
            for instance in cls.instances():
                cls._instance_lookup[instance.name] = instance
                if instance.synonyms:
                    for synonym in instance.synonyms:
                        cls._instance_lookup[synonym] = instance
        return cls._instance_lookup[name]


OperatingDevice.desktop = OperatingDevice(
    id="https://openminds.om-i.org/instances/operatingDevice/desktop",
    name="desktop",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/wiki/Q56155"),
)
OperatingDevice.embedded_system = OperatingDevice(
    id="https://openminds.om-i.org/instances/operatingDevice/embeddedSystem",
    name="embedded system",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/wiki/Q193040"),
)
OperatingDevice.high_performance_computer = OperatingDevice(
    id="https://openminds.om-i.org/instances/operatingDevice/highPerformanceComputer",
    name="high-performance computer",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/wiki/Q121117"),
)
OperatingDevice.mobile = OperatingDevice(
    id="https://openminds.om-i.org/instances/operatingDevice/mobile",
    name="mobile",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/wiki/Q5082128"),
)
OperatingDevice.neuromorphic_computer = OperatingDevice(
    id="https://openminds.om-i.org/instances/operatingDevice/neuromorphicComputer",
    definition="Very-large-scale integration (VLSI) systems containing electronic circuits used to mimic neuro-biological architectures present in the nervous system.",
    name="neuromorphic computer",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/wiki/Q56270917"),
)
OperatingDevice.server = OperatingDevice(
    id="https://openminds.om-i.org/instances/operatingDevice/server",
    name="server",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/wiki/Q64729893"),
)
OperatingDevice.web = OperatingDevice(
    id="https://openminds.om-i.org/instances/operatingDevice/web",
    name="web",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/wiki/Q6368"),
)
