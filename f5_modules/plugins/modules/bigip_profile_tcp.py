#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright: (c) 2017, F5 Networks Inc.
# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'certified'}

DOCUMENTATION = r'''author:
- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)
description:
- Manage TCP profiles on a BIG-IP. Many TCP profiles; each with their own adjustments
  to the standard C(tcp) profile. Users of this module should be aware that many of
  the adjustable knobs have no module default. Instead, the default is assigned by
  the BIG-IP system itself which, in most cases, is acceptable.
extends_documentation_fragment:
- f5networks.f5_modules.f5
module: bigip_profile_tcp
options:
  early_retransmit:
    description:
    - When C(yes) the system uses early fast retransmits to reduce the recovery time
      for connections that are receive-buffer or user-data limited.
    - When creating a new profile, if this parameter is not specified, the default
      is provided by the parent profile.
    type: bool
    version_added: 2.9
  idle_timeout:
    description:
    - Specifies the length of time that a connection is idle (has no traffic) before
      the connection is eligible for deletion.
    - When creating a new profile, if this parameter is not specified, the remote
      device will choose a default value appropriate for the profile, based on its
      C(parent) profile.
    - When a number is specified, indicates the number of seconds that the TCP connection
      can remain idle before the system deletes it.
    - When C(0), or C(indefinite), specifies that the system does not delete TCP connections
      regardless of how long they remain idle.
    type: str
  initial_congestion_window_size:
    description:
    - Specifies the initial congestion window size for connections to this destination.
      The actual window size is this value multiplied by the MSS for the same connection.
    - When set to C(0) the system uses the values specified in RFC2414.
    - The valid value range is 0 - 16 inclusive.
    - When creating a new profile, if this parameter is not specified, the default
      is provided by the parent profile.
    type: int
    version_added: 2.9
  initial_receive_window_size:
    description:
    - Specifies the initial receive window size for connections to this destination.
      The actual window size is this value multiplied by the MSS for the same connection.
    - When set to C(0) the system uses the Slow Start value.
    - The valid value range is 0 - 16 inclusive.
    - When creating a new profile, if this parameter is not specified, the default
      is provided by the parent profile.
    type: int
    version_added: 2.9
  nagle:
    choices:
    - auto
    - enabled
    - disabled
    description:
    - When C(enabled) the system applies Nagle's algorithm to reduce the number of
      short segments on the network.
    - When C(auto), the use of Nagle's algorithm is decided based on network conditions.
    - Note that for interactive protocols such as Telnet, rlogin, or SSH, F5 recommends
      disabling this setting on high-latency networks, to improve application responsiveness.
    - When creating a new profile, if this parameter is not specified, the default
      is provided by the parent profile.
    type: str
    version_added: 2.9
  name:
    description:
    - Specifies the name of the profile.
    required: true
    type: str
  parent:
    description:
    - Specifies the profile from which this profile inherits settings.
    - When creating a new profile, if this parameter is not specified, the default
      is the system-supplied C(tcp) profile.
    type: str
  partition:
    default: Common
    description:
    - Device partition to manage resources on.
    type: str
  proxy_options:
    description:
    - When C(yes) the system advertises an option, such as a time-stamp to the server
      only if it was negotiated with the client.
    - When creating a new profile, if this parameter is not specified, the default
      is provided by the parent profile.
    type: bool
    version_added: 2.9
  state:
    choices:
    - present
    - absent
    default: present
    description:
    - When C(present), ensures that the profile exists.
    - When C(absent), ensures the profile is removed.
    type: str
  syn_rto_base:
    description:
    - Specifies the initial RTO C(Retransmission TimeOut) base multiplier for SYN
      retransmission, in C(milliseconds).
    - This value is modified by the exponential backoff table to select the interval
      for subsequent retransmissions.
    - The valid value range is 0 - 5000 inclusive.
    - When creating a new profile, if this parameter is not specified, the default
      is provided by the parent profile.
    type: int
    version_added: 2.9
  time_wait_recycle:
    description:
    - Specifies that connections in a TIME-WAIT state are reused, if a SYN packet,
      indicating a request for a new connection, is received.
    - When C(no), connections in a TIME-WAIT state remain unused for a specified length
      of time.
    - When creating a new profile, if this parameter is not specified, the default
      is provided by the parent profile.
    type: bool
    version_added: 2.7
short_description: Manage TCP profiles on a BIG-IP
version_added: 2.6
'''

EXAMPLES = r'''
- name: Create a TCP profile
  bigip_profile_tcp:
    name: foo
    parent: f5-tcp-progressive
    time_wait_recycle: no
    idle_timeout: 300
    state: present
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost
'''

