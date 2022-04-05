UNIPROT TEXT FORMAT

The Uniprot_sprot.dat text data file, is a text file with information about proteins. The file can be download from
https://www.uniprot.org/downloads . When in the page, download the file “Reviewed (Swiss-Prot)” in text format.
Please do not download xml or fasta. After downloading, decompress the file. This file is about 3.4 Gb, at the
date of elaboration of this document.
Every record in the file starts with the field ID, and ends with the pair of characters // (slash, slash). Fields have a 2
character identification as the first 2 characters. Sequence field SQ, is followed by aminoacid sequence with no code,
until the record ends.

SPECIFICATIONS - UNIPROT_BROWSER_2.0.PY

This is a query tool to query protein records, given as a filter the name of fields and values using the and logic.
For field/value separator, use the sequence VALUE.in.FIELD separated by .and. concatenators [ VALUE.in.FIELD.and.VALUE.in.FIELD ...]
All the queries have to match on the same record to keep that record.

TOOL USAGE

COMMAND.
● A user use the command line to write the name of the command, like % > python3 uprotview.py filter fieldlist or commands
ARGUMENTS
● First argument is the filename of the uniprot data.
● Second argument is the filter to apply to the data (the QUERY).
○ VALUE.in.FIELD.and.VALUE.in.FIELD
● Following arguments can be FIELDNAMES to show, or COMMANDS to execute, all of this separated by
spaces.
○ [field1 field2 command1 command2 . . .]

BEHAVIOR OF THE COMMAND LINE TOOL WHEN FILTERS ARE USED

FILENAMES & QUERY VALIDATIONS.

1. If a data file name is not provided, the message ‘File Name is required’ is printed and the tool stops.

tom@Toms-iMac prpy % python3 uniprot.py
File name is required.
tom@Toms-iMac prpy %

2. If a data file name is provided, but the file does not exist, the message “File does not exist” appears.

tom@Toms-iMac prpy % python3 uniprot.py data/dat_uniprot.d
File does not exist.
tom@Toms-iMac prpy %

3. If a data file name is provided, the file does exist, but no query is given, the message “File does not exist”
appears.

tom@Toms-iMac prpy % python3 uniprot.py data/dat_uniprot.dat
Query is required.
tom@Toms-iMac prpy %

QUERY WITH VERY BASIC FILTER BUT NO FIELDNAMES OR COMMANDS.

4. The most basic usage of a query is a field with a value.

tom@Toms-iMac prpy % python3 uniprot.py data/dat_uniprot.dat Frog.in.OS
ID HBA1_COTGO Reviewed; 143 AA.
AC P84653;
DT 03-OCT-2006, integrated into UniProtKB/Swiss-Prot.
DT 23-JAN-2007, sequence version 2.
DT 07-APR-2021, entry version 48.
DE RecName: Full=Hemoglobin subunit alpha-1;
DE AltName: Full=Alpha-1-globin;
...

In this example, only the query Frog.in.OS was given. Then, the full fields of every record including the text Frog in
the field OS is shown.

QUERY WITH AND OPERATOR TO FILTER USING TWO FILTERS CONNECTED WITH AND.

5. A query with two fields using AND is as follows:

tom@Toms-iMac prpy % python3 uniprot.py data/dat_uniprot.dat Frog.in.OS.and.Perciformes.in.OC
ID HBA1_COTGO Reviewed; 143 AA.
AC P84653;
DT 03-OCT-2006, integrated into UniProtKB/Swiss-Prot.
DT 23-JAN-2007, sequence version 2.
DE RecName: Full=Hemoglobin subunit alpha-1;
DE AltName: Full=Alpha-1-globin;
GN Name=hba1;
OS Cottoperca gobio (Frogmouth) (Aphritis gobio).
OC Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi;
OC Actinopterygii; Neopterygii; Teleostei; Neoteleostei; Acanthomorphata;
OC Eupercaria; Perciformes; Notothenioidei; Bovichtidae; Cottoperca.
OX NCBI_TaxID=56716;
RN [1] {ECO:0000305}
RP PROTEIN SEQUENCE OF 2-143, AND SUBUNIT.
RC TISSUE=Blood {ECO:0000269|Ref.1};
...

In this example, only the query Frog.in.OS..and.Perciformes.in.OC was given. Then, the full fields of every record is
shown, and only for records including the text Frog in the field OS and the Perciformes text in the field OC.
Note the usage of the operator .and. , obligating only the records matching both fields.

QUERY WITH AND OPERATOR TO FILTER USING N FILTERS, ALL CONNECTED WITH AND.

6. A query with more than 2 fields using AND is shown:

tom@Toms-iMac prpy % python3 uniprot.py data/dat_uniprot.dat
Globin.in.DR.and.Flavohemoprotein.in.FT.and.Yersinia.in.OC
ID HMP_YERPE Reviewed; 396 AA.
AC Q8ZCR0; Q0WCZ6; Q74SP6; Q7CJP3;
DT 13-SEP-2004, integrated into UniProtKB/Swiss-Prot.
DT 29-SEP-2021, entry version 126.
DE AltName: Full=Flavohemoglobin {ECO:0000255|HAMAP-Rule:MF_01252};
DE AltName: Full=Nitric oxide dioxygenase {ECO:0000255|HAMAP-Rule:MF_01252};
DE Short=NO oxygenase {ECO:0000255|HAMAP-Rule:MF_01252};
DE Short=NOD {ECO:0000255|HAMAP-Rule:MF_01252};
GN Name=hmp {ECO:0000255|HAMAP-Rule:MF_01252};
GN Synonyms=fsrB, hmp2, hmpA, hmpX; OrderedLocusNames=YPO2908, y1321, YP_2547;
OS Yersinia pestis.
OC Bacteria; Proteobacteria; Gammaproteobacteria; Enterobacterales;
OC Yersiniaceae; Yersinia.
OX NCBI_TaxID=632;
RN [1]
RP NUCLEOTIDE SEQUENCE [LARGE SCALE GENOMIC DNA].
RC STRAIN=CO-92 / Biovar Orientalis;
RX PubMed=11586360; DOI=10.1038/35097083;
RA Parkhill J., Wren B.W., Thomson N.R., Titball R.W., Holden

In this example, the filter is on fields DR, FT and OC, containing values Globin, Flavohemoprotein and Yersinia
respectively.

BEHAVIOR OF THE COMMAND LINE TOOL WHEN FIELD NAMES AFTER THE FILTER

7. Fieldnames after the filter are used to specify which fields are shown in output.

tom@Toms-iMac prpy % python3 uniprot.py data/dat_uniprot.dat
Globin.in.DR.and.Flavohemoprotein.in.FT ID OC SQ
ID FHBA_DICDI Reviewed; 397 AA.
OC Eukaryota; Amoebozoa; Evosea; Eumycetozoa; Dictyostelia; Dictyosteliales;
OC Dictyosteliaceae; Dictyostelium.
SQ SEQUENCE 397 AA; 43925 MW; 9641037821908183 CRC64;
MSLSQQSISI IKATVPVLQV HGVNITTTFY RNMFKANPQL LNIFNHSNQR EGKQQNALAN
TVLQAAIHID KLNELNLAPI VHKHVALGVL PEHYPIVGTN LLGAIKEVLQ DAATDEILGA
WGEAYGVIAQ AFIDAEAALY KVTEEQIGGW RDTREFIVDR KVEESSNIIS FYFKPADGKP
IATYIPGQYI TIKVPLTLEN GEQRTHIRHY SLSDTPSEQY YRISVKKEDA LKKSDPNGVV
SNHLHANVKV GDKVLLSPPA GDYVVDQLSS NPILLVSGGV GITPLLSMAK ATLAKQPERE
VTFVHSSKNK QYQPFANELS QLEKSNKVKV STVHSETDGQ ITKDKLEKFI NPSQIKDTKV
FICGPVSFMS AINKQLIELG YPKENISYEI FGPLTNV
ID FHBB_DICDI Reviewed; 423 AA.
OC Eukaryota; Amoebozoa; Evosea; Eumycetozoa; Dictyostelia; Dictyosteliales;
OC Dictyosteliaceae; Dictyostelium.
SQ SEQUENCE 423 AA; 48206 MW; 3768C17E89D6D70C CRC64;
MLSQKSIQII KSTVPLLEKY GVEITSLFYK NMFEAQPQFL NIFNHSNQRN QKQPVALANT
ILQSAIHIEK LNEINLMPIV HKHVALGITP EMYPIVGAHL LGAMKTVMQD EATPEIMAAW
TEAYRAVAQA FMDAEEDLYF ETEEQIGGWK DTREFVVDRI EEETPLIKSF YFKAYDGKEI
ATYIPGQYIT VKITLPGDGV DVPTDKMRTY VRHYSLSDKP NDEYYRISIK KELGKNTPNG
IVSNHFHNNI KVGDVVPMSV PAGDFVVNND SETPILLICG GVGINPLFSM LKETLVQQPD
RKINFIFSTH CESSQPFKEE LKQLEDDYKE TGNLKINLVY SENQGHINKE IIEKYSTQHV
DQAEIAETDV YICGPVPFMM QVNKDLLQLG FHKENVHYEL FGPLTPVLEE NQMLRGVKNI
IEN
ID FHP_CANAL Reviewed; 398 AA.
OC Eukaryota; Fungi; Dikarya; Ascomycota; Saccharomycotina; Saccharomycetes;
OC Saccharomycetales; Debaryomycetaceae; Candida/Lodderomyces clade; Candida.
SQ SEQUENCE 398 AA; 45819 MW; 3E3827CC14DF04BA CRC64;
MTVEYETKQL TPAQIKIILD TVPILEEAGE TLTQKFYQRM IGNYDEVKPF FNTTDQKLLR
QPKILAFALL NYAKNIEDLT PLTDFVKQIV VKHIGLQVLP EHYPIVGTCL IQTMVELLPP
EIANKDFLEA WTIAYGNLAK LLIDLEAAEY AKQPWRWFKD FKVTRIVQEC KDVKSVYFTP
VDKDLLPLPK PERGQYLCFR WKLPGEEFEI SREYSVSEFP KENEYRISVR HVPGGKISGY
IHNNLKVGDI LKVAPPAGNF VYDPATDKEL IFVAGGIGIT PLLSMIERAL EEGKNVKLLY
SNRSAETRAF GNLFKEYKSK FGDKFQAIEY FSEDNNTDDK IVIDKAFNRK LTTDDLDFIA
PEHDVYLVGP REFMKDIKEH LGKKNVPVKL EYFGPYDP

