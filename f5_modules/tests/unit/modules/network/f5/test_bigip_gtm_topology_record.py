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
    from library.modules.bigip_gtm_topology_record import ApiParameters
    from library.modules.bigip_gtm_topology_record import ModuleParameters
    from library.modules.bigip_gtm_topology_record import ModuleManager
    from library.modules.bigip_gtm_topology_record import ArgumentSpec

    # In Ansible 2.8, Ansible changed import paths.
    from test.units.compat import unittest
    from test.units.compat.mock import Mock

    from test.units.modules.utils import set_module_args
except ImportError:
    from ansible_collections.f5networks.f5_modules.plugins.modules.network.f5.bigip_gtm_topology_record import ApiParameters
    from ansible_collections.f5networks.f5_modules.plugins.modules.network.f5.bigip_gtm_topology_record import ModuleParameters
    from ansible_collections.f5networks.f5_modules.plugins.modules.network.f5.bigip_gtm_topology_record import ModuleManager
    from ansible_collections.f5networks.f5_modules.plugins.modules.network.f5.bigip_gtm_topology_record import ArgumentSpec

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
            source=dict(
                subnet='192.168.1.0/24',
                negate=True
            ),
            destination=dict(
                region='Foobar',
            ),
            weight=10
        )

        p = ModuleParameters(params=args)
        assert p.name == 'ldns: not subnet 192.168.1.0/24 server: region /Common/Foobar'
        assert p.weight == 10

    def test_api_parameters(self):
        args = dict(
            source=dict(
                subnet='192.168.1.0/24',
                negate=True
            ),
            destination=dict(
                region='Foobar',
            ),
            score=10
        )

        p = ApiParameters(params=args)
        assert p.weight == 10


class TestManager(unittest.TestCase):

    def setUp(self):
        self.spec = ArgumentSpec()

    def test_create_topology_record(self, *args):
        set_module_args(dict(
            source=dict(
                subnet='192.168.1.0/24',
                negate=True
            ),
            destination=dict(
                region='Foobar',
            ),
            weight=10,
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode
        )

        # Override methods in the specific type of manager
        mm = ModuleManager(module=module)
        mm.exists = Mock(side_effect=[False, True])
        mm.create_on_device = Mock(return_value=True)

        results = mm.exec_module()

        assert results['changed'] is True
