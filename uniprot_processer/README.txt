UNIPROT TEXT FORMAT

The Uniprot_sprot.dat text data file, is a text file with information about proteins. The file can be download from
https://www.uniprot.org/downloads . When in the page, download the file “Reviewed (Swiss-Prot)” in text format.
Please do not download xml or fasta. After downloading, decompress the file. This file is about 3.4 Gb, at the
date of elaboration of this document.
Every record in the file starts with the field ID, and ends with the pair of characters // (slash, slash). Fields have a 2
character identification as the first 2 characters. Sequence field SQ, is followed by aminoacid sequence with no code,
until the record ends.

SPECIFICATIONS

This is a query tool to query protein records, given as a filter the name of fields and values using the and logic.
For field/value separator, use the sequence VALUE.in.FIELD [ .and . [VALUE.in.FIELD]][ .and . [VALUE.in.FIELD]]...
Use every record matching the conditional sentence to apply for the commands that could appear as the TOOL
USAGE section explains.

TOOL USAGE

COMMAND.
● The command line tool name is uprotview. A user use the command line to write the name of the
command, like % > python3 uprotview.py filter fieldlist or commands
ARGUMENTS
● First argument is the filename of the uniprot data.
● Second argument is the filter to apply to the data (the QUERY).
○ VALUE_.in.FIELD [ .and . [VALUE.in.FIELD]][ .and . [VALUE.in.FIELD]]...
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