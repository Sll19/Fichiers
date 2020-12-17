#!/bin/bash

# Lister les repos Centreon par ordre alphabétique
curl https://api.github.com/orgs/Centreon/repos?per_page=1000 | grep -o 'git@[^\"]*' | sort
