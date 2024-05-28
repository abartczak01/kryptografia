#!/bin/bash

cat hash-.pdf personal.txt | md5sum | sed 's/  -//' >> hash.txt
cat hash-.pdf personal_.txt | md5sum | sed 's/  -//' >> hash.txt
cat hash-.pdf personal.txt | sha1sum | sed 's/  -//' >> hash.txt
cat hash-.pdf personal_.txt | sha1sum | sed 's/  -//' >> hash.txt
cat hash-.pdf personal.txt | sha224sum | sed 's/  -//' >> hash.txt
cat hash-.pdf personal_.txt | sha224sum | sed 's/  -//' >> hash.txt
cat hash-.pdf personal.txt | sha256sum | sed 's/  -//' >> hash.txt
cat hash-.pdf personal_.txt | sha256sum | sed 's/  -//' >> hash.txt
cat hash-.pdf personal.txt | sha384sum | sed 's/  -//' >> hash.txt
cat hash-.pdf personal_.txt | sha384sum | sed 's/  -//' >> hash.txt
cat hash-.pdf personal.txt | sha512sum | sed 's/  -//' >> hash.txt
cat hash-.pdf personal_.txt | sha512sum | sed 's/  -//' >> hash.txt
cat hash-.pdf personal.txt | b2sum | sed 's/  -//' >> hash.txt
cat hash-.pdf personal_.txt | b2sum | sed 's/  -//' >> hash.txt