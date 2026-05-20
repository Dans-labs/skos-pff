# DANS Preferred File Formats as a SKOS Artifact

DANS maintains a list of preferred file formats (PFF) in https://dans.knaw.nl/nl/bestandsformaten/ 

This repository attempts to encode the information contained in PFF in a SKOS taxonomy.

Similar effort was made in DARIAH project. See https://github.com/ekoi/DANS-File-Formats/blob/additional-formats/dans-file-formats.json



## DANS PFF HTML Content

Scrapped with `python scripts/scrape_pffs_html_pages.py`

Using the URLs from [Hierarchy-Preferred-Formats.csv](Hierarchy-Preferred-Formats.csv) and saving HTML content to [html/](html/), according to `/html/<language>/<file>.html.`

From columns: Collection_URL_NL, Collection_URL_EN, Stable URL English, Stable Nederlands URL

Example: CSV values
* `https://dans.knaw.nl/nl/bestandsformaten/tekstdocumenten` saved to `html/nl/tekstdocumenten.html`
* `https://dans.knaw.nl/en/file-formats/text-documents/` saved to `html/en/text-documents.html`



## DANS PFF Content as skos

[pff-skos.ttl](pff-skos.ttl) [PROTOTYPE]- contains the DANS PFF data in Skos (turtle RDF)  

## DANS PFF Data Model

Define using LinkML in [schemas/pff.linkml.yaml](schemas/pff.linkml.yaml)

![PFF schema in GraphViz](imgs/pff-schema.png) 

generated via `linkml generate graphviz -f png -o imgs/pff-schema schemas/pff.linkml.yaml`

### Data Model Summary table

generated with `linkml generate summary schemas/pff.linkml.yaml | pandoc -f tsv -t gfm`


| Class Name        | Parent Class | YAML Class Name   | Description                                         | Flags | Slot Name    | YAML Slot Name | Range             | Card  | Slot Description | URI                |
|-------------------|--------------|-------------------|-----------------------------------------------------|-------|--------------|----------------|-------------------|-------|------------------|--------------------|
| SKOSCollection    |              | SKOSCollection    | SKOS Collection grouping Concepts                   |       |              |                |                   |       |                  |                    |
|                   |              |                   |                                                     |       | prefLabel    |                | str               | 0..\* |                  | skos:prefLabel     |
|                   |              |                   |                                                     |       | member       |                | SKOSConcept       | 0..\* |                  | skos:member        |
| SKOSConcept       |              | SKOSConcept       | SKOS Concept representing a file format             |       |              |                |                   |       |                  |                    |
|                   |              |                   |                                                     |       | prefLabel    |                | str               | 0..\* |                  | skos:prefLabel     |
|                   |              |                   |                                                     |       | definition   |                | str               | 0..\* |                  | skos:definition    |
|                   |              |                   |                                                     |       | broader      |                | SKOSConcept       | 0..1  |                  | skos:broader       |
|                   |              |                   |                                                     |       | narrower     |                | SKOSConcept       | 0..\* |                  | skos:narrower      |
|                   |              |                   |                                                     |       | inScheme     |                | SKOSConceptScheme | 0..1  |                  | skos:inScheme      |
|                   |              |                   |                                                     |       | isReplacedBy |                | SKOSConcept       | 0..\* |                  | dct:isReplacedBy   |
|                   |              |                   |                                                     |       | exactMatch   |                | SKOSConcept       | 0..1  |                  | skos:exactMatch    |
| SKOSConceptScheme |              | SKOSConceptScheme | SKOS Concept Scheme for DANS Preferred File Formats |       |              |                |                   |       |                  |                    |
|                   |              |                   |                                                     |       | title        |                | str               | 0..1  |                  | dct:title          |
|                   |              |                   |                                                     |       | prefLabel    |                | str               | 0..\* |                  | skos:prefLabel     |
|                   |              |                   |                                                     |       | definition   |                | str               | 0..\* |                  | skos:definition    |
|                   |              |                   |                                                     |       | versionInfo  |                | str               | 0..1  |                  | owl:versionInfo    |
|                   |              |                   |                                                     |       | topConcepts  |                | SKOSConcept       | 0..\* |                  | skos:hasTopConcept |


## DANS PFF Data source
[src_pff.csv](src_pff.csv) is based on the list of PFFs maintained by DANS in Google doc [R.0.2 Curated Support Documentation](https://docs.google.com/spreadsheets/d/1hJtnGgO0FWQj4fMjhSIqtmW2lBt1_lI4fMlkgugHMXQ/edit?usp=sharing) 

<!-- 
changes:

* `isPreferred` column was added, with values: `PreferredFileFormats` and `nonPreferredFileFormats`
* rows addressing more than one format were split into several rows
* renamed: 
    * "Document Hierarchy" -> "Collection"
    * "Fileformat" -> "Concept"
    * 
-->
### DANS PFF Data source Schema

[schemas/src_pff.linkml.yaml](schemas/src_pff.linkml.yaml)

test: `linkml-convert --schema schemas/src_pff.linkml.yaml   -t json src_pff-sample.csv`

### Transforming CSV to Skos RDF

* convert CSV to RDF `linkml-convert --schema schemas/src_pff.linkml.yaml   -t rdf src_pff-sample.csv`
* **next step:** transform RDF(CSV content) through a SPARQL Transform


## Possible future connections with other registries

* NDE Guide to Prefered Formats https://www.wegwijzervoorkeursformaten.nl/index.php/Doorzoek_Register_op_toepassingsgebied
* IANA Media Types http://www.iana.org/assignments/media-types/media-types.xhtml (DCAT-AP recommendation for domain DCAT:Distribution dcat:mediaType)
* EU Vocabularies File Type Named Authority List http://publications.europa.eu/resource/authority/file-type (DCAT-AP dct:format domain DCAT:Distribution, DCAT:DataService)

## DANS PFF in Skosmos

![Concept Scheme](imgs/DPFF-Skosmos03.png)

![a Preferred File Format](imgs/DPFF-Skosmos02.png)

![a Non-Preferred File Format](imgs/DPFF-Skosmos04.png)


# Development

## Development Requirements

### skomos git submodule

* `git submodule add https://github.com/NatLibFi/Skosmos.git`
* append the Skosmos configuration (below) to `Skosmos/dockerfiles/config/config-docker-compose.ttl`
* Start skomos+fuseki docker containers and load voc with `sh skosmos-load-pff.sh`
* Browse DPFF in Skosmos: http://localhost:9090/DPFF

DPFF Skosmos config

```
:DPFF a skosmos:Vocabulary, void:Dataset ;
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
skosmos:sparqlGraph <http://vocabularies.dans.knaw.nl/DPFF/> .
```

### python venv & requirements

* Activate you python virtual environment
* install requirements: `pip install -r requirements.txt`
<!-- * install the sparqlkernel into jupyter `jupyter sparqlkernel install --user` -->


