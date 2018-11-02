import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_zookeeper_user(host):
    u = host.user('zookeeper')

    assert u.name == 'zookeeper'
    assert 'zookeeper' in u.groups


def test_zoo_cfg_file(host):
    f = host.file('/etc/zookeeper/zoo.cfg')

    assert f.exists


def test_zookeeper_init_file(host):
    f = host.file('/etc/init.d/zookeeper-server')

    assert f.exists


def test_zookeeper_pid_file(host):
    f = host.file('/var/run/zookeeper/zookeeper-server.pid')

    assert f.exists


def test_myid_file(host):
    f = host.file('/var/lib/zookeeper/myid')

    assert f.exists
