DIR=data/
SITE_INTERACTIONS=https://stringdb-static.org/download/protein.links.v11.0/9606.protein.links.v11.0.txt.gz
SITE_PFAM=https://chalmersuniversity.box.com/shared/static/08tmtk9adq43f9af9z7b91i0bnpqhd15.txt
SITE_IMAGE=https://chalmersuniversity.box.com/shared/static/lfuvsw6v6smjjxa24gv5dj76mvp6pgxs.sif

FILE_INTERACTIONS=protein_links.txt.gz
FILE_PFAM=protein_domains.txt
FILE_IMAGE=image.sif

mkdir -p $DIR
cd $DIR
wget -O $FILE_INTERACTIONS $SITE_INTERACTIONS
gunzip -f $FILE_INTERACTIONS
wget -O $FILE_PFAM  $SITE_PFAM
cd ..
wget -O $FILE_IMAGE $SITE_IMAGE

