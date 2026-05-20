# Convert PFF CSV to RDF

## files

* Source data: [Hierarchy-Preferred-Formats.csv](Hierarchy-Preferred-Formats.csv)
* Sample data: [Hierarchy-Preferred-Formats-sample.csv]
* Schema: [schemas/Hierarchy-Preferred-Formats.linkml.yaml](schemas/Hierarchy-Preferred-Formats.linkml.yaml)

## CSV rows conversion to RDF

TO RDF: 

`linkml-convert --schema schemas/Hierarchy-Preferred-Formats.linkml.yaml -t rdf Hierarchy-Preferred-Formats-sample.csv`

sample output:

```
@prefix dpff: <http://vocabularies.dans.knaw.nl/pff> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a dpff:PreferredFileFormatCollection ;
    dpff:row [ a dpff:Row ;
            dpff:Collection "Programming Languages" ;
            dpff:Collection_URL_EN "https://dans.knaw.nl/en/file-formats/programming-languages/"^^xsd:anyURI ;
            dpff:Collection_URL_NL "https://dans.knaw.nl/bestandsformaten/programmeertaal/"^^xsd:anyURI ;
            dpff:Concept "NetCDF" ;
            dpff:Stable_Nederlands_URL "https://dans.knaw.nl/bestandsformaten/programmeertaal/netcdf/"^^xsd:anyURI ;
            dpff:Stable_URL_English "https://dans.knaw.nl/en/file-formats/programming-languages/netcdf/"^^xsd:anyURI ;
            dpff:isPreferred true ],
        [ a dpff:Row ;
            dpff:Collection "Markup language" ;
            dpff:Collection_URL_EN "https://dans.knaw.nl/en/file-formats/markup-language/"^^xsd:anyURI ;
            dpff:Collection_URL_NL "https://dans.knaw.nl/bestandsformaten/opmaaktaal/"^^xsd:anyURI ;
            dpff:Concept "SGML (.sgml)" ;
            dpff:Stable_Nederlands_URL "https://dans.knaw.nl/bestandsformaten/opmaaktaal/sgml/"^^xsd:anyURI ;
            dpff:Stable_URL_English "https://dans.knaw.nl/en/file-formats/markup-language/sgml/"^^xsd:anyURI ;
            dpff:isPreferred false ] .
```

## Working with Python

Generate a Python object model ([schemas/Hierarchy-Preferred-Formats.linkml.py](schemas/Hierarchy-Preferred-Formats.linkml.py)) from a LinkML schema

`gen-python schemas/Hierarchy-Preferred-Formats.linkml.yaml > schemas/pff.py` - Schema to python classes. (Neat, but usure if it is useful)

`python transform_csv2skos.py` - WIP

## TODOs

* [x] remove `URI ending` collumns from Hierarchy-Preferred-Formats.csv
* [ ] fill collumn isPreferred with 0 or 1 in Hierarchy-Preferred-Formats.csv

## ISSUES

## duplicate entities, under different collections

- under different collections & URIs
- either being preferred or not preferred
- *same content*
- probably the same file

Example:

* Collection: Text documents
* URL: https://dans.knaw.nl/en/file-formats/text-documents/pdf-a/
* isPreferred: 1

Text documents,https://dans.knaw.nl/nl/bestandsformaten/tekstdocumenten/,https://dans.knaw.nl/en/file-formats/text-documents/,PDF/A (.pdf),1,https://dans.knaw.nl/en/file-formats/text-documents/pdf-a/,https://dans.knaw.nl/bestandsformaten/tekstdocumenten/pdf-a/

* Collection: Spreadsheets
* URL: https://dans.knaw.nl/en/file-formats/spreadsheets/pdf-a/
* isPreferred: 0

Spreadsheets,https://dans.knaw.nl/bestandsformaten/spreadsheets/,https://dans.knaw.nl/en/file-formats/spreadsheets/,PDF/A (.pdf),0,https://dans.knaw.nl/en/file-formats/spreadsheets/pdf-a/,https://dans.knaw.nl/bestandsformaten/spreadsheets/pdf-a/