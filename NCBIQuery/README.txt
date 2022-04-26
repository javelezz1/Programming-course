NCBIQuery

This remote NCBI extractor and exporter will query GenBank data online in database “Nucleotide”,
extract specific gene collection from a set of organisms, and save the queried data to tab separated values file (.tsv).

The following arguments are required in command line:

query: is the query to send to NCBI.
email: the email for presentation to NCBI.
records: the máximum number of records to return.
file: the name of the tsv file to generate.

As an example, note the following call on the command line:

python3 NCBIQuery.py 'Archaea[Organism] AND complete genome[All Fields]' jj@gmail.com 50 arqueas.tsv

This sample asks for a maximum of 50 records of archaeas with complete genome.

EXAMPLE OF FILE RESULT.

.tsv file looks like this:


ID	Locus	Length	Strandedness	Moltype	Topology	Division	Primary-accession	Organism	Taxonomy
2229171692	NZ_CP095400	1398990	double	DNA	circular	CON	NZ_CP095400	Methanonatronarchaeum sp. AMET6-2	Archaea; Euryarchaeota; Methanonatronarchaeia; Methanonatronarchaeales; Methanonatronarchaeaceae; Methanonatronarchaeum; unclassified Methanonatronarchaeum
2229152086	NZ_CP095390	3337253	double	DNA	circular	CON	NZ_CP095390	Natribaculum breve	Archaea; Euryarchaeota; Stenosarchaea group; Halobacteria; Natrialbales; Natrialbaceae; Natribaculum
2229113356	NZ_CP095394	3395034	double	DNA	circular	CON	NZ_CP095394	Natribaculum longum	Archaea; Euryarchaeota; Stenosarchaea group; Halobacteria; Natrialbales; Natrialbaceae; Natribaculum
2228948047	NZ_CP095482	2798302	double	DNA	circular	CON	NZ_CP095482	Halorientalis sp. ZY14	Archaea; Euryarchaeota; Stenosarchaea group; Halobacteria; Halobacteriales; Haloarculaceae; Halorientalis; unclassified Halorientalis
2228936999	NZ_CP095491	3906818	double	DNA	circular	CON	NZ_CP095491	Halovarius sp. SQT-29-1	Archaea; Euryarchaeota; Stenosarchaea group; Halobacteria; Natrialbales; Natrialbaceae; Halovarius; unclassified Halovarius
2228905304	NZ_CP095487	3675221	double	DNA	circular	CON	NZ_CP095487	Halorientalis sp. GDY88	Archaea; Euryarchaeota; Stenosarchaea group; Halobacteria; Halobacteriales; Haloarculaceae; Halorientalis; unclassified Halorientalis
