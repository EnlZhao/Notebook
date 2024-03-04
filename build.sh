#!/bin/bash

# mkdocs build
echo -e "\033[32m mkdocs build\033[0m"
mkdocs gh-deploy
echo -e "\033[42m mkdocs build done\033[0m"

# Delete cache
echo -e "\033[32m Delete cache\033[0m"
rm -rf ./site
echo -e "\033[42m Delete cache done\033[0m"

# Delete branch gh-pages
echo -e "\033[32m Delete branch gh-pages\033[0m"
git branch -D gh-pages
echo -e "\033[42m Delete branch gh-pages done\033[0m"

