# blog


My personal blog. Check it on [http://jordiburgos.com](http://jordiburgos.com).

Writen with Pelican and with my own theme [https://github.com/jmaister/jmtheme](https://github.com/jmaister/jmtheme).


# save environment

    conda env export > environment.yml

# prepare environment

    conda env create -f environment.yml
    git clone https://github.com/jmaister/blog.git
    cd blog
    git clone https://github.com/jmaister/jmtheme.git
    git clone https://github.com/getpelican/pelican-plugins.git
    cd pelican-plugins
    git clone https://github.com/jmaister/readtime.git

# generate

    pelican content
    
    
