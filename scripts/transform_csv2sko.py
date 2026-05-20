# import RDFlib linkml

from linkml_runtime.loaders import CSVLoader

loader = CSVLoader()
# Returns a list of instances (usually of target_class)
data_csv = loader.load(source="src_pff-sample.csv", schema="schemas/src_pff.linkml.yaml", target_class="Row")

print(data_csv)


#### convert source CSV to RDF
# linkml  
# linkml-convert --schema schemas/src_pff.linkml.yaml   -t rdf src_pff.csv 

#### convert source CSV to RDF