In this example, the filter is for records with filter Globin.in.DR.and.Flavohemoprotein.in.FT , and the fields to show
are ID, OC, and the protein sequence (SQ field, and all the fields until the end of the record). This query returns 47
records, but only 3 are shown in the example.

COMMANDS WITH NO FIELD NAMES PRESENT

User can include different commands together. No field names are requiered to get additional information about the
query.

COMMAND SHOWALL

8. The command SHOWALL, if present in the list of fields, says ‘SHOW ALL FIELDS’. This is equivalent to not
using any field at all.

tom@Toms-iMac prpy % python3 uniprot.py data/dat_uniprot.dat
Frog.in.OS.and.Perciformes.in.OC SHOWALL
ID HBA1_COTGO Reviewed; 143 AA.
AC P84653;
DT 03-OCT-2006, integrated into UniProtKB/Swiss-Prot.
DT 23-JAN-2007, sequence version 2.
DE RecName: Full=Hemoglobin subunit alpha-1;
DE AltName: Full=Alpha-1-globin;
GN Name=hba1;
OS Cottoperca gobio (Frogmouth) (Aphritis gobio).
OC Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi;
OC Actinopterygii; Neopterygii; Teleostei; Neoteleostei; Acanthomorphata;
OC Eupercaria; Perciformes; Notothenioidei; Bovichtidae; Cottoperca.
OX NCBI_TaxID=56716;
RN [1] {ECO:0000305}
RP PROTEIN SEQUENCE OF 2-143, AND SUBUNIT.
RC TISSUE=Blood {ECO:0000269|Ref.1};
…

COMMAND COUNTALL

9. The command COUNTALL, if present in the list of fields, says ‘SHOW THE TOTAL OF RECORDS
PROCESSED AND PRESENT IN THE FILE DATABASE’. Every new version of the uniprot file has a
different size.
IF only the COUNTALL is used, no record information is show, but the total of the records analyzed is
shown.

tom@Toms-iMac prpy % python3 uniprot.py data/dat_uniprot.dat
Frog.in.OS.and.Perciformes.in.OC COUNTALL
565928
tom@Toms-iMac prpy %

As the sample shows, there are approximately a half million of protein records in the file.

COMMAND COUNT

The command COUNT, if present in the list of fields, says ‘SHOW THE TOTAL OF RECORDS IN THE FILE
DATABASE MATCHING THE GIVEN FILTER’.

tom@Toms-iMac prpy % python3 uniprot.py data/dat_uniprot.dat Homo.in.OC COUNT
20381
tom@Toms-iMac prpy %

As the sample shows, there are 20381 protein records with the word Homo in the taxonomy field OC.

COMMAND COUNT and COUNTALL

11. If the commands COUNT and COUNTALL are present simultaneously, the total of records matching, and the
total of records in the text database are shown. Additional percentage appears.

tom@Toms-iMac prpy % python3 uniprot.py data/dat_uniprot.dat Homo.in.OC COUNT COUNTALL
20381
565928
3.6013%
tom@Toms-iMac prpy %

As the sample shows, there are 20381 protein records with the word Homo in the taxonomy field OC
between a total of 565928 records. The 20381 fraction corresponds to 3.6% of the total.

COMMANDS WITH FIELD NAMES PRESENT

User can include different commands together with field names. The behavior is the combination of presentation of
records with the normal behavior of the commands.

FIELD NAMES WITH COUNT COMMANDS

12. If field names are given with count commands, the fields of record are shown, and counters are shown at the
final.

tom@Toms-iMac prpy % python3 uniprot.py data/dat_uniprot.dat
Globin.in.DR.and.Flavohemoprotein.in.FT COUNTALL COUNT ID
ID FHBA_DICDI Reviewed; 397 AA.
ID FHBB_DICDI Reviewed; 423 AA.
ID FHP_CANAL Reviewed; 398 AA.
ID FHP_CANNO Reviewed; 390 AA.
ID FHP_SCHPO Reviewed; 427 AA.
ID FHP_YEAST Reviewed; 399 AA.
ID HMP1_GIAIA Reviewed; 457 AA.
ID HMP2_GIAIA Reviewed; 457 AA.
ID HMP_ALKHC Reviewed; 411 AA.
ID HMP_BACAN Reviewed; 402 AA.
ID HMP_BACC1 Reviewed; 402 AA.
ID HMP_BACCR Reviewed; 402 AA.
ID HMP_BACHK Reviewed; 402 AA.
ID HMP_BACSU Reviewed; 399 AA.
ID HMP_BORBR Reviewed; 402 AA.
ID HMP_BORPA Reviewed; 402 AA.
ID HMP_BORPE Reviewed; 402 AA.
ID HMP_BURST Reviewed; 393 AA.
ID HMP_CHRVO Reviewed; 404 AA.
ID HMP_CUPNH Reviewed; 403 AA.
ID HMP_DEIRA Reviewed; 403 AA.
ID HMP_DICD3 Reviewed; 395 AA.
ID HMP_ECO57 Reviewed; 396 AA.
ID HMP_ECOL6 Reviewed; 396 AA.
ID HMP_ECOLI Reviewed; 396 AA.
ID HMP_GIAIB Reviewed; 458 AA.
ID HMP_GIAIC Reviewed; 458 AA.
ID HMP_OCEIH Reviewed; 406 AA.
ID HMP_PECAS Reviewed; 396 AA.
ID HMP_PHOLL Reviewed; 396 AA.
ID HMP_PHOPR Reviewed; 394 AA.
ID HMP_PSEAE Reviewed; 393 AA.
ID HMP_PSEPK Reviewed; 392 AA.
ID HMP_RHIME Reviewed; 403 AA.
ID HMP_RHOBA Reviewed; 408 AA.
ID HMP_SALCH Reviewed; 396 AA.
ID HMP_SALPA Reviewed; 396 AA.
ID HMP_SALTI Reviewed; 396 AA.
ID HMP_SALTY Reviewed; 396 AA.
ID HMP_SHIFL Reviewed; 396 AA.
ID HMP_VIBCH Reviewed; 394 AA.
ID HMP_VIBPA Reviewed; 394 AA.
ID HMP_VIBVU Reviewed; 394 AA.
ID HMP_VIBVY Reviewed; 394 AA.
ID HMP_XYLFA Reviewed; 397 AA.
ID HMP_XYLFT Reviewed; 397 AA.
ID HMP_YERPE Reviewed; 396 AA.
47
565928
0.0083%
tom@Toms-iMac prpy %

TAXONS COMMAND

TAXONS command is a special command in the tool. When present, the total for each taxon in the fields OC of all
records is summarized as a final result..

tom@Toms-iMac prpy % python3 uniprot.py data/dat_uniprot.dat
Globin.in.DR.and.Flavohemoprotein.in.FT COUNTALL COUNT TAXONS
47
565928
0.0083%
Eukaryota 10
Amoebozoa 2
Evosea 2
Eumycetozoa 2
Dictyostelia 2
Dictyosteliales 2
Dictyosteliaceae 2
Dictyostelium 2
Fungi 4
Dikarya 4
Ascomycota 4
Saccharomycotina 3
Saccharomycetes 3
Saccharomycetales 3
Debaryomycetaceae 1
Candida/Lodderomyces clade 1
Candida 1
Pichiaceae 1
Pichia 1
Taphrinomycotina 1
Schizosaccharomycetes 1
Schizosaccharomycetales 1
Schizosaccharomycetaceae 1
Schizosaccharomyces 1
Saccharomycetaceae 1
Saccharomyces 1
Metamonada 4
Diplomonadida 4
Hexamitidae 4
Giardiinae 4
Giardia 4
Bacteria 37
Firmicutes 7
Bacilli 7
Bacillales 7
Bacillaceae 7
Alkalihalobacillus 1
Bacillus 5
Bacillus cereus group 4
Proteobacteria 28
Betaproteobacteria 6
Burkholderiales 5
Alcaligenaceae 3
Bordetella 3
Burkholderiaceae 2
Burkholderia 1
Neisseriales 1
Chromobacteriaceae 1
Chromobacterium 1
Cupriavidus 1
Deinococcus-Thermus 1
Deinococci 1
Deinococcales 1
Deinococcaceae 1
Deinococcus 1
Gammaproteobacteria 21
Enterobacterales 12
Pectobacteriaceae 2
Dickeya 1
Enterobacteriaceae 8
Escherichia 3
Oceanobacillus 1
Pectobacterium 1
Morganellaceae 1
Photorhabdus 1
Vibrionales 5
Vibrionaceae 5
Photobacterium 1
Pseudomonadales 2
Pseudomonadaceae 2
Pseudomonas 2
Alphaproteobacteria 1
Hyphomicrobiales 1
Rhizobiaceae 1
Sinorhizobium/Ensifer group 1
Sinorhizobium 1
Planctomycetes 1
Planctomycetia 1
Pirellulales 1
Pirellulaceae 1
Rhodopirellula 1
Salmonella 4
Shigella 1
Vibrio 4
Xanthomonadales 2
Xanthomonadaceae 2
Xylella 2
Yersiniaceae 1
Yersinia 1
tom@Toms-iMac prpy %

In this sample, the normal output for counters are at the first three lines, and the counts of the totals of all the taxa
related is given.

FASTA COMMAND

FASTA command is a special command in the tool. When present, the total for each taxon in the fields OC of all
records is summarized as a final result.
It follows the normal rules for a protein fasta file: a header, and the sequence represented by lines of 80 amino acids.
IMPORTANT: FASTA command avoids any other output; only the fasta records are emitted, no matter which other
commands are present.

