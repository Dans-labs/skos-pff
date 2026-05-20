# Convert PFF CSV to RDF

## old code

* Sample data: [src_pff-sample.csv](src_pff-sample.csv)
* Schema: [schemas/src_pff.linkml.yaml](schemas/src_pff.linkml.yaml)


`linkml-convert --schema schemas/src_pff.linkml.yaml -t json src_pff-sample.csv`
`linkml-convert --schema schemas/src_pff.linkml.yaml -t rdf src_pff-sample.csv`

## new code

* Source data: [Hierarchy-Preferred-Formats.csv](Hierarchy-Preferred-Formats.csv)
* Sample data: [Hierarchy-Preferred-Formats-sample.csv]
* Schema: [schemas/Hierarchy-Preferred-Formats.linkml.yaml](schemas/Hierarchy-Preferred-Formats.linkml.yaml)

`linkml-convert --schema schemas/Hierarchy-Preferred-Formats.linkml.yaml -t rdf Hierarchy-Preferred-Formats-sample.csv`

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