RETURN = r'''
parent:
  description: The new parent of the resource.
  returned: changed
  type: str
  sample: f5-tcp-optimized
idle_timeout:
  description: The new idle timeout of the resource.
  returned: changed
  type: int
  sample: 100
time_wait_recycle:
  description: Reuse connections in TIME-WAIT state.
  returned: changed
  type: bool
  sample: yes
nagle:
  description: Specifies the use of Nagle's algorithm.
  returned: changed
  type: str
  sample: auto
early_retransmit:
  description: Specifies the use of early fast retransmits.
  returned: changed
  type: bool
  sample: yes
proxy_options:
  description: Specifies if that the system advertises negotiated options to the server.
  returned: changed
  type: bool
  sample: no
initial_congestion_window_size:
  description: Specifies the initial congestion window size for connections to this destination.
  returned: changed
  type: int
  sample: 5
initial_receive_window_size:
  description: Specifies the initial receive window size for connections to this destination.
  returned: changed
  type: int
  sample: 10
syn_rto_base:
  description: Specifies the initial Retransmission TimeOut base multiplier for SYN retransmission.
  returned: changed
  type: int
  sample: 2000
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.basic import env_fallback

try:
    from library.module_utils.network.f5.bigip import F5RestClient
    from library.module_utils.network.f5.common import F5ModuleError
    from library.module_utils.network.f5.common import AnsibleF5Parameters
    from library.module_utils.network.f5.common import fq_name
    from library.module_utils.network.f5.common import f5_argument_spec
    from library.module_utils.network.f5.common import flatten_boolean
    from library.module_utils.network.f5.common import transform_name
except ImportError:
    from ansible_collections.f5networks.f5_modules.plugins.module_utils.network.f5.bigip import F5RestClient
    from ansible_collections.f5networks.f5_modules.plugins.module_utils.network.f5.common import F5ModuleError
    from ansible_collections.f5networks.f5_modules.plugins.module_utils.network.f5.common import AnsibleF5Parameters
    from ansible_collections.f5networks.f5_modules.plugins.module_utils.network.f5.common import fq_name
    from ansible_collections.f5networks.f5_modules.plugins.module_utils.network.f5.common import f5_argument_spec
    from ansible_collections.f5networks.f5_modules.plugins.module_utils.network.f5.common import flatten_boolean
    from ansible_collections.f5networks.f5_modules.plugins.module_utils.network.f5.common import transform_name


class Parameters(AnsibleF5Parameters):
    api_map = {
        'idleTimeout': 'idle_timeout',
        'defaultsFrom': 'parent',
        'timeWaitRecycle': 'time_wait_recycle',
        'earlyRetransmit': 'early_retransmit',
        'proxyOptions': 'proxy_options',
        'initCwnd': 'initial_congestion_window_size',
        'initRwnd': 'initial_receive_window_size',
        'synRtoBase': 'syn_rto_base'
    }

    api_attributes = [
        'idleTimeout',
        'defaultsFrom',
        'timeWaitRecycle',
        'nagle',
        'earlyRetransmit',
        'proxyOptions',
        'initCwnd',
        'initRwnd',
        'synRtoBase',
    ]

    returnables = [
        'idle_timeout',
        'parent',
        'time_wait_recycle',
        'nagle',
        'early_retransmit',
        'proxy_options',
        'initial_congestion_window_size',
        'initial_receive_window_size',
        'syn_rto_base',
    ]

    updatables = [
        'idle_timeout',
        'parent',
        'time_wait_recycle',
        'nagle',
        'early_retransmit',
        'proxy_options',
        'initial_congestion_window_size',
        'initial_receive_window_size',
        'syn_rto_base',
    ]


class ApiParameters(Parameters):
    pass


class ModuleParameters(Parameters):
    @property
    def parent(self):
        if self._values['parent'] is None:
            return None
        result = fq_name(self.partition, self._values['parent'])
        return result

    @property
    def idle_timeout(self):
        if self._values['idle_timeout'] is None:
            return None
        if self._values['idle_timeout'] == 'indefinite':
            return 4294967295
        return int(self._values['idle_timeout'])

    @property
    def time_wait_recycle(self):
        result = flatten_boolean(self._values['time_wait_recycle'])
        if result is None:
            return None
        if result == 'yes':
            return 'enabled'
        return 'disabled'

    @property
    def early_retransmit(self):
        result = flatten_boolean(self._values['early_retransmit'])
        if result is None:
            return None
        if result == 'yes':
            return 'enabled'
        return 'disabled'

    @property
    def proxy_options(self):
        result = flatten_boolean(self._values['proxy_options'])
        if result is None:
            return None
        if result == 'yes':
            return 'enabled'
        return 'disabled'

    @property
    def initial_congestion_window_size(self):
        if self._values['initial_congestion_window_size'] is None:
            return None
        if 0 <= self._values['initial_congestion_window_size'] <= 16:
            return self._values['initial_congestion_window_size']
        raise F5ModuleError(
            "Valid 'initial_congestion_window_size' must be in range 0 - 16 MSS units."
        )

    @property
    def initial_receive_window_size(self):
        if self._values['initial_receive_window_size'] is None:
            return None
        if 0 <= self._values['initial_receive_window_size'] <= 16:
            return self._values['initial_receive_window_size']
        raise F5ModuleError(
            "Valid 'initial_receive_window_size' must be in range 0 - 16 MSS units."
        )

    @property
    def syn_rto_base(self):
        if self._values['syn_rto_base'] is None:
            return None
        if 0 <= self._values['syn_rto_base'] <= 5000:
            return self._values['syn_rto_base']
        raise F5ModuleError(
            "Valid 'syn_rto_base' must be in range 0 - 5000 milliseconds."
        )


class Changes(Parameters):
    def to_return(self):
        result = {}
        try:
            for returnable in self.returnables:
                result[returnable] = getattr(self, returnable)
            result = self._filter_params(result)
        except Exception:
            pass
        return result


class UsableChanges(Changes):
    @property
    def idle_timeout(self):
        if self._values['idle_timeout'] is None:
            return None
        if 0 <= self._values['idle_timeout'] <= 4294967295:
            return self._values['idle_timeout']
        raise F5ModuleError(
            "Valid 'idle_timeout' must be in range 1 - 4294967295, or 'indefinite'."
        )


class ReportableChanges(Changes):
    @property
    def idle_timeout(self):
        if self._values['idle_timeout'] is None:
            return None
        if self._values['idle_timeout'] == 4294967295:
            return 'indefinite'
        return int(self._values['idle_timeout'])

    @property
    def time_wait_recycle(self):
        if self._values['time_wait_recycle'] is None:
            return None
        elif self._values['time_wait_recycle'] == 'enabled':
            return 'yes'
        return 'no'

    @property
    def early_retransmit(self):
        result = flatten_boolean(self._values['early_retransmit'])
        return result

    @property
    def proxy_options(self):
        result = flatten_boolean(self._values['proxy_options'])
        return result


class Difference(object):
    def __init__(self, want, have=None):
        self.want = want
        self.have = have

    def compare(self, param):
        try:
            result = getattr(self, param)
            return result
        except AttributeError:
            return self.__default(param)

    def __default(self, param):
        attr1 = getattr(self.want, param)
        try:
            attr2 = getattr(self.have, param)
            if attr1 != attr2:
                return attr1
        except AttributeError:
            return attr1


class ModuleManager(object):
    def __init__(self, *args, **kwargs):
        self.module = kwargs.get('module', None)
        self.client = F5RestClient(**self.module.params)
        self.want = ModuleParameters(params=self.module.params)
        self.have = ApiParameters()
        self.changes = UsableChanges()

    def _set_changed_options(self):
        changed = {}
        for key in Parameters.returnables:
            if getattr(self.want, key) is not None:
                changed[key] = getattr(self.want, key)
        if changed:
            self.changes = UsableChanges(params=changed)

    def _update_changed_options(self):
        diff = Difference(self.want, self.have)
        updatables = Parameters.updatables
        changed = dict()
        for k in updatables:
            change = diff.compare(k)
            if change is None:
                continue
            else:
                if isinstance(change, dict):
                    changed.update(change)
                else:
                    changed[k] = change
        if changed:
            self.changes = UsableChanges(params=changed)
            return True
        return False

    def should_update(self):
        result = self._update_changed_options()
        if result:
            return True
        return False

    def exec_module(self):
        changed = False
        result = dict()
        state = self.want.state

        if state == "present":
            changed = self.present()
        elif state == "absent":
            changed = self.absent()

        reportable = ReportableChanges(params=self.changes.to_return())
        changes = reportable.to_return()
        result.update(**changes)
        result.update(dict(changed=changed))
        self._announce_deprecations(result)
        return result

    def _announce_deprecations(self, result):
        warnings = result.pop('__warnings', [])
        for warning in warnings:
            self.client.module.deprecate(
                msg=warning['msg'],
                version=warning['version']
            )

    def present(self):
        if self.exists():
            return self.update()
        else:
            return self.create()

    def exists(self):
        uri = "https://{0}:{1}/mgmt/tm/ltm/profile/tcp/{2}".format(
            self.client.provider['server'],
            self.client.provider['server_port'],
            transform_name(self.want.partition, self.want.name)
        )
        resp = self.client.api.get(uri)
        try:
            response = resp.json()
        except ValueError:
            return False
        if resp.status == 404 or 'code' in response and response['code'] == 404:
            return False
        return True

    def update(self):
        self.have = self.read_current_from_device()
        if not self.should_update():
            return False
        if self.module.check_mode:
            return True
        self.update_on_device()
        return True

    def remove(self):
        if self.module.check_mode:
            return True
        self.remove_from_device()
        if self.exists():
            raise F5ModuleError("Failed to delete the resource.")
        return True

    def create(self):
        if self.want.parent is None:
            self.want.update({'parent': fq_name(self.want.partition, 'tcp')})
        self._set_changed_options()
        if self.module.check_mode:
            return True
        self.create_on_device()
        return True

    def create_on_device(self):
        params = self.changes.api_params()
        params['name'] = self.want.name
        params['partition'] = self.want.partition
        uri = "https://{0}:{1}/mgmt/tm/ltm/profile/tcp/".format(
            self.client.provider['server'],
            self.client.provider['server_port']
        )
        resp = self.client.api.post(uri, json=params)
        try:
            response = resp.json()
        except ValueError as ex:
            raise F5ModuleError(str(ex))

        if 'code' in response and response['code'] in [400, 403, 404]:
            if 'message' in response:
                raise F5ModuleError(response['message'])
            else:
                raise F5ModuleError(resp.content)
        return response['selfLink']

    def update_on_device(self):
        params = self.changes.api_params()
        uri = "https://{0}:{1}/mgmt/tm/ltm/profile/tcp/{2}".format(
            self.client.provider['server'],
            self.client.provider['server_port'],
            transform_name(self.want.partition, self.want.name)
        )
        resp = self.client.api.patch(uri, json=params)
        try:
            response = resp.json()
        except ValueError as ex:
            raise F5ModuleError(str(ex))

        if 'code' in response and response['code'] in [400, 404]:
            if 'message' in response:
                raise F5ModuleError(response['message'])
            else:
                raise F5ModuleError(resp.content)

    def absent(self):
        if self.exists():
            return self.remove()
        return False

    def remove_from_device(self):
        uri = "https://{0}:{1}/mgmt/tm/ltm/profile/tcp/{2}".format(
            self.client.provider['server'],
            self.client.provider['server_port'],
            transform_name(self.want.partition, self.want.name)
        )
        response = self.client.api.delete(uri)
        if response.status == 200:
            return True
        raise F5ModuleError(response.content)

    def read_current_from_device(self):
        uri = "https://{0}:{1}/mgmt/tm/ltm/profile/tcp/{2}".format(
            self.client.provider['server'],
            self.client.provider['server_port'],
            transform_name(self.want.partition, self.want.name)
        )
        resp = self.client.api.get(uri)
        try:
            response = resp.json()
        except ValueError as ex:
            raise F5ModuleError(str(ex))

        if 'code' in response and response['code'] == 400:
            if 'message' in response:
                raise F5ModuleError(response['message'])
            else:
                raise F5ModuleError(resp.content)
        return ApiParameters(params=response)


class ArgumentSpec(object):
    def __init__(self):
        self.supports_check_mode = True
        argument_spec = dict(
            name=dict(required=True),
            parent=dict(),
            idle_timeout=dict(),
            state=dict(
                default='present',
                choices=['present', 'absent']
            ),
            time_wait_recycle=dict(type='bool'),
            nagle=dict(
                choices=['enabled', 'disabled', 'auto']
            ),
            early_retransmit=dict(type='bool'),
            proxy_options=dict(type='bool'),
            initial_congestion_window_size=dict(type='int'),
            initial_receive_window_size=dict(type='int'),
            syn_rto_base=dict(type='int'),
            partition=dict(
                default='Common',
                fallback=(env_fallback, ['F5_PARTITION'])
            )
        )
        self.argument_spec = {}
        self.argument_spec.update(f5_argument_spec)
        self.argument_spec.update(argument_spec)


def main():
    spec = ArgumentSpec()

    module = AnsibleModule(
        argument_spec=spec.argument_spec,
        supports_check_mode=spec.supports_check_mode,
    )

    try:
        mm = ModuleManager(module=module)
        results = mm.exec_module()
        module.exit_json(**results)
    except F5ModuleError as ex:
        module.fail_json(msg=str(ex))


if __name__ == '__main__':
    main()
