[![BSD-2-Clause][bsd-2-badge]](LICENSE)

# ansible-fail2ban

This role installs any version of Fail2Ban with minimum requirements and
configure operator customized or pre-made jails by Fail2Ban community to secure
the system from dictionary attacks--or brute-force.

Default behavior of this role is to install Fail2Ban from its git repository
with defined latest version and, of course, start the service.

## Requirements

This role only requires Ansible and operating system that is stated in
[Compatibility Chart](#compatibility-chart).

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

## Compatibility Chart

| Operating System | Release | Tested | Allow failures | Planned |
| ---------------- | ------- | ------ | -------------- | ------- |
| Amazon Linux     | 1       | No     | -              | -       |
| Amazon Linux     | 2       | Yes    | No             | -       |
| CentOS           | 6       | No     | -              | -       |
| CentOS           | 7       | Yes    | No             | -       |
| CentOS           | 8       | Yes    | No             | -       |
| openSUSE         | 15.1    | No     | -              | Yes     |
| Debian           | 8       | No     | -              | Yes     |
| Debian           | 9       | No     | -              | Yes     |
| Debian           | 10      | No     | -              | Yes     |
| Ubuntu           | 16.04   | No     | -              | Yes     |
| Ubuntu           | 18.04   | No     | -              | Yes     |

[bsd-2-badge]: https://img.shields.io/badge/license-BSD--2--Clause-green
