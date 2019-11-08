import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_fail2ban_version(host):
    command = host.command('fail2ban-server -V')

    assert command.stdout.startswith('0.10.4')


def test_fail2ban_service_file(host):
    file = host.file('/usr/lib/systemd/system/fail2ban.service')

    assert file.exists
    assert file.user == 'root'
    assert file.group == 'root'
    assert file.mode == 0o644


def test_fail2ban_directory(host):
    directory = host.file("/etc/fail2ban")

    assert directory.exists
    assert directory.is_directory
    assert directory.user == 'root'
    assert directory.group == 'root'


def test_fail2ban_service_is_running(host):
    fail2ban = host.service('fail2ban')

    assert fail2ban.is_running
    assert fail2ban.is_enabled
