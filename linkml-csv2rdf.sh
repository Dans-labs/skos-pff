#!/bin/sh
# convert CSV to RDF using LinkML schema and generator

linkml-convert --schema schemas/Hierarchy-Preferred-Formats.linkml.yaml -t rdf pff-src-SAMPLE.csv