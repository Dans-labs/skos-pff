#!/bin/bash

DPFF_CONF=$':DPFF a skosmos:Vocabulary, void:Dataset ;
dc:title "DANS Preferred File Formats"@en ;
skosmos:shortName "DPFF";
dc:subject :cat_general ;
void:uriSpace "http://vocabularies.dans.knaw.nl/DPFF/";
skosmos:language "en", "nl";
skosmos:defaultLanguage "en";
skosmos:showTopConcepts true ;
skosmos:fullAlphabeticalIndex false ;
skosmos:groupClass skos:Collection ;
void:sparqlEndpoint <http://fuseki-cache:80/skosmos/sparql> ; 
skosmos:sparqlGraph <http://vocabularies.dans.knaw.nl/DPFF/> .'


# append to aatc config for skosmos (original: https://github.com/DANS-KNAW/dans-core-systems/blob/e12619520b3f48ab4a3d46bc09bc79cb5c3dd1b2/provisioning/files/vocabs/aatc.conf)
# echo "$DPFF_CONF" >> Skosmos/dockerfiles/config/config-docker-compose.ttl
# start docker containers # more on Skosmos containers in Skosmos/dockerfiles/README.md
cd Skosmos
docker compose down
docker compose up -d

sleep 2
# delete all triples  GRAPH <http://vocabularies.dans.knaw.nl/dpff/>
curl -X POST   --data-urlencode 'update=DELETE { GRAPH <http://vocabularies.dans.knaw.nl/DPFF/> { ?s ?p ?o } } WHERE { GRAPH <http://vocabularies.dans.knaw.nl/DPFF/> { ?s ?p ?o } }' http://localhost:9030/skosmos/
sleep 1
cd ..
# Load aatc.ttl to Fuseki on graph http://vocabularies.dans.knaw.nl/DPFF/
curl -X POST -H "Content-Type: text/turtle" -T PreferredFileFormats-controlledlist.ttl "http://localhost:9030/skosmos/data?graph=http://vocabularies.dans.knaw.nl/DPFF/"

echo "DPFF in Skosmos: http://localhost:9090/DPFF"

