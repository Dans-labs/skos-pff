# DANS Preferred File Formats - SKOS Artifacts

DANS maintains a list of preferred file formats (PFF) in https://dans.knaw.nl/nl/bestandsformaten/

This repository attempts to encode the information contained in PFF in a SKOS taxonomy.

Similar effort was made in DARIAH project. See https://github.com/ekoi/DANS-File-Formats/blob/additional-formats/dans-file-formats.json

## Requirements

### skomos git submodule

* `git submodule add https://github.com/NatLibFi/Skosmos.git`
* `sh skosmos-load-pff.sh`

### python venv & requirements

* Activate you python virtual environment
* install requirements: `pip install -r requirements.txt`
* install the sparqlkernel into jupyter `jupyter sparqlkernel install --user`


## Data source
[Hierarchy-Preferred-Formats.csv](Hierarchy-Preferred-Formats.csv) is based on the list of PFFs maintained by DANS in Google doc [R.0.2 Curated Support Documentation](https://docs.google.com/spreadsheets/d/1hJtnGgO0FWQj4fMjhSIqtmW2lBt1_lI4fMlkgugHMXQ/edit?usp=sharing) 

changes:

* `isPreferred` column was added, with values: `PreferredFileFormats` and `nonPreferredFileFormats`
* rows addressing more than one format were split into several rows
* renamed: 
    * "Document Hierarchy" -> "Collection"
    * "Fileformat" -> "Concept"
    * 

## SKOS taxonomy structure

<!-- TODO -->

[PreferredFileFormats-controlledlist.ttl](PreferredFileFormats-controlledlist.ttl) is structured around 2 `skos:ConceptScheme`: 
* `:preferredFileFormats`
* `:nonPreferredFileFormats`.

File format grouping are defined by instances of `skos:Collection`, ie. `:textDocuments rdf:type skos:Collection`

Each file format is a concept, that is either in `:preferredFileFormats` or `:nonPreferredFileFormats` `skos:ConceptScheme` and is `skos:member` of one or more `skos:Collections`. 
In the case of `:nonPreferredFileFormats` formats, the property `dct:isReplaceBy` to indicate the alternative, preferred file formats.


Example:

```ttl
:ODT rdf:type skos:Concept ;
      skos:inScheme :preferredFileFormats;
      skos:member :textDocuments .


:doc rdf:type skos:Concept  ;
      skos:inScheme :nonPreferredFileFormats;
      skos:member :textDocuments ;
      dct:isReplacedBy  :PDFA, :ODT .

```

