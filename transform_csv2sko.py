from pathlib import Path
# from linkml_runtime.linkml_model.meta import SchemaDefinition
from linkml.utils.schemaloader import SchemaLoader
from linkml_runtime import SchemaView
from linkml_runtime.loaders import CSVLoader
# from schemas.H import Row, PreferredFileFormatCollection
from schemas import HierarchyPreferredFormats

# Classes
Collection = HierarchyPreferredFormats.PreferredFileFormatCollection()
Row = HierarchyPreferredFormats.Row()


# Schema
schema_path = (Path().cwd() / "schemas" / "Hierarchy-Preferred-Formats.linkml.yaml").as_posix()
print(f"Schema path: {schema_path}")
schema = SchemaLoader(schema_path).resolve()

# SchemaView 
# The SchemaView class in the linkml-runtime provides a method for dynamically introspecting and manipulating schemas.
view = SchemaView(schema_path)
# print(type(schema.classes["PreferredFileFormatCollection"]))
# print(view) 

# Loading Data from CSV
data_csv = CSVLoader().load(
    source=(Path().cwd() / "Hierarchy-Preferred-Formats-sample.csv").as_posix(),
    target_class=HierarchyPreferredFormats.PreferredFileFormatCollection,
    index_slot='Collection', 
    schema=schema,
    schemaview=view,
)


    # source="Hierarchy-Preferred-Formats-sample.csv",
    # ,                       
    # base_dir="schemas",
    # schema=schema, 
    # index_slot="row_slot"






# ex_row = Row(
#     Collection="Text documents",
#     Collection_URL_NL="https://dans.knaw.nl/nl/bestandsformaten/tekstdocumenten/",
#     Collection_URL_EN="https://dans.knaw.nl/en/file-formats/text-documents/",
#     Concept="PDF/A (.pdf)",
#     isPreferred=1,
#     Stable_URL_English="https://dans.knaw.nl/en/file-formats/text-documents/pdf-a/",
#     Stable_Nederlands_URL="https://dans.knaw.nl/bestandsformaten/tekstdocumenten/pdf-a/"
# )
# # Load the CSV instances using the schema
# csv_path = "Hierarchy-Preferred-Formats-sample.csv"
# loader = CSVLoader()
# data = loader.load(csv_path, 
#                    target_class="Row", 
#                    index_slot="row_slot",
#                    schema=schema, 
#                    )
# data =loader.load_any(csv_path, schema)
# print(data)


# loader = CSVLoader()
# # Returns a list of instances (usually of target_class)
# data_csv = loader.load(source="Hierarchy-Preferred-Formats-sample.csv", 
#                        target_class="PreferredFileFormatCollection",                       
#                        schema="schemas/Hierarchy-Preferred-Formats.linkml.yaml", 
#                        index_slot="row_slot"
#                        )

# print(data_csv)


#### convert source CSV to RDF
# linkml  
# linkml-convert --schema schemas/Hierarchy-Preferred-Formats.linkml.yaml   -t rdf Hierarchy-Preferred-Formats-sample.csv 

#### convert source CSV to RDF
