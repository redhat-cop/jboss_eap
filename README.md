Ansible JBoss EAP Role
=================

A role to install JBoss Enterprise Application Platform on RHEL7. Intended to be used with [JBoss Middleware Playbooks](https://github.com/rhtconsulting/ansible-middleware-playbooks)

Requirements
------------

- Valid subscription for JBoss EAP. This role retrieves all binaries from the [Red Hat Customer Portal](https://access.redhat.com/downloads/)

Required Role Variables
--------------

Credentitals to interact with the [Red Hat Customer Portal](https://access.redhat.com/downloads/).
- `rhn_username`
- `rhn_password`

Download Options
------------

There are a few different ways that this role can download the required artifacts:

1. Download the artifacts directly to the ansible host machine. This is the default option, but it requires the host to have network connectivity to the [Red Hat Customer Portal](https://access.redhat.com/downloads/).
  - To enable this option, set the variable: `download_method: csp-to-host`
2. Use the [copy](http://docs.ansible.com/ansible/copy_module.html) module to transer the files to the host. This option works well when the host system does not have network connectivity to the public internet, as is common in corporate datacenters. You'll need to manually download the artifacts or hook up your own automation (at least for now).
  To enable this option, set the variable: `download_method: copy-from-client`
3. TODO - Download the artifacts to the host from a custom file server. Useful when you want to centrally manage the artifacts behind a corporate firewall.
  - `download_method: file-server-to-host`



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

* [Andrew Block] (https://github.com/sabre1041)
* [Albert Wong] (https://github.com/alberttwong)
* [Justin Holmes] (https://github.com/sherl0cks)
* [Kamesh Sampath] (https://github.com/kameshsampath)
