# -*- coding: utf-8 -*-
import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_packages(host):
    assert host.package('hd-idle').is_installed
    assert host.package('hd-idle').version.startswith("1.05")


def test_service(host):
    assert host.service('hd-idle').is_running
    assert host.service('hd-idle').is_enabled
