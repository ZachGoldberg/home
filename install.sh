mkdir -p parts
mkdir -p build/parts

sudo apt-get install uwsgi nginx haproxy  uwsgi-plugin-python


python bootstrap.py
