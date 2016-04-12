Ansible JBoss EAP Role
=================

A role to install JBoss Enterprise Application Platform on RHEL7. Intended to be used with [JBoss Middleware Playbooks](https://github.com/rhtconsulting/ansible-middleware-playbooks)

Requirements
------------

- Valid subscription for JBoss EAP. This role retrieves all binaries from the [Red Hat Customer Portal](https://access.redhat.com/downloads/)

Required Role Variables
--------------

- 'rhn_username'
- 'rhn_password'

Dependencies
------------

- java

Example Playbook
----------------

[JBoss EAP 6.4.0 on RHEL 7](https://github.com/rhtconsulting/ansible-middleware-playbooks/blob/master/eap6.4-centos7.yml)

License
-------

[LICENSE](./LICENSE)

Authors Information
------------------

* [Andrew Block] (https://github.com/orgs/rhtconsulting/people/sabre1041)
* [Albert Wong] (https://github.com/orgs/rhtconsulting/people/alberttwong)
* [Justin Holmes] (https://github.com/sherl0cks)
* [Kamesh Sampath] (https://github.com/kameshsampath)
