#!/bin/bash

mysql -u root --password="" -e "drop database db;"
mysql -u root --password="" -e "create database db;"
echo "no" | python ~/brewer/manage.py syncdb
echo "import scripts.initial_data" | python ~/brewer/manage.py shell
echo "\n"
