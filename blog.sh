cd blog
git pull
cd jmtheme
git pull
cd ..
make clean
make publish
rm -rf /home/jordibur/public_html/*
cp -r output/* /home/jordibur/public_html/
cd
cp -r blog/content/js www/