tom@Toms-iMac prpy % python3 uniprot.py data/dat_uniprot.dat
Globin.in.DR.and.Flavohemoprotein.in.FT FASTA
>id=FHBA_DICDI;acc=Q9UAG7; Q54D74;name=Dictyostelium discoideum (Slime mold).
MSLSQQSISIIKATVPVLQVHGVNITTTFYRNMFKANPQLLNIFNHSNQREGKQQNALANTVLQAAIHIDKLNELNLAPI
VHKHVALGVLPEHYPIVGTNLLGAIKEVLQDAATDEILGAWGEAYGVIAQAFIDAEAALYKVTEEQIGGWRDTREFIVDR
KVEESSNIISFYFKPADGKPIATYIPGQYITIKVPLTLENGEQRTHIRHYSLSDTPSEQYYRISVKKEDALKKSDPNGVV
SNHLHANVKVGDKVLLSPPAGDYVVDQLSSNPILLVSGGVGITPLLSMAKATLAKQPEREVTFVHSSKNKQYQPFANELS
QLEKSNKVKVSTVHSETDGQITKDKLEKFINPSQIKDTKVFICGPVSFMSAINKQLIELGYPKENISYEIFGPLTNV
>id=FHBB_DICDI;acc=Q54D73; Q9UAG6;name=Dictyostelium discoideum (Slime mold).
MLSQKSIQIIKSTVPLLEKYGVEITSLFYKNMFEAQPQFLNIFNHSNQRNQKQPVALANTILQSAIHIEKLNEINLMPIV
HKHVALGITPEMYPIVGAHLLGAMKTVMQDEATPEIMAAWTEAYRAVAQAFMDAEEDLYFETEEQIGGWKDTREFVVDRI
EEETPLIKSFYFKAYDGKEIATYIPGQYITVKITLPGDGVDVPTDKMRTYVRHYSLSDKPNDEYYRISIKKELGKNTPNG
IVSNHFHNNIKVGDVVPMSVPAGDFVVNNDSETPILLICGGVGINPLFSMLKETLVQQPDRKINFIFSTHCESSQPFKEE
LKQLEDDYKETGNLKINLVYSENQGHINKEIIEKYSTQHVDQAEIAETDVYICGPVPFMMQVNKDLLQLGFHKENVHYEL
FGPLTPVLEENQMLRGVKNIIEN
>id=FHP_CANAL;acc=Q59MV9; A0A1D8PTL9; Q59MX2;name=Candida albicans (strain SC5314 / ATCC MYA-2876) (Yeast).
MTVEYETKQLTPAQIKIILDTVPILEEAGETLTQKFYQRMIGNYDEVKPFFNTTDQKLLRQPKILAFALLNYAKNIEDLT
PLTDFVKQIVVKHIGLQVLPEHYPIVGTCLIQTMVELLPPEIANKDFLEAWTIAYGNLAKLLIDLEAAEYAKQPWRWFKD
FKVTRIVQECKDVKSVYFTPVDKDLLPLPKPERGQYLCFRWKLPGEEFEISREYSVSEFPKENEYRISVRHVPGGKISGY
IHNNLKVGDILKVAPPAGNFVYDPATDKELIFVAGGIGITPLLSMIERALEEGKNVKLLYSNRSAETRAFGNLFKEYKSK
FGDKFQAIEYFSEDNNTDDKIVIDKAFNRKLTTDDLDFIAPEHDVYLVGPREFMKDIKEHLGKKNVPVKLEYFGPYDP
>id=FHP_CANNO;acc=Q03331;name=Candida norvegensis (Yeast) (Candida mycoderma).
MSAAKQLFKIVPLTPTEINFLQSLAPVVKEHGVTVTSTMYKYMFQTYPEVRSYFNMTNQKTGRQPKVLAFSLYQYILHLN
DLTPISGFVNQIVLKHCGLGIKPDQYPVVGESLVQAFKMVLGEAADEHFVEVFKKAYGNLAQTLIDAEASVYKTLAWEEF
KDFRVTKLVKEAEDVTSVYLTPVDGFKLKPIIPGEYISFRWDIHNPDITDIQPREYSISQDVKENEYRISVRDIGIVSDY
INKKLQVGDIVPVHAPVGTMKYDSISKKGKVAVLAGGIGITPMIPIIEHALKDGKDVELYYSNRSYQSEPFREFFSNLEK
ENNGKFKLNNYISAENQKLQVKDLEHINPDEYDVYLLGPVAYMHEFKTYLVGKGVSDLKMEFFGPTDPDC
>id=FHP_SCHPO;acc=Q9URY5;name=Schizosaccharomyces pombe (strain 972 / ATCC 24843) (Fission yeast).
MSSVEVNRENADVANTNRQANLAEGYEIKELNESQKQYIRSSIPILESSGVNLTKAFYQKMLGNYPEVLPYFNKAHQISL
SQPRILAFALLNYAKNIDDLTSLSAFMDQIVVKHVGLQIKAEHYPIVGHCLLSTMQELLPSDVATPAFLEAWTTAYGNLA
KILIDSEKKVYQSQPWNGFVEFKVTELINESSDVKSVYLGPKDPAFRISHAHPGQYVSVLWEIPGLSHKTLREYSLSNRV
DTCRNQFRISVRRVAGGVVSNFVHDNLKVGDIVGVSPPAGNFVYKRSEENVNRPLLCFAGGIGITPLIPIIETALLDGRK
VNFCYSSRNYVSRPFKQWLEQLKLKYKENLKLKEFFSEESSVTKEQIVDEVMTRIINEEDLEKLDLSECDIYMLGPNNYM
RFVKQELVKLGVEPNKVQSEFFGPYIP

For simplicity reasons, In this sample, only 4 fasta records are shown.


DATABASE COMMANDS

DBINSERT
The purpose of this command is to export data from Swiss-Uniprot text database to a SQL database.

Use the argument DBINSERT db=sqlite_database_name to export the filtered records to the given SQL database.
The schema of the database is as follows:



