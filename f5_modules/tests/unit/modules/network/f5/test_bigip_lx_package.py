# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 F5 Networks Inc.
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
    from library.modules.bigip_lx_package import Parameters
    from library.modules.bigip_lx_package import ModuleManager
    from library.modules.bigip_lx_package import ArgumentSpec

    # In Ansible 2.8, Ansible changed import paths.
    from test.units.compat import unittest
    from test.units.compat.mock import Mock
    from test.units.compat.mock import patch

    from test.units.modules.utils import set_module_args
except ImportError:
    from ansible_collections.f5networks.f5_modules.plugins.modules.network.f5.bigip_lx_package import Parameters
    from ansible_collections.f5networks.f5_modules.plugins.modules.network.f5.bigip_lx_package import ArgumentSpec
    from ansible_collections.f5networks.f5_modules.plugins.modules.network.f5.bigip_lx_package import ModuleManager

    # Ansible 2.8 imports
    from ansible_collections.f5networks.f5_modules.tests.unit.compat import unittest
    from ansible_collections.f5networks.f5_modules.tests.unit.compat.mock import Mock
    from ansible_collections.f5networks.f5_modules.tests.unit.compat.mock import patch

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
            package='MyApp-0.1.0-0001.noarch.rpm',
            state='present'
        )
        p = Parameters(params=args)
        assert p.package == 'MyApp-0.1.0-0001.noarch.rpm'


class TestManager(unittest.TestCase):

    def setUp(self):
        self.spec = ArgumentSpec()
        self.patcher1 = patch('time.sleep')
        self.patcher1.start()

        try:
            self.p1 = patch('library.modules.bigip_lx_package.tmos_version')
            self.m1 = self.p1.start()
            self.m1.return_value = '12.1.3'
        except Exception:
            self.p1 = patch('ansible.modules.network.f5.bigip_lx_package.tmos_version')
            self.m1 = self.p1.start()
            self.m1.return_value = '12.1.3'

    def tearDown(self):
        self.patcher1.stop()

    def test_create_iapp_template(self, *args):
        package_name = os.path.join(fixture_path, 'MyApp-0.1.0-0001.noarch.rpm')
        # Configure the arguments that would be sent to the Ansible module
        set_module_args(dict(
            package=package_name,
            state='present',
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            required_if=self.spec.required_if
        )
        mm = ModuleManager(module=module)

        # Override methods to force specific logic in the module to happen
        mm.exists = Mock(side_effect=[False, True])
        mm.create_on_device = Mock(return_value=True)
        mm.upload_to_device = Mock(return_value=True)
        mm.enable_iapplx_on_device = Mock(return_value=True)
        mm.remove_package_file_from_device = Mock(return_value=True)

        results = mm.exec_module()

        assert results['changed'] is True
