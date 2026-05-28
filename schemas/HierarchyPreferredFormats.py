# Auto generated from Hierarchy-Preferred-Formats.linkml.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-26T12:10:45
# Schema: DANS-PFF-spreadsheet-linkml-schema
#
# id: http://vocabularies.dans.knaw.nl/pff/linkml-schema
# description: data source CSV: Hierarchy-Preferred-Formats-sample.csv
#
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, String, Uri
from linkml_runtime.utils.metamodelcore import Bool, URI

metamodel_version = "1.7.0"
version = None

# Namespaces
DPFF = CurieNamespace('dpff', 'http://vocabularies.dans.knaw.nl/pff/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = DPFF


# Types
class HttpsIdentifier(String):
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "https identifier"
    type_model_uri = DPFF.HttpsIdentifier


# Class references



@dataclass(repr=False)
class PreferredFileFormatCollection(YAMLRoot):
    """
    DANS preferred file formats
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPFF["PreferredFileFormatCollection"]
    class_class_curie: ClassVar[str] = "dpff:PreferredFileFormatCollection"
    class_name: ClassVar[str] = "PreferredFileFormatCollection"
    class_model_uri: ClassVar[URIRef] = DPFF.PreferredFileFormatCollection

    row_slot: Optional[Union[Union[dict, "Row"], list[Union[dict, "Row"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.row_slot, list):
            self.row_slot = [self.row_slot] if self.row_slot is not None else []
        self.row_slot = [v if isinstance(v, Row) else Row(**as_dict(v)) for v in self.row_slot]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Row(YAMLRoot):
    """
    A row describing a file format, its hierarchy, and metadata.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPFF["Row"]
    class_class_curie: ClassVar[str] = "dpff:Row"
    class_name: ClassVar[str] = "Row"
    class_model_uri: ClassVar[URIRef] = DPFF.Row

    Collection: Optional[str] = None
    Collection_URL_NL: Optional[Union[str, URI]] = None
    Collection_URL_EN: Optional[Union[str, URI]] = None
    Concept: Optional[str] = None
    isPreferred: Optional[Union[bool, Bool]] = False
    Stable_URL_English: Optional[Union[str, URI]] = None
    Stable_Nederlands_URL: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.Collection is not None and not isinstance(self.Collection, str):
            self.Collection = str(self.Collection)

        if self.Collection_URL_NL is not None and not isinstance(self.Collection_URL_NL, URI):
            self.Collection_URL_NL = URI(self.Collection_URL_NL)

        if self.Collection_URL_EN is not None and not isinstance(self.Collection_URL_EN, URI):
            self.Collection_URL_EN = URI(self.Collection_URL_EN)

        if self.Concept is not None and not isinstance(self.Concept, str):
            self.Concept = str(self.Concept)

        if self.isPreferred is not None and not isinstance(self.isPreferred, Bool):
            self.isPreferred = Bool(self.isPreferred)

        if self.Stable_URL_English is not None and not isinstance(self.Stable_URL_English, URI):
            self.Stable_URL_English = URI(self.Stable_URL_English)

        if self.Stable_Nederlands_URL is not None and not isinstance(self.Stable_Nederlands_URL, URI):
            self.Stable_Nederlands_URL = URI(self.Stable_Nederlands_URL)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.Collection = Slot(uri=DPFF.Collection, name="Collection", curie=DPFF.curie('Collection'),
                   model_uri=DPFF.Collection, domain=None, range=Optional[str])

slots.Collection_URL_NL = Slot(uri=DPFF.Collection_URL_NL, name="Collection_URL_NL", curie=DPFF.curie('Collection_URL_NL'),
                   model_uri=DPFF.Collection_URL_NL, domain=None, range=Optional[Union[str, URI]])

slots.Collection_URL_EN = Slot(uri=DPFF.Collection_URL_EN, name="Collection_URL_EN", curie=DPFF.curie('Collection_URL_EN'),
                   model_uri=DPFF.Collection_URL_EN, domain=None, range=Optional[Union[str, URI]])

slots.Concept = Slot(uri=DPFF.Concept, name="Concept", curie=DPFF.curie('Concept'),
                   model_uri=DPFF.Concept, domain=None, range=Optional[str])

slots.isPreferred = Slot(uri=DPFF.isPreferred, name="isPreferred", curie=DPFF.curie('isPreferred'),
                   model_uri=DPFF.isPreferred, domain=None, range=Optional[Union[bool, Bool]])

slots.Stable_URL_English = Slot(uri=DPFF.Stable_URL_English, name="Stable_URL_English", curie=DPFF.curie('Stable_URL_English'),
                   model_uri=DPFF.Stable_URL_English, domain=None, range=Optional[Union[str, URI]])

slots.Stable_Nederlands_URL = Slot(uri=DPFF.Stable_Nederlands_URL, name="Stable_Nederlands_URL", curie=DPFF.curie('Stable_Nederlands_URL'),
                   model_uri=DPFF.Stable_Nederlands_URL, domain=None, range=Optional[Union[str, URI]])

slots.row_slot = Slot(uri=DPFF.row_slot, name="row_slot", curie=DPFF.curie('row_slot'),
                   model_uri=DPFF.row_slot, domain=None, range=Optional[Union[Union[dict, Row], list[Union[dict, Row]]]])

