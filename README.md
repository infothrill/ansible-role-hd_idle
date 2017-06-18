Ansible role: hd-idle
=====================

Install [hd-idle](http://hd-idle.sourceforge.net/) from source.

Requirements
------------

Operating system support for /proc/diskstats, Debian compatibility.
Tested with Ansible 2.1, 2.2, 2.3

Role Variables
--------------

Available variables are listed below, along with default values (see defaults/main.yml):

	hd_idle_version: 1.05

The version to install. If changed, `hd_idle_checksum` also needs to be adapted.

	hd_idle_checksum: sha256:4efefe79d145b50e055582730d9d685e485da3df3dad90fef030036d52aa3a0c

The checksum. We do this to enable trust in the downloaded code as well as enabling
downloads without https cert verification (which is problematic on old python installs).	

	hd_idle_compile_dir: /tmp/hd_idle

The directory to use for compilation purposes.

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: raspberrypis
      roles:
         - { role: hd-idle }

Changelog
---------

### 1.1

* added test for ansible 2.3
* fixed deprecation warnings in ansible 2.3

### 1.0

* initial release

License
-------

MIT / BSD

Author Information
------------------

This role was created in 2017 by Paul Kremer.
