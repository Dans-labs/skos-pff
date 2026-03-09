import csv
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, OWL, RDFS, SKOS


# def create_rdf_graph():

def to_camel_case(value):
    content = "".join(value.title().split())
    return content[0].lower() + content[1:]

def url2uri(url, src_base_uri, dest_base_uri):
    url = url.replace(src_base_uri, dest_base_uri)
    if url[-1] == '/':
        return url[:-1]
    else:
        return url
    
    
def parse_csv_line_by_line(file_path):
    """
    A generator function that parses a CSV file line by line and yields each row as a dictionary.

    :param file_path: Path to the CSV file.
    :yield: Dictionary representing a row in the CSV file.
    """
    with open(file_path, mode='r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            yield row

pff_graph = Graph()
ns_str = 'http://vocabularies.dans.knaw.nl/pff/'
namespace = Namespace(ns_str)

for row in parse_csv_line_by_line('Hierarchy-Preferred-Formats.csv'):
    if row['isPreferred']:  # tmp - while spreadsheet is not complete

        # row['Concept'] - SKOS.Concept
        concept_uri = url2uri(url=row['Stable URL English'], src_base_uri='https://dans.knaw.nl/en/file-formats/text-documents/', dest_base_uri=ns_str)
        print(concept_uri)
#         # concept_uri = URIRef(f'{ns_str}{to_camel_case(row['Concept'])}')
#         pff_graph.add((concept_uri, RDF.type, SKOS.Concept))
#         pff_graph.add((concept_uri, SKOS.member, URIRef(f'{ns_str}{to_camel_case(row["Collection"])}')))
#         # todo: prefLabel
#         print(concept_uri)

#         # row['isPreferred'] -  SKOS.ConceptScheme
#         schema_instance_uri = URIRef(f'{ns_str}{row["isPreferred"]}')
#         pff_graph.add((schema_instance_uri,  RDF.type, SKOS.ConceptScheme))
#         pff_graph.add((concept_uri, SKOS.inScheme, schema_instance_uri))

#         # row['Collection'] 
#         # col1 collection
#         collection_uri = URIRef(f'{ns_str}{to_camel_case(row['Collection'])}')
#         pff_graph.add((collection_uri, RDF.type, SKOS.Collection))        

#         print(row)

# print(pff_graph.serialize())