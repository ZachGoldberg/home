mkdir -p parts
mkdir -p build/parts

sudo apt-get install uwsgi nginx haproxy


python bootstrap.py
