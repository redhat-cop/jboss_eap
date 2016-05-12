#!/usr/bin/python

# Written By - Andrew Block <andy.block@gmail.com>

##############################################################################

import requests
import lxml.html

DOCUMENTATION = '''
---
module: redhat_csp_download
version_added: "0.1"
short_description: Downloads resources from the Red Hat customer portal.
description:
    - Downloads resources from the Red Hat customer portal.
options:
    username:
        description:
            - Red Hat Customer Portal username.
        required: true
    password:
        description:
            - Red Hat Customer Portal username.
        required: true
    url:
        description:
            - Protected Red Hat Customer Portal resource.
        required: true
    dest:
        description:
            - absolute path of where to download the file to.
        required: true
'''

EXAMPLES = '''
- name: Download JBoss EAP Zip
  redhat_csp_download: username=foo password=bar url=https://access.redhat.com/jbossnetwork/restricted/softwareDownload.html?softwareId=37193 dest=/tmp/eap-connectors.zip

'''

def get_csp_file(module,username,password,url,dest):

    # Setup Auth Struct
    auth = {'j_username': username, 'j_password': password}

    session = requests.Session()

    # Get initial request
    r = session.get(url)

    # Parse initial response
    root = lxml.html.fromstring(r.text)
    samlrequest = root.xpath('//input[@name="SAMLRequest"]')[0].value
    relaystate = root.xpath('//input[@name="RelayState"]')[0].value
    post_url = root.xpath('//form[@method="POST"]')[0].action

    data = {'RelayState': relaystate, 'SAMLRequest': samlrequest, 'j_username': username, 'j_password': password}
    r = session.post(post_url, data=data)

    root = lxml.html.fromstring(r.text)
    post_url = root.xpath('//form[@method="post"]')[0].action

    # Format relative path
    security_check_url = "{}{}".format(r.url,post_url)

    r = session.post(security_check_url, data=data)

    root = lxml.html.fromstring(r.text)

    # Validate Authentication with SAMLResponse
    samlresponse = root.xpath('//input[@name="SAMLResponse"]')

    if not samlresponse:
        module.fail_json(msg="Invalid credentials")

    samlresponse = samlresponse[0].value

    relaystate = root.xpath('//input[@name="RelayState"]')[0].value
    post_url = root.xpath('//form[@method="POST"]')[0].action
    data = {'RelayState': relaystate, 'SAMLResponse': samlresponse, 'j_username': username, 'j_password': password}

    # Final Post to download file
    r = session.post(post_url, data=data)

    # Download file
    with open(dest, "wb") as code:
        code.write(r.content)

    # Close session
    session.close()


def main():
    module = AnsibleModule(
        argument_spec = dict(
            username = dict(required=True),
            password = dict(required=True),
            url = dict(required=True),
            dest = dict(required=True)
        ),
        add_file_common_args=True
    )

    username = module.params.get('username')
    password = module.params.get('password')
    url = module.params.get('url')
    dest = module.params.get('dest')

    if os.path.exists(dest):
        # allow file attribute changes
        module.params['path'] = dest
        file_args = module.load_file_common_arguments(module.params)
        file_args['path'] = dest
        changed = module.set_fs_attributes_if_different(file_args, False)

        if changed:
            module.exit_json(msg="file already exists but file attributes changed", dest=dest, url=url, changed=changed)
        module.exit_json(msg="file already exists", dest=dest, url=url, changed=changed)

    get_csp_file(module,username,password,url,dest)

    changed = True

    res_args = dict(
        url = url, dest = dest, changed = changed, msg = "OK"
    )

    module.exit_json(**res_args)


from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()
