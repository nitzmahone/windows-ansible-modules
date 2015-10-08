#!/usr/bin/python

DOCUMENTATION='''
'''

EXAMPLES='''
# ensure a server is a domain controller 
- hosts: winclient
  gather_facts: no
  tasks:
  - win_domain_controller:
      dns_domain_name: ansible.vagrant
      domain_admin_user: testguy@ansible.vagrant
      domain_admin_pass: password123!
      safe_mode_pass: password123!
      state: domain_controller
      log_path: c:\\ansible_win_domain_controller.txt

# ensure a server is not a domain controller
# note that without an action wrapper, in the case where a DC is demoted, 
# the task will fail with a 401 Unauthorized, because the domain credential 
# becomes invalid to fetch the final output over WinRM. This requires win_async 
# with credential switching (or some other clever credential-switching 
# mechanism to get the output and trigger the required reboot)
- hosts: winclient
  gather_facts: no
  tasks:
  - win_domain_controller:
      domain_admin_user: testguy@ansible.vagrant
      domain_admin_pass: password123!
      local_admin_pass: password123!
      state: member_server
      log_path: c:\\ansible_win_domain_controller.txt



'''

