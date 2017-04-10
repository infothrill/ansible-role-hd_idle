import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_hosts_file(File):
    f = File('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_packages(Package):
    assert Package('hd-idle').is_installed
    assert Package('hd-idle').version.startswith("1.05")


def test_service(Service):
    assert Service('hd-idle').is_running
    assert Service('hd-idle').is_enabled
