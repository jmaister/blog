cd blog
git pull
cd jmtheme2
git pull
cd ..
cd pelican-plugins
git pull
cd ..
make clean
make publish
rm -rf /home/jordibur/public_html/*
cp -r output/* /home/jordibur/public_html/
cd
cp -r blog/content/js www/
