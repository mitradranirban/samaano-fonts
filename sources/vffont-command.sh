# You need to install via Pip, in a venv or otherwise, the packages:
#   afdko fontmake

python3 make_designspace.py
fontmake -m Samaano.designspace -o variable --production-names --output-path Samaano[weight].ttf
