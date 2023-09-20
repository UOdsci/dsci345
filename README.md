

The actual website can be viewed at [https://UOdsci.github.io/dsci345/](https://UOdsci.github.io/dsci345/).

Quick link: the [schedule](https://UOdsci.github.io/dsci345/pages/schedule.html), with links to the slides.


--------------------


This is a [jekyll](https://jekyllrb.com) website,
modified from Karl Broman's [simple site](http://github.com/kbroman/simple_site)
by way of [Cécile Ané](http://cecileane.github.io/computingtools/).


*Notes on installation/building:*

- To view a local version run `bundle exec jekyll serve`.

- The skeleton can by modified by editing `config.yml` and `_includes/themes/twitter/default.html`.

- To get this to build locally with Debian, I had to `aptitude remove jekyll`; `bundle update`; 
    then find where the executable is using `bundle info jekyll`; 
    and finally make a symlink for the `jekyll` executable to somewhere in my `PATH`.


-------------------

The slides are written in jupyter,
rendered using [RISE](https://rise.readthedocs.io/en/stable/):
see notes [here](https://www.markroepke.me/posts/2019/05/23/creating-interactive-slideshows-in-jupyter.html)
and [here](https://www.markroepke.me/posts/2019/06/05/tips-for-slideshows-in-jupyter.html).
Also see [enabling extensions](https://github.com/ipython-contrib/jupyter_contrib_nbextensions/blob/master/README.md#2-install-javascript-and-css-files)

Prerequisites for executing and showing the slides are in `requirements/conda-environment.yml`:
```
conda env create -f requirements/conda-environment.yml 
conda activate dsci
```

Also currently (9/20/23) that to use the slides (with jupyter RISE) you have to display them with jupyter notebook,
and there is a bug that requires doing
```
pip uninstall traitlets
pip install traitlets==5.9.0
```
