DIR=data/
SITE=https://stringdb-static.org/download/protein.links.v11.0/9606.protein.links.v11.0.txt.gz
FILE=9606.protein.links.v11.0.txt.gz

cd $DIR
wget $SITE
gunzip $FILE
#rm $FILE
cd ..
