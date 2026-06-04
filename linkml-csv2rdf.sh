#!/bin/sh
# convert CSV to RDF using LinkML schema and generator

INPUT_DATA=pff-src-SAMPLE.csv
SCHEMA=schemas/pff-src.linkml.yaml
INPUT_DATA_rdf=pff-src-SAMPLE.ttl


linkml-convert --schema $SCHEMA -t ttl $INPUT_DATA -o $INPUT_DATA_rdf
