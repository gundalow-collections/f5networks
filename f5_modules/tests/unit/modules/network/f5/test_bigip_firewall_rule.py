# -*- coding: utf-8 -*-
#
# Copyright: (c) 2018, F5 Networks Inc.
# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os
import json
import pytest
import sys

if sys.version_info < (2, 7):
    pytestmark = pytest.mark.skip("F5 Ansible modules require Python >= 2.7")

from ansible.module_utils.basic import AnsibleModule

try:
    from library.modules.bigip_firewall_rule import ModuleParameters
    from library.modules.bigip_firewall_rule import ModuleManager
    from library.modules.bigip_firewall_rule import ArgumentSpec

    # In Ansible 2.8, Ansible changed import paths.
    from test.units.compat import unittest
    from test.units.compat.mock import Mock

    from test.units.modules.utils import set_module_args
except ImportError:
    from ansible_collections.f5networks.f5_modules.plugins.modules.network.f5.bigip_firewall_rule import ModuleParameters
    from ansible_collections.f5networks.f5_modules.plugins.modules.network.f5.bigip_firewall_rule import ModuleManager
    from ansible_collections.f5networks.f5_modules.plugins.modules.network.f5.bigip_firewall_rule import ArgumentSpec

    # Ansible 2.8 imports
    from ansible_collections.f5networks.f5_modules.tests.unit.compat import unittest
    from ansible_collections.f5networks.f5_modules.tests.unit.compat.mock import Mock

    from ansible_collections.f5networks.f5_modules.tests.unit.modules.utils import set_module_args


fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures')
fixture_data = {}


def load_fixture(name):
    path = os.path.join(fixture_path, name)

    if path in fixture_data:
        return fixture_data[path]

    with open(path) as f:
        data = f.read()

    try:
        data = json.loads(data)
    except Exception:
        pass

    fixture_data[path] = data
    return data


class TestParameters(unittest.TestCase):
    def test_module_parameters(self):
        args = dict(
            name='foo',
            parent_policy='policy1',
            protocol='tcp',
            source=[
                dict(address='1.2.3.4'),
                dict(address='::1'),
                dict(address_list='foo-list1'),
                dict(address_range='1.1.1.1-2.2.2.2.'),
                dict(vlan='vlan1'),
                dict(country='US'),
                dict(port='22'),
                dict(port_list='port-list1'),
                dict(port_range='80-443'),
            ],
            destination=[
                dict(address='1.2.3.4'),
                dict(address='::1'),
                dict(address_list='foo-list1'),
                dict(address_range='1.1.1.1-2.2.2.2.'),
                dict(country='US'),
                dict(port='22'),
                dict(port_list='port-list1'),
                dict(port_range='80-443'),
            ],
            irule='irule1',
            action='accept',
            logging=True,
        )

        p = ModuleParameters(params=args)
        assert p.irule == '/Common/irule1'
        assert p.action == 'accept'
        assert p.logging is True


class TestManager(unittest.TestCase):

    def setUp(self):
        self.spec = ArgumentSpec()

    def test_create_monitor(self, *args):
        set_module_args(dict(
            name='foo',
            parent_policy='policy1',
            protocol='tcp',
            source=[
                dict(address='1.2.3.4'),
                dict(address='::1'),
                dict(address_list='foo-list1'),
                dict(address_range='1.1.1.1-2.2.2.2.'),
                dict(vlan='vlan1'),
                dict(country='US'),
                dict(port='22'),
                dict(port_list='port-list1'),
                dict(port_range='80-443'),
            ],
            destination=[
                dict(address='1.2.3.4'),
                dict(address='::1'),
                dict(address_list='foo-list1'),
                dict(address_range='1.1.1.1-2.2.2.2.'),
                dict(country='US'),
                dict(port='22'),
                dict(port_list='port-list1'),
                dict(port_range='80-443'),
            ],
            irule='irule1',
            action='accept',
            logging='yes',
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            mutually_exclusive=self.spec.mutually_exclusive,
            required_one_of=self.spec.required_one_of
        )

        # Override methods in the specific type of manager
        mm = ModuleManager(module=module)
        mm.exists = Mock(side_effect=[False, True])
        mm.create_on_device = Mock(return_value=True)

        results = mm.exec_module()

        assert results['changed'] is True
