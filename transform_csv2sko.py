# from linkml_runtime.linkml_model.meta import SchemaDefinition
# from linkml_runtime.dumpers import json_dumper
# from linkml.utils.schemaloader import SchemaLoader
# from linkml_runtime.loaders import CSVLoader
#import pff
# from pff import Row, PreferredFileFormatCollection
from schemas import pff
# from schemas.pff import Row, PreferredFileFormatCollection
print(pff.__file__)

# # load schema
# schema_path = "schemas/Hierarchy-Preferred-Formats.linkml.yaml"
# schema = SchemaLoader(schema_path).resolve()
# # print(json_dumper.dumps(schema))

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
