#!/bin/sh
# convert CSV to RDF using LinkML schema and generator

linkml-convert --schema schemas/pff-src.linkml.yaml -t rdf pff-src-SAMPLE.csv