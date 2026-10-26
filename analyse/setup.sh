#!/bin/sh
# Haalt de grote databestanden op (niet in de repo): OpenTaal-woordenlijst en Nederlandse ondertitelfrequenties.
cd "$(dirname "$0")" && mkdir -p data
[ -d data/opentaal ] || git clone --depth 1 https://github.com/OpenTaal/opentaal-wordlist.git data/opentaal
[ -f data/nl_full.txt ] || curl -sSL -o data/nl_full.txt https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/nl/nl_full.txt
pip install numpy >/dev/null 2>&1 || pip install --break-system-packages numpy
