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

    s = list(filter(lambda x: len(x) > 0, f.content_string.split('\n')))

    assert 'maxClientCnxns=60' in s
    assert 'tickTime=2000' in s
    assert 'initLimit=10' in s
    assert 'syncLimit=5' in s
    assert 'dataDir=/var/lib/zookeeper' in s
    assert 'clientPort=2181' in s
    assert 'globalOutstandingLimit=1000' in s
    assert 'snapCount=100000' in s
    assert 'minSessionTimeout=4000' in s
    assert 'maxSessionTimeout=40000' in s
    assert 'fsync.warningthresholdms=1000' in s
    assert 'autopurge.snapRetainCount=3' in s
    assert 'autopurge.purgeInterval=0' in s
    assert 'syncEnabled=true' in s


def test_zookeeper_sh_file(host):
    f = host.file('/etc/profile.d/zookeeper.sh')

    assert f.exists
    assert f.user == 'root'


def test_zookeeper_init_file(host):
    f = host.file('/etc/init.d/zookeeper-server')

    assert f.exists
