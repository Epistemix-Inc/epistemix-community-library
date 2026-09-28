#!/bin/sh

# Fail the job (before S3 is cleared) if any fred.toml cannot be parsed.
set -e

pip install tomlq

touch manifest.toml && echo "" > manifest.toml

for file in */fred.toml; do
    filename=${file%/fred.toml}
    metadata=$(tomlq -t '.metadata' "$file")
    echo "[[metadata]]\n$metadata\nslug = \"$filename\"\n" >> manifest.toml
done

sed -i -e '1{/^$/d;}' manifest.toml
sed -i -e '${/^$/d;}' manifest.toml
