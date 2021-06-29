DIR=data/
SITE_INTERACTIONS=https://stringdb-static.org/download/protein.links.v11.0/9606.protein.links.v11.0.txt.gz
SiTE_PFAM=https://chalmersuniversity.box.com/shared/static/08tmtk9adq43f9af9z7b91i0bnpqhd15.txt

FILE_INTERACTIONS=protein_links.txt.gz
FILE_PFAM=protein_domains.txt

cd $DIR
wget $SITE_INTERACTIONS -O $FILE_INTERACTIONS
gunzip $FILE_INTERACTIONS
wget $SITE_PFAM -O $FILE_PFAM
cd ..
