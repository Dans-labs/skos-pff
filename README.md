# DANS Preferred File Formats as a SKOS Artifact

DANS maintains a list of preferred file formats (PFF) in https://dans.knaw.nl/nl/bestandsformaten/ This repository attempts to encode the information contained in PFF in a SKOS taxonomy.

Similar effort was made in DARIAH project. See https://github.com/ekoi/DANS-File-Formats/blob/additional-formats/dans-file-formats.json

## Requirements
* Req01: maintain PFF list (incl. descriptions, alternatives, domain) in a source online spreadsheet, so that non-tech staff can maintain it
* Req02: include multilingual support: content lebels in both EN and NL    
* Req03: outcome is a skos file based artifact, which can be ingested and browsed by Skosmos 
* Req04: all of the skos artifact's statemets are supported and displayed by Skosmos (see https://github.com/NatLibFi/Skosmos/wiki/Data-Model for the RDF constructs, including but not limited to SKOS, that Skosmos supports)
* Req05: in the skos artifact, create statements that express that A is not a preferred file format, but B is preferred file format to A"
* Req06: include in the source spreasheet and skos artifact, some of the relevant and fitting information include in Eko's [https://github.com/ekoi/DANS-File-Formats/blob/additional-formats/dans-file-formats.json](dans-file-formats.json)
  

## Data source
[Hierarchy-Preferred-Formats.csv](Hierarchy-Preferred-Formats.csv) is based on the list of PFFs maintained by DANS in Google doc [R.0.2 Curated Support Documentation](https://docs.google.com/spreadsheets/d/1hJtnGgO0FWQj4fMjhSIqtmW2lBt1_lI4fMlkgugHMXQ/edit?usp=sharing) 

changes:
* `isPreferred` column was added, with values: `PreferredFileFormats` and `nonPreferredFileFormats`
* rows addressing more than one format were split into several rows
* renamed: 
    * "Document Hierarchy" -> "Collection"
    * "Fileformat" -> "Concept"
    * 

## PFF SKOS artifact Structure

[PreferredFileFormats-controlledlist.ttl](PreferredFileFormats-controlledlist.ttl) is structured around 2 `skos:ConceptScheme`: 
* `:preferredFileFormats`
* `:nonPreferredFileFormats`.

File format (preferred/non-preferred) grouping are defined by instances of `skos:Collection`, ie. `:textDocuments rdf:type skos:Collection`

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