CREATE TABLE IF NOT EXISTS "Comments" (
  "id_protein" TEXT NOT NULL,
  "comment" TEXT NOT NULL,
FOREIGN KEY("id_protein") REFERENCES "Proteins"("idprotein") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "Dates" (
  "id_protein" TEXT NOT NULL,
  "date" TEXT NOT NULL,
  "event" TEXT NOT NULL,
FOREIGN KEY("id_protein") REFERENCES "Proteins"("idprotein") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "Features" (
  "id_protein" TEXT NOT NULL,
  "type" TEXT NOT NULL,
  "loc" TEXT,
  "description" INTEGER,
FOREIGN KEY("id_protein") REFERENCES "Proteins"("idprotein") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "Names" (
  "id_protein" TEXT NOT NULL,
  "name" INTEGER NOT NULL,
FOREIGN KEY("id_protein") REFERENCES "Proteins"("idprotein") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "Fasta" (
  "id_protein" TEXT NOT NULL,
  "header" TEXT NOT NULL,
  "sequence" TEXT NOT NULL,
FOREIGN KEY("id_protein") REFERENCES "Proteins"("idprotein") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "Codes" (
  "id_protein" TEXT NOT NULL,
  "code" TEXT NOT NULL,
FOREIGN KEY("id_protein") REFERENCES "Proteins"("idprotein") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "Proteins" (
  "idprotein" TEXT NOT NULL,
  "accession" TEXT NOT NULL,
  "names" TEXT NOT NULL,
  "taxonomy" TEXT NOT NULL,
  "taxonomyid" TEXT NOT NULL,
  "sequence" TEXT NOT NULL,
  "AA_number" INTEGER NOT NULL DEFAULT 0,
  "keywords" TEXT,
  "predicted" TEXT,
  "orfnames" TEXT,
PRIMARY KEY("idprotein")


The fields of origin for each type of data are the following:

'id' : 'ID',
'orfnames' : 'GN',
'predicted' : 'PE',
'keywords' : 'KW',
'accession' : 'AC',
'name' : 'OS',
'taxa' : 'OC',
'taxaid' : 'OX',
'sequence' : 'SQ',
'dates' : 'DT',
'names' : 'DE',
'codes' : 'DR',
'features' : 'FT',
'comments' : 'CC',
'fasta' : 'FA'


During the process, no information will be printed, except if VERBOSE command was given.
VERBOSE command, when present, prints the information being inserted into the database.

If a record to insert already exists on the database, it will be replaced with the new information.
For every 100 records inserted, the message “records inserted = XXXX” will be printed.
At the end of the execution, print the total of records inserted, and the name of the database where the
records were inserted:
“XXXX records inserted on database YYYYYYY”.

tom@Toms-iMac uniprotquery % python3 uniprot.py $HOME/tempodata/dat_uniprot.dat "Transit
peptide.in.KW".and."Choline catabolism".in.DR DBINSERT db=$HOME/tempodata/finalprot.db

12 records inserted on database /Users/tom/tempodata/finalprot.db


tom@Toms-iMac uniprotquery % python3 uniprot.py $HOME/tempodata/dat_uniprot.dat
Homo.in.OC.and.Phosphoprotein.in.KW.and.dehydrogenase.in.DE.and.VAVA.in.SQ DBINSERT
db=$HOME/tempodata/finalprot.db VERBOSE


--TABLE PROTEIN--
[['ADPPT_HUMAN', 'Q9NRN7; B2R6D1; B4DDW7; Q9C068; Q9P0Q3; Q9UG80; Q9Y389;', '309', 'Name=AASDHPPT; ORFNames=CGI-80, HAH-P, HSPC223, x0005;', 'Homo sapiens (Human).', 'Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;Eutheria; Euarchontoglires; Primates; Haplorrhini; Catarrhini; Hominidae;Homo.', 'NCBI_TaxID=9606;', '3D-structure; Alternative splicing; Cytoplasm; Direct protein sequencing;Magnesium; Metal-binding; Phosphoprotein; Reference proteome; Transferase.', '1: Evidence at protein level;', 'SQ   SEQUENCE   309 AA;  35776 MW;  6263E302600FDDED CRC64;MVFPAKRFCLVPSMEGVRWAFSCGTWLPSRAEWLLAVRSIQPEEKERIGQFVFARDAKAAMAGRLMIRKLVAEKLNIPWNHIRLQRTAKG\nKPVLAKDSSNPYPNFNFNISHQGDYAVLAAEPELQVGIDIMKTSFPGRGSIPEFFHIMKRKFTNKEWETIRSFKDEWTQLDMFYRNWALK\nESFIKAIGVGLGFELQRLEFDLSPLNLDIGQVYKETRLFLDGEEEKEWAFEESKIDEHHFVAVALRKPDGSRHQDVPSQDDSKPTQRQFT\nILNFNDLMSSAVPMTPEDPSFWDCFCFTEEIPIRNGTKS\n']]

--TABLE DATES--
['ADPPT_HUMAN', '08-NOV-2005', ' integrated into UniProtKB/Swiss-Prot.']
['ADPPT_HUMAN', '08-NOV-2005', ' sequence version 2.']
['ADPPT_HUMAN', '29-SEP-2021', ' entry version 159.']

--TABLE NAMES--
['ADPPT_HUMAN', 'RecName: Full=L-aminoadipate-semialdehyde dehydrogenase-phosphopantetheinyl transferase;      EC=2.7.8.7 {ECO:0000269|PubMed:12815048, ECO:0000269|PubMed:18022563};']
['ADPPT_HUMAN', "AltName: Full=4'-phosphopantetheinyl transferase;"]
['ADPPT_HUMAN', 'AltName: Full=Alpha-aminoadipic semialdehyde dehydrogenase-phosphopantetheinyl transferase;      Short=AASD-PPT;']
['ADPPT_HUMAN', 'AltName: Full=LYS5 ortholog;']

--TABLE CODES--
['ADPPT_HUMAN', 'EMBL; AF302110; AAG30872.1; -; mRNA.']
['ADPPT_HUMAN', 'EMBL; AF151838; AAD34075.1; ALT_FRAME; mRNA.']
['ADPPT_HUMAN', 'EMBL; AF151057; AAF36143.1; -; mRNA.']
['ADPPT_HUMAN', 'EMBL; AF136978; AAG49439.1; -; mRNA.']
['ADPPT_HUMAN', 'EMBL; AF201943; AAF86879.1; ALT_INIT; mRNA.']
['ADPPT_HUMAN', 'EMBL; AK312529; BAG35428.1; -; mRNA.']
['ADPPT_HUMAN', 'EMBL; AK293362; BAG56878.1; -; mRNA.']
['ADPPT_HUMAN', 'EMBL; AP001001; -; NOT_ANNOTATED_CDS; Genomic_DNA.']
['ADPPT_HUMAN', 'EMBL; CH471065; EAW67078.1; -; Genomic_DNA.']
['ADPPT_HUMAN', 'EMBL; BC015470; AAH15470.1; -; mRNA.']
['ADPPT_HUMAN', 'EMBL; BC016728; AAH16728.1; -; mRNA.']
['ADPPT_HUMAN', 'EMBL; AL050073; CAB43257.1; -; mRNA.']
['ADPPT_HUMAN', 'CCDS; CCDS31664.1; -. [Q9NRN7-1]']
['ADPPT_HUMAN', 'PIR; T08733; T08733.']
['ADPPT_HUMAN', 'RefSeq; NP_056238.2; NM_015423.2. [Q9NRN7-1]']
['ADPPT_HUMAN', 'PDB; 2BYD; X-ray; 2.00 A; A=14-309.']
['ADPPT_HUMAN', 'PDB; 2C43; X-ray; 1.93 A; A=14-309.']
['ADPPT_HUMAN', 'PDB; 2CG5; X-ray; 2.70 A; A=14-309.']
['ADPPT_HUMAN', 'PDBsum; 2BYD; -.']
['ADPPT_HUMAN', 'PDBsum; 2C43; -.']
['ADPPT_HUMAN', 'PDBsum; 2CG5; -.']
['ADPPT_HUMAN', 'SMR; Q9NRN7; -.']
['ADPPT_HUMAN', 'BioGRID; 121927; 49.']
['ADPPT_HUMAN', 'IntAct; Q9NRN7; 23.']
['ADPPT_HUMAN', 'STRING; 9606.ENSP00000278618; -.']
['ADPPT_HUMAN', 'ChEMBL; CHEMBL3137295; -.']
['ADPPT_HUMAN', 'SwissLipids; SLP:000001260; -.']
['ADPPT_HUMAN', 'iPTMnet; Q9NRN7; -.']
['ADPPT_HUMAN', 'PhosphoSitePlus; Q9NRN7; -.']
['ADPPT_HUMAN', 'SwissPalm; Q9NRN7; -.']
['ADPPT_HUMAN', 'BioMuta; AASDHPPT; -.']
['ADPPT_HUMAN', 'DMDM; 81170356; -.']
['ADPPT_HUMAN', 'EPD; Q9NRN7; -.']
['ADPPT_HUMAN', 'jPOST; Q9NRN7; -.']
['ADPPT_HUMAN', 'MassIVE; Q9NRN7; -.']
['ADPPT_HUMAN', 'MaxQB; Q9NRN7; -.']
['ADPPT_HUMAN', 'PaxDb; Q9NRN7; -.']
['ADPPT_HUMAN', 'PeptideAtlas; Q9NRN7; -.']
['ADPPT_HUMAN', 'PRIDE; Q9NRN7; -.']
['ADPPT_HUMAN', 'ProteomicsDB; 3900; -.']
['ADPPT_HUMAN', 'ProteomicsDB; 82396; -. [Q9NRN7-1]']
['ADPPT_HUMAN', 'Antibodypedia; 18138; 217 antibodies.']
['ADPPT_HUMAN', 'DNASU; 60496; -.']
['ADPPT_HUMAN', 'Ensembl; ENST00000278618; ENSP00000278618; ENSG00000149313. [Q9NRN7-1]']
['ADPPT_HUMAN', 'Ensembl; ENST00000525660; ENSP00000437144; ENSG00000149313. [Q9NRN7-2]']
['ADPPT_HUMAN', 'GeneID; 60496; -.']
['ADPPT_HUMAN', 'KEGG; hsa:60496; -.']
['ADPPT_HUMAN', 'UCSC; uc001pjc.2; human. [Q9NRN7-1]']
['ADPPT_HUMAN', 'CTD; 60496; -.']
['ADPPT_HUMAN', 'DisGeNET; 60496; -.']
['ADPPT_HUMAN', 'GeneCards; AASDHPPT; -.']
['ADPPT_HUMAN', 'HGNC; HGNC:14235; AASDHPPT.']
['ADPPT_HUMAN', 'HPA; ENSG00000149313; Low tissue specificity.']
['ADPPT_HUMAN', 'MIM; 607756; gene.']
['ADPPT_HUMAN', 'neXtProt; NX_Q9NRN7; -.']
['ADPPT_HUMAN', 'OpenTargets; ENSG00000149313; -.']
['ADPPT_HUMAN', 'PharmGKB; PA24368; -.']
['ADPPT_HUMAN', 'VEuPathDB; HostDB:ENSG00000149313; -.']
['ADPPT_HUMAN', 'eggNOG; KOG0945; Eukaryota.']
['ADPPT_HUMAN', 'GeneTree; ENSGT00390000004663; -.']
['ADPPT_HUMAN', 'HOGENOM; CLU_1854476_0_0_1; -.']
['ADPPT_HUMAN', 'InParanoid; Q9NRN7; -.']
['ADPPT_HUMAN', 'OMA; IPWSEIR; -.']
['ADPPT_HUMAN', 'OrthoDB; 960416at2759; -.']
['ADPPT_HUMAN', 'PhylomeDB; Q9NRN7; -.']
['ADPPT_HUMAN', 'TreeFam; TF313753; -.']
['ADPPT_HUMAN', 'BioCyc; MetaCyc:HS14278-MONOMER; -.']
['ADPPT_HUMAN', 'BRENDA; 2.7.8.7; 2681.']
['ADPPT_HUMAN', 'PathwayCommons; Q9NRN7; -.']
['ADPPT_HUMAN', 'Reactome; R-HSA-199220; Vitamin B5 (pantothenate) metabolism.']
['ADPPT_HUMAN', 'SABIO-RK; Q9NRN7; -.']
['ADPPT_HUMAN', 'BioGRID-ORCS; 60496; 306 hits in 995 CRISPR screens.']
['ADPPT_HUMAN', 'ChiTaRS; AASDHPPT; human.']
['ADPPT_HUMAN', 'EvolutionaryTrace; Q9NRN7; -.']
['ADPPT_HUMAN', 'GeneWiki; AASDHPPT; -.']
['ADPPT_HUMAN', 'GenomeRNAi; 60496; -.']
['ADPPT_HUMAN', 'Pharos; Q9NRN7; Tbio.']
['ADPPT_HUMAN', 'PRO; PR:Q9NRN7; -.']
['ADPPT_HUMAN', 'Proteomes; UP000005640; Chromosome 11.']
['ADPPT_HUMAN', 'RNAct; Q9NRN7; protein.']
['ADPPT_HUMAN', 'Bgee; ENSG00000149313; Expressed in neocortex and 255 other tissues.']
['ADPPT_HUMAN', 'ExpressionAtlas; Q9NRN7; baseline and differential.']
['ADPPT_HUMAN', 'Genevisible; Q9NRN7; HS.']
['ADPPT_HUMAN', 'GO; GO:0005829; C:cytosol; IDA:UniProtKB.']
['ADPPT_HUMAN', 'GO; GO:0070062; C:extracellular exosome; HDA:UniProtKB.']
['ADPPT_HUMAN', 'GO; GO:0008897; F:holo-[acyl-carrier-protein] synthase activity; IDA:UniProtKB.']
['ADPPT_HUMAN', 'GO; GO:0000287; F:magnesium ion binding; IDA:UniProtKB.']
['ADPPT_HUMAN', 'GO; GO:0019878; P:lysine biosynthetic process via aminoadipic acid; IBA:GO_Central.']
['ADPPT_HUMAN', 'GO; GO:0015939; P:pantothenate metabolic process; TAS:Reactome.']
['ADPPT_HUMAN', 'Gene3D; 3.90.470.20; -; 2.']
['ADPPT_HUMAN', 'InterPro; IPR008278; 4-PPantetheinyl_Trfase_dom.']
['ADPPT_HUMAN', 'InterPro; IPR037143; 4-PPantetheinyl_Trfase_dom_sf.']
['ADPPT_HUMAN', 'Pfam; PF01648; ACPS; 1.']
['ADPPT_HUMAN', 'SUPFAM; SSF56214; SSF56214; 2.']

--TABLE FEATURES--
['ADPPT_HUMAN', 'CHAIN', '1..309', ' /note="L-aminoadipate-semialdehyde dehydrogenase- phosphopantetheinyl transferase" /id="PRO_0000175736"']
['ADPPT_HUMAN', 'REGION', '86..91', ' /note="Coenzyme A binding" /evidence="ECO:0000269|PubMed:18022563, ECO:0007744|PDB:2C43, ECO:0007744|PDB:2CG5"']
['ADPPT_HUMAN', 'REGION', '108..111', ' /note="Coenzyme A binding" /evidence="ECO:0000269|PubMed:18022563, ECO:0007744|PDB:2C43, ECO:0007744|PDB:2CG5"']
['ADPPT_HUMAN', 'REGION', '181..185', ' /note="Coenzyme A binding" /evidence="ECO:0000269|PubMed:18022563, ECO:0007744|PDB:2C43, ECO:0007744|PDB:2CG5"']
['ADPPT_HUMAN', 'METAL', '129', ' /note="Magnesium" /evidence="ECO:0000269|PubMed:18022563, ECO:0007744|PDB:2C43"']
['ADPPT_HUMAN', 'METAL', '181', ' /note="Magnesium" /evidence="ECO:0000269|PubMed:18022563, ECO:0007744|PDB:2C43"']
['ADPPT_HUMAN', 'BINDING', '47', ' /note="Coenzyme A" /evidence="ECO:0000269|PubMed:18022563, ECO:0007744|PDB:2C43, ECO:0007744|PDB:2CG5"']
['ADPPT_HUMAN', 'MOD_RES', '258', ' /note="Phosphoserine" /evidence="ECO:0007744|PubMed:17525332, ECO:0007744|PubMed:18669648, ECO:0007744|PubMed:20068231, ECO:0007744|PubMed:23186163"']
['ADPPT_HUMAN', 'VAR_SEQ', '138', ' /note="R -> T (in isoform 2)" /evidence="ECO:0000303|PubMed:14702039" /id="VSP_055783"']
['ADPPT_HUMAN', 'VAR_SEQ', '139..309', ' /note="Missing (in isoform 2)" /evidence="ECO:0000303|PubMed:14702039" /id="VSP_055784"']
['ADPPT_HUMAN', 'MUTAGEN', '47', ' /note="R->A: Reduces affinity for magnesium by 7-fold, and holo-[acyl-carrier-protein] synthase activity by 2-fold." /evidence="ECO:0000269|PubMed:18022563"']
['ADPPT_HUMAN', 'MUTAGEN', '86', ' /note="R->A: Reduces affinity for magnesium and coenzyme A, and reduces holo-[acyl-carrier-protein] synthase activity by 7-fold." /evidence="ECO:0000269|PubMed:18022563"']
['ADPPT_HUMAN', 'MUTAGEN', '111', ' /note="H->A: Reduces affinity for magnesium by 75-fold, and holo-[acyl-carrier-protein] synthase activity by 150-fold." /evidence="ECO:0000269|PubMed:18022563"']
['ADPPT_HUMAN', 'MUTAGEN', '112', ' /note="Q->E: Reduces affinity for magnesium by 200-fold and abolishes holo-[acyl-carrier-protein] synthase activity; when associated with Q-181." /evidence="ECO:0000269|PubMed:18022563"']
['ADPPT_HUMAN', 'MUTAGEN', '129', ' /note="D->A: Reduces affinity for magnesium by 10-fold, and holo-[acyl-carrier-protein] synthase activity by 30000- fold." /evidence="ECO:0000269|PubMed:18022563"']
['ADPPT_HUMAN', 'MUTAGEN', '181', ' /note="E->A: Reduces affinity for magnesium by 40-fold, and holo-[acyl-carrier-protein] synthase activity by 32000- fold." /evidence="ECO:0000269|PubMed:18022563"']
['ADPPT_HUMAN', 'MUTAGEN', '181', ' /note="E->Q: Reduces affinity for magnesium by 20-fold, and holo-[acyl-carrier-protein] synthase activity by 6500- fold." /evidence="ECO:0000269|PubMed:18022563"']
['ADPPT_HUMAN', 'MUTAGEN', '185', ' /note="K->A: Reduces holo-[acyl-carrier-protein] synthase activity by 2000-fold, with only minor change in the affinity for magnesium and coenzyme A." /evidence="ECO:0000269|PubMed:18022563"']
['ADPPT_HUMAN', 'CONFLICT', '136..141', ' /note="PGRGSI -> FQVVVQF (in Ref. 4; AAG49439)" /evidence="ECO:0000305"']
['ADPPT_HUMAN', 'CONFLICT', '307..309', ' /note="TKS -> YKVMMIP (in Ref. 4; AAG49439)" /evidence="ECO:0000305"']
['ADPPT_HUMAN', 'STRAND', '17..21', ' /evidence="ECO:0007829|PDB:2C43"']
['ADPPT_HUMAN', 'HELIX', '23..25', ' /evidence="ECO:0007829|PDB:2C43"']
['ADPPT_HUMAN', 'HELIX', '30..38', ' /evidence="ECO:0007829|PDB:2C43"']
['ADPPT_HUMAN', 'HELIX', '42..49', ' /evidence="ECO:0007829|PDB:2C43"']
['ADPPT_HUMAN', 'HELIX', '54..74', ' /evidence="ECO:0007829|PDB:2C43"']
['ADPPT_HUMAN', 'HELIX', '79..81', ' /evidence="ECO:0007829|PDB:2C43"']
['ADPPT_HUMAN', 'STRAND', '84..86', ' /evidence="ECO:0007829|PDB:2C43"']
['ADPPT_HUMAN', 'STRAND', '92..94', ' /evidence="ECO:0007829|PDB:2C43"']
['ADPPT_HUMAN', 'STRAND', '102..104', ' /evidence="ECO:0007829|PDB:2C43"']
['ADPPT_HUMAN', 'STRAND', '106..112', ' /evidence="ECO:0007829|PDB:2C43"']
['ADPPT_HUMAN', 'STRAND', '115..132', ' /evidence="ECO:0007829|PDB:2C43"']
['ADPPT_HUMAN', 'STRAND', '137..139', ' /evidence="ECO:0007829|PDB:2C43"']
['ADPPT_HUMAN', 'HELIX', '141..147', ' /evidence="ECO:0007829|PDB:2C43"']
['ADPPT_HUMAN', 'HELIX', '149..151', ' /evidence="ECO:0007829|PDB:2C43"']
['ADPPT_HUMAN', 'HELIX', '154..160', ' /evidence="ECO:0007829|PDB:2C43"']
['ADPPT_HUMAN', 'STRAND', '163..165', ' /evidence="ECO:0007829|PDB:2C43"']
['ADPPT_HUMAN', 'HELIX', '166..187', ' /evidence="ECO:0007829|PDB:2C43"']
['ADPPT_HUMAN', 'HELIX', '190..192', ' /evidence="ECO:0007829|PDB:2BYD"']
['ADPPT_HUMAN', 'HELIX', '195..197', ' /evidence="ECO:0007829|PDB:2C43"']
['ADPPT_HUMAN', 'STRAND', '198..201', ' /evidence="ECO:0007829|PDB:2C43"']
['ADPPT_HUMAN', 'STRAND', '203..206', ' /evidence="ECO:0007829|PDB:2BYD"']
['ADPPT_HUMAN', 'STRAND', '217..220', ' /evidence="ECO:0007829|PDB:2C43"']
['ADPPT_HUMAN', 'STRAND', '228..236', ' /evidence="ECO:0007829|PDB:2C43"']
['ADPPT_HUMAN', 'STRAND', '239..246', ' /evidence="ECO:0007829|PDB:2C43"']
['ADPPT_HUMAN', 'STRAND', '270..272', ' /evidence="ECO:0007829|PDB:2C43"']
['ADPPT_HUMAN', 'HELIX', '274..277', ' /evidence="ECO:0007829|PDB:2C43"']
['ADPPT_HUMAN', 'TURN', '278..280', ' /evidence="ECO:0007829|PDB:2C43"']
['ADPPT_HUMAN', 'HELIX', '289..291', ' /evidence="ECO:0007829|PDB:2C43"']
['ADPPT_HUMAN', 'HELIX', '298..300', ' /evidence="ECO:0007829|PDB:2C43"']
['ADPPT_HUMAN', 'TURN', '305..307', ' /evidence="ECO:0007829|PDB:2BYD"']

--TABLE COMMENTS--
['ADPPT_HUMAN', " FUNCTION: Catalyzes the post-translational modification of target proteins by phosphopantetheine. Can transfer the 4'-phosphopantetheine moiety from coenzyme A, regardless of whether the CoA is presented in the free thiol form or as an acetyl thioester, to a serine residue of a broad range of acceptors including the acyl carrier domain of FASN. {ECO:0000269|PubMed:11286508, ECO:0000269|PubMed:12815048, ECO:0000269|PubMed:18022563}."]
['ADPPT_HUMAN', " CATALYTIC ACTIVITY: Reaction=apo-[ACP] + CoA = adenosine 3',5'-bisphosphate + H(+) + holo-   [ACP]; Xref=Rhea:RHEA:12068, Rhea:RHEA-COMP:9685, Rhea:RHEA-   COMP:9690, ChEBI:CHEBI:15378, ChEBI:CHEBI:29999, ChEBI:CHEBI:57287,   ChEBI:CHEBI:58343, ChEBI:CHEBI:64479; EC=2.7.8.7;   Evidence={ECO:0000269|PubMed:12815048, ECO:0000269|PubMed:18022563}; PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:12069;   Evidence={ECO:0000305|PubMed:12815048};"]      
['ADPPT_HUMAN', " CATALYTIC ACTIVITY: Reaction=acetyl-CoA + apo-[ACP] = acetyl-[ACP] + adenosine 3',5'-   bisphosphate + H(+); Xref=Rhea:RHEA:46564, Rhea:RHEA-COMP:9621,   Rhea:RHEA-COMP:9690, ChEBI:CHEBI:15378, ChEBI:CHEBI:29999,   ChEBI:CHEBI:57288, ChEBI:CHEBI:58343, ChEBI:CHEBI:78446;   Evidence={ECO:0000269|PubMed:12815048, ECO:0000269|PubMed:18022563}; PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:46565;   Evidence={ECO:0000305|PubMed:12815048};"]
['ADPPT_HUMAN', ' COFACTOR: Name=Mg(2+); Xref=ChEBI:CHEBI:18420;   Evidence={ECO:0000269|PubMed:12815048, ECO:0000269|PubMed:18022563}; Note=Binds 1 Mg(2+) ion. {ECO:0000269|PubMed:12815048, ECO:0000269|PubMed:18022563};']
['ADPPT_HUMAN', ' BIOPHYSICOCHEMICAL PROPERTIES: Kinetic parameters:   KM=0.44 mM for magnesium {ECO:0000269|PubMed:18022563};   KM=0.025 mM for coenzyme A {ECO:0000269|PubMed:18022563}; pH dependence:   Optimum pH is 6-10. {ECO:0000269|PubMed:12815048};']
['ADPPT_HUMAN', ' SUBUNIT: Monomer. {ECO:0000269|PubMed:12815048}.']
['ADPPT_HUMAN', ' INTERACTION: Q9NRN7; O43186: CRX; NbExp=3; IntAct=EBI-740884, EBI-748171; Q9NRN7; Q5JST6: EFHC2; NbExp=3; IntAct=EBI-740884, EBI-2349927; Q9NRN7; Q8IUQ4: SIAH1; NbExp=3; IntAct=EBI-740884, EBI-747107; Q9NRN7; Q12933: TRAF2; NbExp=7; IntAct=EBI-740884, EBI-355744; Q9NRN7; Q9UPT9: USP22; NbExp=6; IntAct=EBI-740884, EBI-723510; Q9NRN7; Q9UPT9-2: USP22; NbExp=11; IntAct=EBI-740884, EBI-12074414;']
['ADPPT_HUMAN', ' SUBCELLULAR LOCATION: Cytoplasm, cytosol {ECO:0000269|PubMed:12815048}.']
['ADPPT_HUMAN', ' ALTERNATIVE PRODUCTS: Event=Alternative splicing; Named isoforms=2; Name=1;   IsoId=Q9NRN7-1; Sequence=Displayed; Name=2;   IsoId=Q9NRN7-2; Sequence=VSP_055783, VSP_055784;']
['ADPPT_HUMAN', ' TISSUE SPECIFICITY: Detected in heart, skeletal muscle, placenta, testis, brain, pancreas, liver and kidney. {ECO:0000269|PubMed:11286508, ECO:0000269|PubMed:12815048}.']
['ADPPT_HUMAN', ' SIMILARITY: Belongs to the P-Pant transferase superfamily. AcpS family. {ECO:0000305}.']
['ADPPT_HUMAN', ' SEQUENCE CAUTION: Sequence=AAD34075.1; Type=Frameshift; Evidence={ECO:0000305}; Sequence=AAF86879.1; Type=Erroneous initiation; Evidence={ECO:0000305};']
['ADPPT_HUMAN', '---------------------------------------------------------------------------']
['ADPPT_HUMAN', 'Copyrighted by the UniProt Consortium, see https://www.uniprot.org/terms']
['ADPPT_HUMAN', 'Distributed under the Creative Commons Attribution (CC BY 4.0) License']
['ADPPT_HUMAN', '---------------------------------------------------------------------------']

--TABLE FASTA--
['ADPPT_HUMAN', 'id=ADPPT_HUMAN;accesion=Q9NRN7;B2R6D1;B4DDW7;Q9C068;Q9P0Q3;Q9UG80;Q9Y389;name=Homo sapiens (Human).', 'MVFPAKRFCLVPSMEGVRWAFSCGTWLPSRAEWLLAVRSIQPEEKERIGQFVFARDAKAAMAGRLMIRKLVAEKLNIPWNHIRLQRTAKG\nKPVLAKDSSNPYPNFNFNISHQGDYAVLAAEPELQVGIDIMKTSFPGRGSIPEFFHIMKRKFTNKEWETIRSFKDEWTQLDMFYRNWALK\nESFIKAIGVGLGFELQRLEFDLSPLNLDIGQVYKETRLFLDGEEEKEWAFEESKIDEHHFVAVALRKPDGSRHQDVPSQDDSKPTQRQFT\nILNFNDLMSSAVPMTPEDPSFWDCFCFTEEIPIRNGTKS\n']

--TABLE PROTEIN--
[['ODPX_HUMAN', 'O00330; B4DW62; D3DR11; E9PB14; E9PBP7; O60221; Q96FV8; Q99783;', '501', 'Name=PDHX; Synonyms=PDX1;', 'Homo sapiens (Human).', 'Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;Eutheria; Euarchontoglires; Primates; Haplorrhini; Catarrhini; Hominidae;Homo.', 'NCBI_TaxID=9606;', '3D-structure; Acetylation; Alternative splicing; Lipoyl; Mitochondrion;Phosphoprotein; Reference proteome; Transit peptide.', '1: Evidence at protein level;', 'SQ   SEQUENCE   501 AA;  54122 MW;  9CF0C1DAE9E12EF9 CRC64;MAASWRLGCDPRLLRYLVGFPGRRSVGLVKGALGWSVSRGANWRWFHSTQWLRGDPIKILMPSLSPTMEEGNIVKWLKKEGEAVSAGDAL\nCEIETDKAVVTLDASDDGILAKIVVEEGSKNIRLGSLIGLIVEEGEDWKHVEIPKDVGPPPPVSKPSEPRPSPEPQISIPVKKEHIPGTL\nRFRLSPAARNILEKHSLDASQGTATGPRGIFTKEDALKLVQLKQTGKITESRPTPAPTATPTAPSPLQATAGPSYPRPVIPPVSTPGQPN\nAVGTFTEIPASNIRRVIAKRLTESKSTVPHAYATADCDLGAVLKVRQDLVKDDIKVSVNDFIIKAAAVTLKQMPDVNVSWDGEGPKQLPF\nIDISVAVATDKGLLTPIIKDAAAKGIQEIADSVKALSKKARDGKLLPEEYQGGSFSISNLGMFGIDEFTAVINPPQACILAVGRFRPVLK\nLTEDEEGNAKLQQRQLITVTMSSDSRVVDDELATRFLKSFKANLENPIRLA\n']]

--TABLE DATES--
['ODPX_HUMAN', '15-JUL-1999', ' integrated into UniProtKB/Swiss-Prot.']
['ODPX_HUMAN', '24-JAN-2001', ' sequence version 3.']
['ODPX_HUMAN', '29-SEP-2021', ' entry version 207.']

--TABLE NAMES--
['ODPX_HUMAN', 'RecName: Full=Pyruvate dehydrogenase protein X component, mitochondrial;']
['ODPX_HUMAN', 'AltName: Full=Dihydrolipoamide dehydrogenase-binding protein of pyruvate dehydrogenase complex;']
['ODPX_HUMAN', 'AltName: Full=E3-binding protein;      Short=E3BP;']
['ODPX_HUMAN', 'AltName: Full=Lipoyl-containing pyruvate dehydrogenase complex component X;']
['ODPX_HUMAN', 'AltName: Full=proX;']
['ODPX_HUMAN', 'Flags: Precursor;']

--TABLE CODES--
['ODPX_HUMAN', 'EMBL; AF001437; AAB66315.1; -; mRNA.']
['ODPX_HUMAN', 'EMBL; Y13145; CAA73606.1; -; mRNA.']
['ODPX_HUMAN', 'EMBL; U82328; AAC39661.1; -; mRNA.']
['ODPX_HUMAN', 'EMBL; AJ298105; CAC18649.1; -; Genomic_DNA.']
['ODPX_HUMAN', 'EMBL; AK301384; BAG62924.1; -; mRNA.']
['ODPX_HUMAN', 'EMBL; AC107928; -; NOT_ANNOTATED_CDS; Genomic_DNA.']
['ODPX_HUMAN', 'EMBL; AL138810; -; NOT_ANNOTATED_CDS; Genomic_DNA.']
['ODPX_HUMAN', 'EMBL; AL356215; -; NOT_ANNOTATED_CDS; Genomic_DNA.']
['ODPX_HUMAN', 'EMBL; CH471064; EAW68158.1; -; Genomic_DNA.']
['ODPX_HUMAN', 'EMBL; CH471064; EAW68160.1; -; Genomic_DNA.']
['ODPX_HUMAN', 'EMBL; BC010389; AAH10389.1; -; mRNA.']
['ODPX_HUMAN', 'EMBL; U79296; AAB50223.1; -; mRNA.']
['ODPX_HUMAN', 'CCDS; CCDS53616.1; -. [O00330-2]']
['ODPX_HUMAN', 'CCDS; CCDS7896.1; -. [O00330-1]']
['ODPX_HUMAN', 'RefSeq; NP_001128496.1; NM_001135024.1. [O00330-3]']
['ODPX_HUMAN', 'RefSeq; NP_001159630.1; NM_001166158.1. [O00330-2]']
['ODPX_HUMAN', 'RefSeq; NP_003468.2; NM_003477.2. [O00330-1]']
['ODPX_HUMAN', 'PDB; 1ZY8; X-ray; 2.59 A; K/L/M/N/O=54-274.']
['ODPX_HUMAN', 'PDB; 2DNC; NMR; -; A=57-141.']
['ODPX_HUMAN', 'PDB; 2F5Z; X-ray; 2.18 A; K/L/M/N/O=173-228.']
['ODPX_HUMAN', 'PDB; 2F60; X-ray; 1.55 A; K=173-228.']
['ODPX_HUMAN', 'PDB; 6H60; EM; 6.00 A; A=1-501.']
['ODPX_HUMAN', 'PDBsum; 1ZY8; -.']
['ODPX_HUMAN', 'PDBsum; 2DNC; -.']
['ODPX_HUMAN', 'PDBsum; 2F5Z; -.']
['ODPX_HUMAN', 'PDBsum; 2F60; -.']
['ODPX_HUMAN', 'PDBsum; 6H60; -.']
['ODPX_HUMAN', 'SMR; O00330; -.']
['ODPX_HUMAN', 'BioGRID; 113737; 76.']
['ODPX_HUMAN', 'DIP; DIP-29026N; -.']
['ODPX_HUMAN', 'IntAct; O00330; 25.']
['ODPX_HUMAN', 'MINT; O00330; -.']
['ODPX_HUMAN', 'STRING; 9606.ENSP00000227868; -.']
['ODPX_HUMAN', 'iPTMnet; O00330; -.']
['ODPX_HUMAN', 'PhosphoSitePlus; O00330; -.']
['ODPX_HUMAN', 'SwissPalm; O00330; -.']
['ODPX_HUMAN', 'BioMuta; PDHX; -.']
['ODPX_HUMAN', 'EPD; O00330; -.']
['ODPX_HUMAN', 'jPOST; O00330; -.']
['ODPX_HUMAN', 'MassIVE; O00330; -.']
['ODPX_HUMAN', 'MaxQB; O00330; -.']
['ODPX_HUMAN', 'PaxDb; O00330; -.']
['ODPX_HUMAN', 'PeptideAtlas; O00330; -.']
['ODPX_HUMAN', 'PRIDE; O00330; -.']
['ODPX_HUMAN', 'ProteomicsDB; 19121; -.']
['ODPX_HUMAN', 'ProteomicsDB; 19268; -.']
['ODPX_HUMAN', 'ProteomicsDB; 47851; -. [O00330-1]']
['ODPX_HUMAN', 'Antibodypedia; 25893; 300 antibodies.']
['ODPX_HUMAN', 'DNASU; 8050; -.']
['ODPX_HUMAN', 'Ensembl; ENST00000227868; ENSP00000227868; ENSG00000110435. [O00330-1]']
['ODPX_HUMAN', 'Ensembl; ENST00000430469; ENSP00000415695; ENSG00000110435. [O00330-2]']
['ODPX_HUMAN', 'GeneID; 8050; -.']
['ODPX_HUMAN', 'KEGG; hsa:8050; -.']
['ODPX_HUMAN', 'UCSC; uc001mvt.4; human. [O00330-1]']
['ODPX_HUMAN', 'CTD; 8050; -.']
['ODPX_HUMAN', 'DisGeNET; 8050; -.']
['ODPX_HUMAN', 'GeneCards; PDHX; -.']
['ODPX_HUMAN', 'HGNC; HGNC:21350; PDHX.']
['ODPX_HUMAN', 'HPA; ENSG00000110435; Tissue enhanced (skeletal).']
['ODPX_HUMAN', 'MalaCards; PDHX; -.']
['ODPX_HUMAN', 'MIM; 245349; phenotype.']
['ODPX_HUMAN', 'MIM; 608769; gene.']
['ODPX_HUMAN', 'neXtProt; NX_O00330; -.']
['ODPX_HUMAN', 'OpenTargets; ENSG00000110435; -.']
['ODPX_HUMAN', 'Orphanet; 255182; Pyruvate dehydrogenase E3-binding protein deficiency.']
['ODPX_HUMAN', 'PharmGKB; PA134976445; -.']
['ODPX_HUMAN', 'VEuPathDB; HostDB:ENSG00000110435; -.']
['ODPX_HUMAN', 'eggNOG; KOG0557; Eukaryota.']
['ODPX_HUMAN', 'GeneTree; ENSGT00940000156046; -.']
['ODPX_HUMAN', 'HOGENOM; CLU_016733_10_2_1; -.']
['ODPX_HUMAN', 'InParanoid; O00330; -.']
['ODPX_HUMAN', 'OMA; QVTVIKH; -.']
['ODPX_HUMAN', 'OrthoDB; 747232at2759; -.']
['ODPX_HUMAN', 'PhylomeDB; O00330; -.']
['ODPX_HUMAN', 'TreeFam; TF332256; -.']
['ODPX_HUMAN', 'BioCyc; MetaCyc:ENSG00000110435-MONOMER; -.']
['ODPX_HUMAN', 'PathwayCommons; O00330; -.']
['ODPX_HUMAN', 'Reactome; R-HSA-204174; Regulation of pyruvate dehydrogenase (PDH) complex.']
['ODPX_HUMAN', 'Reactome; R-HSA-389661; Glyoxylate metabolism and glycine degradation.']
['ODPX_HUMAN', 'Reactome; R-HSA-5362517; Signaling by Retinoic Acid.']
['ODPX_HUMAN', 'Reactome; R-HSA-70268; Pyruvate metabolism.']
['ODPX_HUMAN', 'SIGNOR; O00330; -.']
['ODPX_HUMAN', 'BioGRID-ORCS; 8050; 8 hits in 1018 CRISPR screens.']
['ODPX_HUMAN', 'ChiTaRS; PDHX; human.']
['ODPX_HUMAN', 'EvolutionaryTrace; O00330; -.']
['ODPX_HUMAN', 'GeneWiki; E3_binding_protein; -.']
['ODPX_HUMAN', 'GenomeRNAi; 8050; -.']
['ODPX_HUMAN', 'Pharos; O00330; Tbio.']
['ODPX_HUMAN', 'PRO; PR:O00330; -.']
['ODPX_HUMAN', 'Proteomes; UP000005640; Chromosome 11.']
['ODPX_HUMAN', 'RNAct; O00330; protein.']
['ODPX_HUMAN', 'Bgee; ENSG00000110435; Expressed in skeletal muscle tissue and 245 other tissues.']
['ODPX_HUMAN', 'ExpressionAtlas; O00330; baseline and differential.']
['ODPX_HUMAN', 'Genevisible; O00330; HS.']
['ODPX_HUMAN', 'GO; GO:0005759; C:mitochondrial matrix; TAS:Reactome.']
['ODPX_HUMAN', 'GO; GO:0005739; C:mitochondrion; IBA:GO_Central.']
['ODPX_HUMAN', 'GO; GO:0045254; C:pyruvate dehydrogenase complex; IDA:UniProtKB.']
['ODPX_HUMAN', 'GO; GO:0016746; F:acyltransferase activity; IEA:InterPro.']
['ODPX_HUMAN', 'GO; GO:0061732; P:mitochondrial acetyl-CoA biosynthetic process from pyruvate; IC:MGI.']
['ODPX_HUMAN', 'Gene3D; 3.30.559.10; -; 1.']
['ODPX_HUMAN', 'Gene3D; 4.10.320.10; -; 1.']
['ODPX_HUMAN', 'InterPro; IPR003016; 2-oxoA_DH_lipoyl-BS.']
['ODPX_HUMAN', 'InterPro; IPR001078; 2-oxoacid_DH_actylTfrase.']
['ODPX_HUMAN', 'InterPro; IPR000089; Biotin_lipoyl.']
['ODPX_HUMAN', 'InterPro; IPR023213; CAT-like_dom_sf.']
['ODPX_HUMAN', 'InterPro; IPR036625; E3-bd_dom_sf.']
['ODPX_HUMAN', 'InterPro; IPR004167; PSBD.']
['ODPX_HUMAN', 'InterPro; IPR011053; Single_hybrid_motif.']
['ODPX_HUMAN', 'Pfam; PF00198; 2-oxoacid_dh; 1.']
['ODPX_HUMAN', 'Pfam; PF00364; Biotin_lipoyl; 1.']
['ODPX_HUMAN', 'Pfam; PF02817; E3_binding; 1.']
['ODPX_HUMAN', 'SUPFAM; SSF47005; SSF47005; 1.']
['ODPX_HUMAN', 'SUPFAM; SSF51230; SSF51230; 1.']
['ODPX_HUMAN', 'PROSITE; PS50968; BIOTINYL_LIPOYL; 1.']
['ODPX_HUMAN', 'PROSITE; PS00189; LIPOYL; 1.']
['ODPX_HUMAN', 'PROSITE; PS51826; PSBD; 1.']

--TABLE FEATURES--
['ODPX_HUMAN', 'TRANSIT', '1..53', ' /note="Mitochondrion" /evidence="ECO:0000250"']
['ODPX_HUMAN', 'CHAIN', '54..501', ' /note="Pyruvate dehydrogenase protein X component, mitochondrial" /id="PRO_0000020484"']
['ODPX_HUMAN', 'DOMAIN', '56..132', ' /note="Lipoyl-binding" /evidence="ECO:0000255|PROSITE-ProRule:PRU01066"']
['ODPX_HUMAN', 'DOMAIN', '183..220', ' /note="Peripheral subunit-binding (PSBD)" /evidence="ECO:0000255|PROSITE-ProRule:PRU01170"']
['ODPX_HUMAN', 'REGION', '142..175', ' /note="Disordered" /evidence="ECO:0000256|SAM:MobiDB-lite"']
['ODPX_HUMAN', 'REGION', '225..268', ' /note="Disordered" /evidence="ECO:0000256|SAM:MobiDB-lite"']
['ODPX_HUMAN', 'COMPBIAS', '145..166', ' /note="Pro residues" /evidence="ECO:0000256|SAM:MobiDB-lite"']
['ODPX_HUMAN', 'MOD_RES', '97', ' /note="N6-lipoyllysine" /evidence="ECO:0000255|PROSITE-ProRule:PRU01066, ECO:0000269|PubMed:25525879"']
['ODPX_HUMAN', 'MOD_RES', '194', ' /note="N6-acetyllysine" /evidence="ECO:0007744|PubMed:19608861"']
['ODPX_HUMAN', 'MOD_RES', '196', ' /note="Phosphoserine" /evidence="ECO:0007744|PubMed:24275569"']
['ODPX_HUMAN', 'MOD_RES', '394', ' /note="N6-succinyllysine" /evidence="ECO:0000250|UniProtKB:Q8BKZ9"']
['ODPX_HUMAN', 'VAR_SEQ', '2..53', ' /note="AASWRLGCDPRLLRYLVGFPGRRSVGLVKGALGWSVSRGANWRWFHSTQWLR -> QSGGAEGSPGAGRTGRGPGSGKAPPAEISSGAPDFPG (in isoform 3)" /evidence="ECO:0000305" /id="VSP_053817"']
['ODPX_HUMAN', 'VAR_SEQ', '115..341', ' /note="Missing (in isoform 2)" /evidence="ECO:0000305" /id="VSP_045271"']
['ODPX_HUMAN', 'VARIANT', '23', ' /note="R -> C (in dbSNP:rs1049306)" /evidence="ECO:0000269|PubMed:9242632" /id="VAR_046619"']
['ODPX_HUMAN', 'VARIANT', '101', ' /note="T -> A (in dbSNP:rs11539202)" /id="VAR_046620"']
['ODPX_HUMAN', 'VARIANT', '370', ' /note="D -> V (in dbSNP:rs17850649)" /evidence="ECO:0000269|PubMed:15489334" /id="VAR_046621"']
['ODPX_HUMAN', 'MUTAGEN', '183', ' /note="R->A: Strongly decreased DLD binding." /evidence="ECO:0000269|PubMed:16442803"']
['ODPX_HUMAN', 'MUTAGEN', '185', ' /note="S->A: Strongly decreased DLD binding." /evidence="ECO:0000269|PubMed:16442803"']
['ODPX_HUMAN', 'MUTAGEN', '186', ' /note="P->A: Strongly decreased DLD binding." /evidence="ECO:0000269|PubMed:16442803"']
['ODPX_HUMAN', 'MUTAGEN', '187', ' /note="A->M: Strongly decreased DLD binding." /evidence="ECO:0000269|PubMed:16442803"']
['ODPX_HUMAN', 'MUTAGEN', '189', ' /note="R->A: Strongly decreased DLD binding." /evidence="ECO:0000269|PubMed:16442803"']
['ODPX_HUMAN', 'MUTAGEN', '190', ' /note="N->A: Decreased DLD binding." /evidence="ECO:0000269|PubMed:16442803, ECO:0000269|PubMed:20160912"']
['ODPX_HUMAN', 'MUTAGEN', '190', ' /note="N->K: Moderately decreased interaction with DLD." /evidence="ECO:0000269|PubMed:20160912"']
['ODPX_HUMAN', 'MUTAGEN', '193', ' /note="E->A: Strongly decreased DLD binding." /evidence="ECO:0000269|PubMed:16442803"']
['ODPX_HUMAN', 'MUTAGEN', '208', ' /note="R->A: Strongly decreased DLD binding." /evidence="ECO:0000269|PubMed:16442803"']
['ODPX_HUMAN', 'MUTAGEN', '208', ' /note="R->D: Decreased interaction with DLD." /evidence="ECO:0000269|PubMed:20160912"']
['ODPX_HUMAN', 'MUTAGEN', '210', ' /note="I->A: Strongly decreased DLD binding." /evidence="ECO:0000269|PubMed:16442803"']
['ODPX_HUMAN', 'MUTAGEN', '210', ' /note="I->R: Decreased interaction with DLD." /evidence="ECO:0000269|PubMed:20160912"']
['ODPX_HUMAN', 'MUTAGEN', '210', ' /note="I->S: Decreased interaction with DLD." /evidence="ECO:0000269|PubMed:20160912"']
['ODPX_HUMAN', 'MUTAGEN', '213', ' /note="K->A: Strongly decreased DLD binding." /evidence="ECO:0000269|PubMed:16442803"']
['ODPX_HUMAN', 'MUTAGEN', '214', ' /note="E->A: Strongly decreased DLD binding." /evidence="ECO:0000269|PubMed:16442803"']
['ODPX_HUMAN', 'CONFLICT', '41', ' /note="A -> R (in Ref. 3; AAC39661)" /evidence="ECO:0000305"']
['ODPX_HUMAN', 'CONFLICT', '251', ' /note="A -> S (in Ref. 1; AAB66315 and 2; CAA73606)" /evidence="ECO:0000305"']
['ODPX_HUMAN', 'CONFLICT', '344', ' /note="P -> S (in Ref. 5; BAG62924)" /evidence="ECO:0000305"']
['ODPX_HUMAN', 'STRAND', '57..60', ' /evidence="ECO:0007829|PDB:2DNC"']
['ODPX_HUMAN', 'STRAND', '69..71', ' /evidence="ECO:0007829|PDB:2DNC"']
['ODPX_HUMAN', 'STRAND', '73..78', ' /evidence="ECO:0007829|PDB:2DNC"']
['ODPX_HUMAN', 'STRAND', '88..94', ' /evidence="ECO:0007829|PDB:2DNC"']
['ODPX_HUMAN', 'STRAND', '99..103', ' /evidence="ECO:0007829|PDB:2DNC"']
['ODPX_HUMAN', 'STRAND', '108..112', ' /evidence="ECO:0007829|PDB:2DNC"']
['ODPX_HUMAN', 'STRAND', '122..125', ' /evidence="ECO:0007829|PDB:2DNC"']
['ODPX_HUMAN', 'STRAND', '127..132', ' /evidence="ECO:0007829|PDB:2DNC"']
['ODPX_HUMAN', 'HELIX', '180..183', ' /evidence="ECO:0007829|PDB:2F60"']
['ODPX_HUMAN', 'HELIX', '186..194', ' /evidence="ECO:0007829|PDB:2F60"']
['ODPX_HUMAN', 'HELIX', '199..201', ' /evidence="ECO:0007829|PDB:2F60"']
['ODPX_HUMAN', 'HELIX', '207..209', ' /evidence="ECO:0007829|PDB:2F60"']
['ODPX_HUMAN', 'HELIX', '213..230', ' /evidence="ECO:0007829|PDB:2F60"']

--TABLE COMMENTS--
['ODPX_HUMAN', ' FUNCTION: Required for anchoring dihydrolipoamide dehydrogenase (E3) to the dihydrolipoamide transacetylase (E2) core of the pyruvate dehydrogenase complexes of eukaryotes. This specific binding is essential for a functional PDH complex.']
['ODPX_HUMAN', ' SUBUNIT: Part of the inner core of the multimeric pyruvate dehydrogenase complex that is composed of about 48 DLAT and 12 PDHX molecules (PubMed:14638692, PubMed:20361979). This core binds multiple copies of pyruvate dehydrogenase (subunits PDH1A and PDHB, E1), dihydrolipoamide acetyltransferase (DLAT, E2) and lipoamide dehydrogenase (DLD, E3) (PubMed:14638692). Interacts with SIRT4 (PubMed:25525879). Interacts with DLD (PubMed:20385101, PubMed:16263718, PubMed:16442803, PubMed:20160912, PubMed:20361979). {ECO:0000269|PubMed:14638692, ECO:0000269|PubMed:16263718, ECO:0000269|PubMed:16442803, ECO:0000269|PubMed:20160912, ECO:0000269|PubMed:20361979, ECO:0000269|PubMed:20385101, ECO:0000269|PubMed:25525879}.']
['ODPX_HUMAN', ' INTERACTION: O00330; Q6RW13: AGTRAP; NbExp=5; IntAct=EBI-751566, EBI-741181; O00330; Q9UHD4: CIDEB; NbExp=3; IntAct=EBI-751566, EBI-7062247; O00330; P09622: DLD; NbExp=7; IntAct=EBI-751566, EBI-353366; O00330; Q9Y6E7: SIRT4; NbExp=4; IntAct=EBI-751566, EBI-2606540;']
['ODPX_HUMAN', ' SUBCELLULAR LOCATION: Mitochondrion matrix.']
['ODPX_HUMAN', ' ALTERNATIVE PRODUCTS: Event=Alternative splicing; Named isoforms=3; Name=1;   IsoId=O00330-1; Sequence=Displayed; Name=2;   IsoId=O00330-2; Sequence=VSP_045271; Name=3;   IsoId=O00330-3; Sequence=VSP_053817;']
['ODPX_HUMAN', ' PTM: Delipoylated at Lys-97 by SIRT4, delipoylation decreases the PHD complex activity. {ECO:0000269|PubMed:25525879}.']
['ODPX_HUMAN', ' DISEASE: Pyruvate dehydrogenase E3-binding protein deficiency (PDHXD) [MIM:245349]: A metabolic disorder characterized by decreased activity of the pyruvate dehydrogenase complex without observable reduction in the activities of enzymes E1, E2, or E3. Clinical features include hypotonia and psychomotor retardation. {ECO:0000269|PubMed:9399911}. Note=The disease is caused by variants affecting the gene represented in this entry.']
['ODPX_HUMAN', ' SIMILARITY: Belongs to the 2-oxoacid dehydrogenase family. {ECO:0000305}.']
['ODPX_HUMAN', '---------------------------------------------------------------------------']
['ODPX_HUMAN', 'Copyrighted by the UniProt Consortium, see https://www.uniprot.org/terms']
['ODPX_HUMAN', 'Distributed under the Creative Commons Attribution (CC BY 4.0) License']
['ODPX_HUMAN', '---------------------------------------------------------------------------']

--TABLE FASTA--
['ODPX_HUMAN', 'id=ODPX_HUMAN;accesion=O00330;B4DW62;D3DR11;E9PB14;E9PBP7;O60221;Q96FV8;Q99783;name=Homo sapiens (Human).', 'MAASWRLGCDPRLLRYLVGFPGRRSVGLVKGALGWSVSRGANWRWFHSTQWLRGDPIKILMPSLSPTMEEGNIVKWLKKEGEAVSAGDAL\nCEIETDKAVVTLDASDDGILAKIVVEEGSKNIRLGSLIGLIVEEGEDWKHVEIPKDVGPPPPVSKPSEPRPSPEPQISIPVKKEHIPGTL\nRFRLSPAARNILEKHSLDASQGTATGPRGIFTKEDALKLVQLKQTGKITESRPTPAPTATPTAPSPLQATAGPSYPRPVIPPVSTPGQPN\nAVGTFTEIPASNIRRVIAKRLTESKSTVPHAYATADCDLGAVLKVRQDLVKDDIKVSVNDFIIKAAAVTLKQMPDVNVSWDGEGPKQLPF\nIDISVAVATDKGLLTPIIKDAAAKGIQEIADSVKALSKKARDGKLLPEEYQGGSFSISNLGMFGIDEFTAVINPPQACILAVGRFRPVLK\nLTEDEEGNAKLQQRQLITVTMSSDSRVVDDELATRFLKSFKANLENPIRLA\n']
2  records inserted in total in  example2.db


