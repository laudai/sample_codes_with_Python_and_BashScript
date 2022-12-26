#!/usr/bin/env python
# encoding: utf8
# Author : laudai

# reference: https://www.ithome.com.tw/voice/127918import hashlib

import hashlib
import subprocess
import secrets


origin = "123456"
salt1 = secrets.token_hex(8)
salt2 = secrets.token_hex(8)


def make_md5(text: str) -> str:
    md5_value = hashlib.md5(text.encode("utf-8")).hexdigest()
    return md5_value


def make_sha256(text: str) -> str:
    sha256_value = hashlib.sha256(text.encode("utf-8")).hexdigest()
    return sha256_value


print("random salt scope")
print("salt1 is:", salt1)
print("salt2 is:", salt2)
print("-----------")

print("md5 scope")
print("origin")
print(make_md5(origin))
print("with salt1")
print(make_md5(origin + salt1))
print("with salt2")
print(make_md5(origin + salt2))
print()
subprocess.run(f"echo -n '{origin}' | md5sum | awk {{'print $1'}}", shell=True)
subprocess.run(f"echo -n '{origin+salt1}' | md5sum | awk {{'print $1'}}", shell=True)
subprocess.run(f"echo -n '{origin+salt2}' | md5sum | awk {{'print $1'}}", shell=True)
print("-----------")

print("sha256 scope")
print("origin")
print(make_sha256(origin))
print("with salt1")
print(make_sha256(origin + salt1))
print("with salt2")
print(make_sha256(origin + salt2))
print()

subprocess.run(f"echo -n '{origin}' | sha256sum | awk {{'print $1'}}", shell=True)
subprocess.run(f"echo -n '{origin+salt1}' | sha256sum | awk {{'print $1'}}", shell=True)
subprocess.run(f"echo -n '{origin+salt2}' | sha256sum | awk {{'print $1'}}", shell=True)
