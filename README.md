# Ansible role: hd_idle

![Build status](https://github.com/infothrill/ansible-role-hd_idle/actions/workflows/tests.yml/badge.svg)
[![Ansible Role](https://img.shields.io/ansible/role/29102.svg)](https://galaxy.ansible.com/infothrill/hd_idle/)

Install [hd-idle](http://hd-idle.sourceforge.net/) from source. This
program is useful to spin down harddrives after a given timeout of
inactivity. This can save power and maybe extend the lifespan of the spinning disk.

## Requirements

Operating system support for /proc/diskstats, Debian compatibility.

## Role Variables

Available variables are listed below, along with default values (see defaults/main.yml):

    hd_idle_version: 1.05

The version to install. If changed, `hd_idle_checksum` also needs to be adapted.

    hd_idle_checksum: sha256:4efefe79d145b50e055582730d9d685e485da3df3dad90fef030036d52aa3a0c

The checksum. We do this to enable trust in the downloaded code as well as enabling
downloads without https cert verification (which is problematic on old python installs).

    hd_idle_compile_dir: /tmp/hd_idle

The directory to use for compilation purposes.

## Dependencies

None.

## Example Playbook

    - hosts: raspberrypis
      roles:
         - { role: infothrill.hd_idle }

## Changelog

### 2.x

* Drop support for ansible < 5
* Drop support for python < 3.8
* Switch to Github Actions for CI

### 2.0.2

* Drop support for ansible < 2.9
* Upgrade molecule to 3.0.x
* added support for ansible 2.10, 3.0
* add support for python 3.7+

### 2.0.1

* increase timeout for download to 60 sec
* explicitly set owner of unpacked source code to `root`

### 2.0.0

* dropped support for ansible 2.4
* added support for ansible 2.8
* switched testing toolchain to python 3.6
* upgraded molecule and ansible-lint

### 1.4.1

* added testing for ansible 2.8
* added experimental test for debian buster

### 1.4.0

* added basic lint/syntax test using travis
* renamed role to `hd_idle` (from `hd-idle`)

### 1.3

* added test for ansible 2.6

### 1.2.0

* added test for ansible 2.4, 2.5
* dropped support for ansible 2.1
* upgraded molecule to 2.15
* added test for debian stretch 9.4

### 1.2.0

* upgraded molecule
* fixed molecule paybook

### 1.1.0

* added test for ansible 2.3
* fixed deprecation warnings in ansible 2.3

### 1.0.0

* initial release

## License

MIT

## Author Information

This role was created in 2017 by Paul Kremer.
