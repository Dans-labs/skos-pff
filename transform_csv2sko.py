# from linkml_runtime.linkml_model.meta import SchemaDefinition
from linkml.utils.schemaloader import SchemaLoader
# from linkml_runtime.loaders import CSVLoader
# from schemas.pff import Row, PreferredFileFormatCollection


schema_path = "schemas/Hierarchy-Preferred-Formats.linkml.yaml"
schema = SchemaLoader(schema_path).resolve()
print(schema) 

# How the @#$$@ do I use the SchemaLoader?






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
