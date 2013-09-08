# nus-stalker
Time to feed your inner stalker

## What is it?
A python API to search nus ldap.

## Installation
Just use pip!

    pip install nusstalker

## Usage
There are currently two functions. You can either search for any person in NUS or
browse the class roster for a module.

    from nusstalker.main import NusStalker
    s = NusStalker(user="nusstu\A00123", pw="secret")
    s.search_by_name("jason")
    s.search_by_module("CS1010S")

## Credits
[Fazli's](http://github.com/fuzzie360) nus-stalker in javascript - https://github.com/fuzzie360/nus-stalker/
