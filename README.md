[![Build Status][build-status-badge]][build-system]
[![BSD-2-Clause][bsd-2-badge]](LICENSE)

# ansible-fail2ban

This role installs any version of Fail2Ban with minimum requirements and
configure operator customized or pre-made jails by Fail2Ban community to secure
the system from dictionary attacks--or brute-force.

Default behavior of this role is to install Fail2Ban from its git repository
with defined latest version and, of course, start the service.

## Requirements

This role only requires Ansible and operating system that is stated in
[Compatibility Chart][compatibility-chart].

## Role Variables

There is no additional variables for this role.

## Example Playbook

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

```yaml
- hosts: servers
  roles:
     - { role: ansible-fail2ban }
```

## Versioning

We use [SemVer][semver] for versioning. For the versions available, see [the releases on this repository][project-releases].

[build-system]: https://travis-ci.org/BerkhanBerkdemir/ansible-fail2ban
[build-status-badge]: https://travis-ci.org/BerkhanBerkdemir/ansible-fail2ban.svg?branch=master
[bsd-2-badge]: https://img.shields.io/badge/license-BSD--2--Clause-green
[compatibility-chart]: https://github.com/BerkhanBerkdemir/ansible-fail2ban/wiki/Compatibility-Chart
[semver]: https://semver.org
[project-releases]: https://github.com/BerkhanBerkdemir/ansible-fail2ban/releases
