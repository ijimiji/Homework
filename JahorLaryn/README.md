# Running
```
cd py-rss
poetry install
./reader.py ...
```
# Building
```
cd py-rss
poetry build
```
Produces dist folder with installer.
# Testing 
```
cd py-rss/py_rss
python3 -m pytest
```
# Using as a daemon
```
# First process
cd py-rss/py_rss
./reader.py ... --daemon
# Second process
cd py-rss-client
npm install
npm run dev
```
# Screenshots
![client](client.jpg "Svelte client")
![cli](cli.jpg "Cli view")


