#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright: (c) 2018, F5 Networks Inc.
# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'certified'}

DOCUMENTATION = r'''author:
- Wojciech Wypior (@wojtek0806)
description:
- Manage HTTP profiles on a BIG-IP.
extends_documentation_fragment:
- f5networks.f5_modules.f5
module: bigip_profile_http
options:
  accept_xff:
    description:
    - Enables or disables trusting the client IP address, and statistics from the
      client IP address, based on the request's XFF (X-forwarded-for) headers, if
      they exist.
    - When creating a new profile, if this parameter is not specified, the default
      is provided by the parent profile.
    type: bool
    version_added: 2.9
  description:
    description:
    - Description of the profile.
    type: str
  dns_resolver:
    description:
    - Specifies the name of a configured DNS resolver, this option is mandatory when
      C(proxy_type) is set to C(explicit).
    - Format of the name can be either be prepended by partition (C(/Common/foo)),
      or specified just as an object name (C(foo)).
    - To remove the entry a value of C(none) or C('') can be set, however the profile
      C(proxy_type) must not be set as C(explicit).
    type: str
  encrypt_cookie_secret:
    description:
    - Passphrase for cookie encryption.
    - When creating a new profile, if this parameter is not specified, the default
      is provided by the parent profile.
    type: str
  encrypt_cookies:
    description:
    - Cookie names for the system to encrypt.
    - To remove the entry completely a value of C(none) or C('') should be set.
    - When creating a new profile, if this parameter is not specified, the default
      is provided by the parent profile.
    type: list
  enforcement:
    description:
    - Specifies protocol enforcement settings for the HTTP profile.
    - When creating a new profile, if this parameter is not specified, the default
      is provided by the parent profile.
    suboptions:
      excess_client_headers:
        choices:
        - reject
        - pass-through
        description:
        - Specifies the behavior when too many client headers are received.
        - If set to C(pass-through), will switch to pass through mode, when C(reject)
          the connection will be rejected.
        - When creating a new profile, if this parameter is not specified, the default
          is provided by the parent profile.
        type: str
      excess_server_headers:
        choices:
        - reject
        - pass-through
        description:
        - Specifies the behavior when too many server headers are received.
        - If set to C(pass-through), will switch to pass through mode, when C(reject)
          the connection will be rejected.
        - When creating a new profile, if this parameter is not specified, the default
          is provided by the parent profile.
        type: str
      known_methods:
        description:
        - Specifies which HTTP methods count as being known, removing RFC-defined
          methods from this list will cause the HTTP filter to not recognize them.
        - 'The default list provided with the system include: C(CONNECT), C(DELETE),
          C(GET), C(HEAD), C(LOCK), C(OPTIONS), C(POST), C(PROPFIND), C(PUT), C(TRACE)
          ,C(UNLOCK). The list can be appended by by specifying C(default) keyword
          as one of the list elements.'
        - The C(default) keyword can also be used to restore the default C(known_methods)
          on the system.
        - When creating a new profile, if this parameter is not specified, the default
          is provided by the parent profile.
        type: list
      max_header_count:
        description:
        - Specifies the maximum number of headers allowed in HTTP request/response.
        - The valid value range is between 16 and 4096 inclusive.
        - When set to C(default) the value of this parameter will be C(64)
        - When creating a new profile, if this parameter is not specified, the default
          is provided by the parent profile.
        type: str
      max_header_size:
        description:
        - Specifies the maximum header size specified in bytes.
        - The valid value range is between 0 and 4294967295 inclusive.
        - When set to C(default) the value of this parameter will be C(32768) bytes
        - When creating a new profile, if this parameter is not specified, the default
          is provided by the parent profile.
        type: str
      max_requests:
        description:
        - Specifies the number of requests that the system accepts on a per-connection
          basis.
        - The valid value range is between 0 and 4294967295 inclusive.
        - When set to C(default) the value of this parameter will be C(0), which means
          the system will not limit the number of requests per connection.
        - When creating a new profile, if this parameter is not specified, the default
          is provided by the parent profile.
        type: str
      oversize_client_headers:
        choices:
        - reject
        - pass-through
        description:
        - Specifies the behavior when too-large client headers are received.
        - If set to C(pass-through), will switch to pass through mode, when C(reject)
          the connection will be rejected.
        - When creating a new profile, if this parameter is not specified, the default
          is provided by the parent profile.
        type: str
      oversize_server_headers:
        choices:
        - reject
        - pass-through
        description:
        - Specifies the behavior when too-large server headers are received.
        - If set to C(pass-through), will switch to pass through mode, when C(reject)
          the connection will be rejected.
        - When creating a new profile, if this parameter is not specified, the default
          is provided by the parent profile.
        type: str
      pipeline:
        choices:
        - allow
        - reject
        - pass-through
        description:
        - Enables HTTP/1.1 pipelining, allowing clients to make requests even when
          prior requests have not received a response.
        - In order for this to succeed, however, destination servers must include
          support for pipelining.
        - If set to C(pass-through), pipelined data will cause the BIG-IP to immediately
          switch to pass-through mode and disable the HTTP filter.
        - When creating a new profile, if this parameter is not specified, the default
          is provided by the parent profile.
        type: str
      truncated_redirects:
        description:
        - Specifies what happens if a truncated redirect is seen from a server.
        - If C(yes), the redirect will be forwarded to the client, otherwise the malformed
          HTTP will be silently ignored.
        - When creating a new profile, if this parameter is not specified, the default
          is provided by the parent profile.
        type: bool
      unknown_method:
        choices:
        - allow
        - reject
        - pass-through
        description:
        - Specifies whether to allow, reject or switch to pass-through mode when an
          unknown HTTP method is parsed.
        - When creating a new profile, if this parameter is not specified, the default
          is provided by the parent profile.
        type: str
    type: dict
    version_added: 2.9
  fallback_host:
    description:
    - Specifies an HTTP fallback host.
    - When creating a new profile, if this parameter is not specified, the default
      is provided by the parent profile.
    type: str
    version_added: 2.9
  fallback_status_codes:
    description:
    - Specifies one or more HTTP error codes from server responses that should trigger
      a redirection to the fallback host.
    - The accepted valid error codes are as defined by rfc2616.
    - The codes can be specified as individual items or as valid ranges e.g. C(400-417)
      or C(500-505).
    - Mixing response code range across error types is invalid e.g. defining C(400-505)
      will raise an error.
    - When creating a new profile, if this parameter is not specified, the default
      is provided by the parent profile.
    type: list
    version_added: 2.9
  header_erase:
    description:
    - The name of a header, in an HTTP request, which the system removes from request.
    - To remove the entry completely a value of C(none) or C('') should be set.
    - The format of the header must be in C(KEY:VALUE) format, otherwise error is
      raised.
    - When creating a new profile, if this parameter is not specified, the default
      is provided by the parent profile.
    type: str
    version_added: 2.8
  header_insert:
    description:
    - A string that the system inserts as a header in an HTTP request.
    - To remove the entry completely a value of C(none) or C('') should be set.
    - The format of the header must be in C(KEY:VALUE) format, otherwise error is
      raised.
    - When creating a new profile, if this parameter is not specified, the default
      is provided by the parent profile.
    type: str
    version_added: 2.8
  hsts_mode:
    description:
    - When set to C(yes), enables the HSTS settings.
    - When creating a new profile, if this parameter is not specified, the default
      is provided by the parent profile.
    type: bool
    version_added: 2.8
  include_subdomains:
    description:
    - When set to C(yes), applies the HSTS policy to the HSTS host and its sub-domains.
    - When creating a new profile, if this parameter is not specified, the default
      is provided by the parent profile.
    type: bool
    version_added: 2.8
  insert_xforwarded_for:
    description:
    - When specified system inserts an X-Forwarded-For header in an HTTP request with
      the client IP address, to use with connection pooling.
    - When creating a new profile, if this parameter is not specified, the default
      is provided by the parent profile.
    type: bool
  maximum_age:
    description:
    - Specifies the maximum length of time, in seconds, that HSTS functionality requests
      that clients only use HTTPS to connect to the current host and any sub-domains
      of the current host's domain name.
    - The accepted value range is C(0 - 4294967295) seconds, a value of C(0) seconds
      re-enables plaintext HTTP access, while specifying C(indefinite) will set it
      to the maximum value.
    - When creating a new profile, if this parameter is not specified, the default
      is provided by the parent profile.
    type: str
    version_added: 2.8
  name:
    description:
    - Specifies the name of the profile.
    required: true
    type: str
  oneconnect_transformations:
    description:
    - Enables the system to perform HTTP header transformations for the purpose of
      keeping server-side connections open. This feature requires configuration of
      a OneConnect profile.
    - When creating a new profile, if this parameter is not specified, the default
      is provided by the parent profile.
    type: bool
    version_added: 2.9
  parent:
    default: /Common/http
    description:
    - Specifies the profile from which this profile inherits settings.
    - When creating a new profile, if this parameter is not specified, the default
      is the system-supplied C(http) profile.
    type: str
  partition:
    default: Common
    description:
    - Device partition to manage resources on.
    type: str
  proxy_type:
    choices:
    - reverse
    - transparent
    - explicit
    description:
    - Specifies the proxy mode for the profile.
    - When creating a new profile, if this parameter is not specified, the default
      is provided by the parent profile.
    type: str
  redirect_rewrite:
    choices:
    - none
    - all
    - matching
    - nodes
    description:
    - Specifies whether the system rewrites the URIs that are part of HTTP redirect
      (3XX) responses.
    - When set to C(none) the system will not rewrite the URI in any HTTP redirect
      responses.
    - When set to C(all) the system rewrites the URI in all HTTP redirect responses.
    - When set to C(matching) the system rewrites the URI in any HTTP redirect responses
      that match the request URI.
    - When set to C(nodes) if the URI contains a node IP address instead of a host
      name, the system changes it to the virtual server address.
    - When creating a new profile, if this parameter is not specified, the default
      is provided by the parent profile.
    type: str
  request_chunking:
    choices:
    - rechunk
    - selective
    - preserve
    description:
    - Specifies how to handle chunked and unchunked requests.
    - When creating a new profile, if this parameter is not specified, the default
      is provided by the parent profile.
    type: str
    version_added: 2.9
  response_chunking:
    choices:
    - rechunk
    - selective
    - preserve
    description:
    - Specifies how to handle chunked and unchunked responses.
    - When creating a new profile, if this parameter is not specified, the default
      is provided by the parent profile.
    type: str
    version_added: 2.9
  server_agent_name:
    description:
    - Specifies the string used as the server name in traffic generated by BIG-IP.
    - To remove the entry completely a value of C(none) or C('') should be set.
    - When creating a new profile, if this parameter is not specified, the default
      is provided by the parent profile.
    type: str
    version_added: 2.8
  sflow:
    description:
    - Specifies sFlow settings for the HTTP profile.
    - When creating a new profile, if this parameter is not specified, the default
      is provided by the parent profile.
    suboptions:
      poll_interval:
        description:
        - Specifies the maximum interval in seconds between two pollings.
        - The valid value range is between 0 and 4294967295 seconds inclusive.
        - For this setting to take effect the C(poll_interval_global) parameter must
          be set to C(no).
        - When creating a new profile, if this parameter is not specified, the default
          is provided by the parent profile.
        type: int
      poll_interval_global:
        description:
        - Specifies whether the global HTTP poll-interval setting overrides the object-level
          Cpoll-interval setting.
        - When creating a new profile, if this parameter is not specified, the default
          is provided by the parent profile.
        type: bool
      sampling_rate:
        description:
        - Specifies the ratio of packets observed to the samples generated. For example,
          a sampling rate of C(2000) specifies that 1 sample will be randomly generated
          for every 2000 packets observed.
        - The valid value range is between 0 and 4294967295 packets inclusive.
        - For this setting to take effect the C(sampling_rate_global) parameter must
          be set to C(no).
        - When creating a new profile, if this parameter is not specified, the default
          is provided by the parent profile.
        type: int
      sampling_rate_global:
        description:
        - Specifies whether the global HTTP sampling-rate setting overrides the object-level
          sampling-rate setting.
        - When creating a new profile, if this parameter is not specified, the default
          is provided by the parent profile.
        type: bool
    type: dict
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
  update_password:
    choices:
    - always
    - on_create
    default: always
    description:
    - C(always) will update passwords if the C(encrypt_cookie_secret) is specified.
    - C(on_create) will only set the password for newly created profiles.
    type: str
  xff_alternative_names:
    description:
    - Specifies alternative XFF headers instead of the default X-forwarded-for header.
    - When creating a new profile, if this parameter is not specified, the default
      is provided by the parent profile.
    type: list
    version_added: 2.9
short_description: Manage HTTP profiles on a BIG-IP
version_added: 2.7
'''

EXAMPLES = r'''
- name: Create HTTP profile
  bigip_profile_http:
    name: my_profile
    insert_xforwarded_for: yes
    redirect_rewrite: all
    state: present
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Remove HTTP profile
  bigip_profile_http:
    name: my_profile
    state: absent
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Add HTTP profile for transparent proxy
  bigip_profile_http:
    name: my_profile
    proxy_type: transparent
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
'''

RETURN = r'''
parent:
  description: Specifies the profile from which this profile inherits settings.
  returned: changed
  type: str
  sample: /Common/http
description:
  description: Description of the profile.
  returned: changed
  type: str
  sample: My profile
proxy_type:
  description: Specify proxy mode of the profile.
  returned: changed
  type: str
  sample: explicit
hsts_mode:
  description: Enables the HSTS settings.
  returned: changed
  type: bool
  sample: no
maximum_age:
  description: The maximum length of time, in seconds, that HSTS functionality requests that clients only use HTTPS.
  returned: changed
  type: str
  sample: indefinite
include_subdomains:
  description: Applies the HSTS policy to the HSTS host and its sub-domains.
  returned: changed
  type: bool
  sample: yes
server_agent_name:
  description: The string used as the server name in traffic generated by BIG-IP.
  returned: changed
  type: str
  sample: foobar
header_erase:
  description: The name of a header, in an HTTP request, which the system removes from request.
  returned: changed
  type: str
  sample: FOO:BAR
header_insert:
  description: The string that the system inserts as a header in an HTTP request.
  returned: changed
  type: str
  sample: FOO:BAR
insert_xforwarded_for:
  description: Insert X-Forwarded-For-Header.
  returned: changed
  type: bool
  sample: yes
redirect_rewrite:
  description: Rewrite URI that are part of 3xx responses.
  returned: changed
  type: str
  sample: all
encrypt_cookies:
  description: Cookie names to encrypt.
  returned: changed
  type: list
  sample: ['MyCookie1', 'MyCookie2']
dns_resolver:
  description: Configured dns resolver.
  returned: changed
  type: str
  sample: '/Common/FooBar'
accept_xff:
  description: Enables or disables trusting the client IP address, and statistics from the client IP address.
  returned: changed
  type: bool
  sample: yes
xff_alternative_names:
  description: Specifies alternative XFF headers instead of the default X-forwarded-for header.
  returned: changed
  type: list
  sample: ['FooBar', 'client1']
fallback_host:
  description: Specifies an HTTP fallback host.
  returned: changed
  type: str
  sample: 'foobar.com'
fallback_status_codes:
  description: HTTP error codes from server responses that should trigger a redirection to the fallback host.
  returned: changed
  type: list
  sample: ['400-404', '500', '501']
oneconnect_transformations:
  description: Enables or disables HTTP header transformations.
  returned: changed
  type: bool
  sample: no
request_chunking:
  description: Specifies how to handle chunked and unchunked requests.
  returned: changed
  type: str
  sample: rechunk
response_chunking:
  description: Specifies how to handle chunked and unchunked responses.
  returned: changed
  type: str
  sample: rechunk
enforcement:
  description: Specifies protocol enforcement settings for the HTTP profile.
  type: complex
  returned: changed
  contains:
    truncated_redirects:
      description: Specifies what happens if a truncated redirect is seen from a server.
      returned: changed
      type: bool
      sample: yes
    excess_server_headers:
      description: Specifies the behavior when too many server headers are received.
      returned: changed
      type: str
      sample: pass-through
    oversize_client_headers:
      description: Specifies the behavior when too-large client headers are received.
      returned: changed
      type: str
      sample: reject
    oversize_server_headers:
      description: Specifies the behavior when too-large server headers are received.
      returned: changed
      type: str
      sample: reject
    pipeline:
      description: Allows, rejects or switches to pass-through mode when dealing with pipelined data.
      returned: changed
      type: str
      sample: allow
    unknown_method:
      description: Allows, rejects or switches to pass-through mode when an unknown HTTP method is parsed.
      returned: changed
      type: str
      sample: allow
    max_header_count:
      description: The maximum number of headers allowed in HTTP request/response.
      returned: changed
      type: str
      sample: 4096
    max_header_size:
      description: The maximum header size specified in bytes.
      returned: changed
      type: str
      sample: default
    max_requests:
      description: The number of requests that the system accepts on a per-connection basis.
      returned: changed
      type: str
      sample: default
    known_methods:
      description: The list of known HTTP methods.
      returned: changed
      type: list
      sample: ['default', 'FOO', 'BAR']
  sample: hash/dictionary of values
sflow:
  description: Specifies sFlow settings for the HTTP profile.
  type: complex
  returned: changed
  contains:
    poll_interval:
      description: Specifies the maximum interval in seconds between two pollings.
      returned: changed
      type: int
      sample: 30
    poll_interval_global:
      description: Enables/Disables overriding HTTP poll-interval setting.
      returned: changed
      type: bool
      sample: yes
    sampling_rate:
      description: Specifies the ratio of packets observed to the samples generated.
      returned: changed
      type: int
      sample: 2000
    sampling_rate_global:
      description: Enables/Disables overriding HTTP sampling-rate setting.
      returned: changed
      type: bool
      sample: yes
  sample: hash/dictionary of values
'''

import re
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
    from library.module_utils.network.f5.compare import cmp_simple_list
    from library.module_utils.network.f5.urls import check_header_validity
except ImportError:
    from ansible_collections.f5networks.f5_modules.plugins.module_utils.network.f5.bigip import F5RestClient
    from ansible_collections.f5networks.f5_modules.plugins.module_utils.network.f5.common import F5ModuleError
    from ansible_collections.f5networks.f5_modules.plugins.module_utils.network.f5.common import AnsibleF5Parameters
    from ansible_collections.f5networks.f5_modules.plugins.module_utils.network.f5.common import fq_name
    from ansible_collections.f5networks.f5_modules.plugins.module_utils.network.f5.common import f5_argument_spec
    from ansible_collections.f5networks.f5_modules.plugins.module_utils.network.f5.common import flatten_boolean
    from ansible_collections.f5networks.f5_modules.plugins.module_utils.network.f5.common import transform_name
    from ansible_collections.f5networks.f5_modules.plugins.module_utils.network.f5.compare import cmp_simple_list
    from ansible_collections.f5networks.f5_modules.plugins.module_utils.network.f5.urls import check_header_validity


class Parameters(AnsibleF5Parameters):
    api_map = {
        'defaultsFrom': 'parent',
        'insertXforwardedFor': 'insert_xforwarded_for',
        'redirectRewrite': 'redirect_rewrite',
        'encryptCookies': 'encrypt_cookies',
        'encryptCookieSecret': 'encrypt_cookie_secret',
        'proxyType': 'proxy_type',
        'explicitProxy': 'explicit_proxy',
        'headerErase': 'header_erase',
        'headerInsert': 'header_insert',
        'serverAgentName': 'server_agent_name',
        'includeSubdomains': 'include_subdomains',
        'maximumAge': 'maximum_age',
        'mode': 'hsts_mode',
        'acceptXff': 'accept_xff',
        'xffAlternativeNames': 'xff_alternative_names',
        'fallbackHost': 'fallback_host',
        'fallbackStatusCodes': 'fallback_status_codes',
        'oneconnectTransformations': 'oneconnect_transformations',
        'requestChunking': 'request_chunking',
        'responseChunking': 'response_chunking',
    }

    api_attributes = [
        'insertXforwardedFor',
        'description',
        'defaultsFrom',
        'redirectRewrite',
        'encryptCookies',
        'encryptCookieSecret',
        'proxyType',
        'explicitProxy',
        'headerErase',
        'headerInsert',
        'hsts',
        'serverAgentName',
        'acceptXff',
        'xffAlternativeNames',
        'fallbackHost',
        'fallbackStatusCodes',
        'oneconnectTransformations',
        'requestChunking',
        'responseChunking',
        'enforcement',
        'sflow',
    ]

    returnables = [
        'parent',
        'description',
        'insert_xforwarded_for',
        'redirect_rewrite',
        'encrypt_cookies',
        'proxy_type',
        'explicit_proxy',
        'dns_resolver',
        'hsts_mode',
        'maximum_age',
        'include_subdomains',
        'server_agent_name',
        'header_erase',
        'header_insert',
        'accept_xff',
        'xff_alternative_names',
        'fallback_host',
        'fallback_status_codes',
        'oneconnect_transformations',
        'request_chunking',
        'response_chunking',
        'truncated_redirects',
        'excess_client_headers',
        'excess_server_headers',
        'oversize_client_headers',
        'oversize_server_headers',
        'pipeline',
        'unknown_method',
        'max_header_count',
        'max_header_size',
        'max_requests',
        'known_methods',
        'poll_interval',
        'poll_interval_global',
        'sampling_rate',
        'sampling_rate_global',
    ]

    updatables = [
        'description',
        'insert_xforwarded_for',
        'redirect_rewrite',
        'encrypt_cookies',
        'encrypt_cookie_secret',
        'proxy_type',
        'dns_resolver',
        'hsts_mode',
        'maximum_age',
        'include_subdomains',
        'server_agent_name',
        'header_erase',
        'header_insert',
        'accept_xff',
        'xff_alternative_names',
        'fallback_host',
        'fallback_status_codes',
        'oneconnect_transformations',
        'request_chunking',
        'response_chunking',
        'truncated_redirects',
        'excess_client_headers',
        'excess_server_headers',
        'oversize_client_headers',
        'oversize_server_headers',
        'pipeline',
        'unknown_method',
        'max_header_count',
        'max_header_size',
        'max_requests',
        'known_methods',
        'poll_interval',
        'poll_interval_global',
        'sampling_rate',
        'sampling_rate_global',
    ]


class ApiParameters(Parameters):
    @property
    def poll_interval(self):
        return self._values['sflow']['pollInterval']

    @property
    def poll_interval_global(self):
        return self._values['sflow']['pollIntervalGlobal']

    @property
    def sampling_rate(self):
        return self._values['sflow']['samplingRate']

    @property
    def sampling_rate_global(self):
        return self._values['sflow']['samplingRateGlobal']

    @property
    def truncated_redirects(self):
        return self._values['enforcement']['truncatedRedirects']

    @property
    def excess_client_headers(self):
        return self._values['enforcement']['excessClientHeaders']

    @property
    def excess_server_headers(self):
        return self._values['enforcement']['excessServerHeaders']

    @property
    def oversize_client_headers(self):
        return self._values['enforcement']['oversizeClientHeaders']

    @property
    def oversize_server_headers(self):
        return self._values['enforcement']['oversizeServerHeaders']

    @property
    def pipeline(self):
        return self._values['enforcement']['pipeline']

    @property
    def unknown_method(self):
        return self._values['enforcement']['unknownMethod']

    @property
    def max_header_count(self):
        return self._values['enforcement']['maxHeaderCount']

    @property
    def max_header_size(self):
        return self._values['enforcement']['maxHeaderSize']

    @property
    def max_requests(self):
        return self._values['enforcement']['maxRequests']

    @property
    def known_methods(self):
        return self._values['enforcement'].get('knownMethods', None)

    @property
    def dns_resolver(self):
        if self._values['explicit_proxy'] is None:
            return None
        if 'dnsResolver' in self._values['explicit_proxy']:
            return self._values['explicit_proxy']['dnsResolver']

    @property
    def dns_resolver_address(self):
        if self._values['explicit_proxy'] is None:
            return None
        if 'dnsResolverReference' in self._values['explicit_proxy']:
            return self._values['explicit_proxy']['dnsResolverReference']

    @property
    def include_subdomains(self):
        if self._values['hsts'] is None:
            return None
        return self._values['hsts']['includeSubdomains']

    @property
    def hsts_mode(self):
        if self._values['hsts'] is None:
            return None
        return self._values['hsts']['mode']

    @property
    def maximum_age(self):
        if self._values['hsts'] is None:
            return None
        return self._values['hsts']['maximumAge']


class ModuleParameters(Parameters):
    @property
    def accept_xff(self):
        result = flatten_boolean(self._values['accept_xff'])
        if result is None:
            return None
        if result == 'yes':
            return 'enabled'
        return 'disabled'

    @property
    def fallback_status_codes(self):
        if self._values['fallback_status_codes'] is None:
            return None

        p1 = r'(?!([4][0-1][0-7]))\d{3}'
        p2 = r'(?!(50[0-5]))\d{3}'

        for code in self._values['fallback_status_codes']:
            match_4xx = re.search(p1, code)
            if match_4xx:
                match_5xx = re.search(p2, code)
                if match_5xx:
                    raise F5ModuleError(
                        'Invalid HTTP error code or error code range specified.'
                    )
        return self._values['fallback_status_codes']

    @property
    def oneconnect_transformations(self):
        result = flatten_boolean(self._values['oneconnect_transformations'])
        if result is None:
            return None
        if result == 'yes':
            return 'enabled'
        return 'disabled'

    @property
    def proxy_type(self):
        if self._values['proxy_type'] is None:
            return None
        if self._values['proxy_type'] == 'explicit':
            if self.dns_resolver is None or self.dns_resolver == '':
                raise F5ModuleError(
                    'A proxy type cannot be set to {0} without providing DNS resolver.'.format(self._values['proxy_type'])
                )
        return self._values['proxy_type']

    @property
    def dns_resolver(self):
        if self._values['dns_resolver'] is None:
            return None
        if self._values['dns_resolver'] == '' or self._values['dns_resolver'] == 'none':
            return ''
        result = fq_name(self.partition, self._values['dns_resolver'])
        return result

    @property
    def dns_resolver_address(self):
        resolver = self.dns_resolver
        if resolver is None:
            return None
        tmp = resolver.split('/')
        link = dict(link='https://localhost/mgmt/tm/net/dns-resolver/~{0}~{1}'.format(tmp[1], tmp[2]))
        return link

    @property
    def insert_xforwarded_for(self):
        result = flatten_boolean(self._values['insert_xforwarded_for'])
        if result is None:
            return None
        if result == 'yes':
            return 'enabled'
        return 'disabled'

    @property
    def parent(self):
        if self._values['parent'] is None:
            return None
        result = fq_name(self.partition, self._values['parent'])
        return result

    @property
    def encrypt_cookies(self):
        if self._values['encrypt_cookies'] is None:
            return None
        if self._values['encrypt_cookies'] == [''] or self._values['encrypt_cookies'] == ['none']:
            return list()
        return self._values['encrypt_cookies']

    @property
    def explicit_proxy(self):
        if self.dns_resolver is None:
            return None
        result = dict(
            dnsResolver=self.dns_resolver,
            dnsResolverReference=self.dns_resolver_address
        )
        return result

    @property
    def include_subdomains(self):
        result = flatten_boolean(self._values['include_subdomains'])
        if result is None:
            return None
        if result == 'yes':
            return 'enabled'
        return 'disabled'

    @property
    def maximum_age(self):
        if self._values['maximum_age'] is None:
            return None
        if self._values['maximum_age'] == 'indefinite':
            return 4294967295
        if 0 <= int(self._values['maximum_age']) <= 4294967295:
            return int(self._values['maximum_age'])
        raise F5ModuleError(
            "Valid 'maximum_age' must be in range 0 - 4294967295, or 'indefinite'."
        )

    @property
    def hsts_mode(self):
        result = flatten_boolean(self._values['hsts_mode'])
        if result is None:
            return None
        if result == 'yes':
            return 'enabled'
        return 'disabled'

    @property
    def header_erase(self):
        header_erase = self._values['header_erase']
        if header_erase is None:
            return None
        if header_erase in ['none', '']:
            return self._values['header_erase']
        check_header_validity(header_erase)
        return header_erase

    @property
    def header_insert(self):
        header_insert = self._values['header_insert']
        if header_insert is None:
            return None
        if header_insert in ['none', '']:
            return self._values['header_insert']
        check_header_validity(header_insert)
        return header_insert

    @property
    def excess_client_headers(self):
        if self._values['enforcement'] is None:
            return None
        return self._values['enforcement']['excess_client_headers']

    @property
    def excess_server_headers(self):
        if self._values['enforcement'] is None:
            return None
        return self._values['enforcement']['excess_server_headers']

    @property
    def oversize_client_headers(self):
        if self._values['enforcement'] is None:
            return None
        return self._values['enforcement']['oversize_client_headers']

    @property
    def oversize_server_headers(self):
        if self._values['enforcement'] is None:
            return None
        return self._values['enforcement']['oversize_server_headers']

    @property
    def pipeline(self):
        if self._values['enforcement'] is None:
            return None
        return self._values['enforcement']['pipeline']

    @property
    def unknown_method(self):
        if self._values['enforcement'] is None:
            return None
        return self._values['enforcement']['unknown_method']

    @property
    def truncated_redirects(self):
        if self._values['enforcement'] is None:
            return None
        result = flatten_boolean(self._values['enforcement']['truncated_redirects'])
        if result is None:
            return None
        if result == 'yes':
            return 'enabled'
        return 'disabled'

    @property
    def max_header_count(self):
        if self._values['enforcement'] is None:
            return None
        if self._values['enforcement']['max_header_count'] is None:
            return None
        if self._values['enforcement']['max_header_count'] == 'default':
            return 64
        if 16 <= int(self._values['enforcement']['max_header_count']) <= 4096:
            return int(self._values['enforcement']['max_header_count'])
        raise F5ModuleError(
            "Valid 'max_header_count' must be in range 16 - 4096, or 'default'."
        )

    @property
    def max_header_size(self):
        if self._values['enforcement'] is None:
            return None
        if self._values['enforcement']['max_header_size'] is None:
            return None
        if self._values['enforcement']['max_header_size'] == 'default':
            return 32768
        if 0 <= int(self._values['enforcement']['max_header_size']) <= 4294967295:
            return int(self._values['enforcement']['max_header_size'])
        raise F5ModuleError(
            "Valid 'max_header_size' must be in range 0 - 4294967295, or 'default'."
        )

    @property
    def max_requests(self):
        if self._values['enforcement'] is None:
            return None
        if self._values['enforcement']['max_requests'] is None:
            return None
        if self._values['enforcement']['max_requests'] == 'default':
            return 0
        if 0 <= int(self._values['enforcement']['max_requests']) <= 4294967295:
            return int(self._values['enforcement']['max_requests'])
        raise F5ModuleError(
            "Valid 'max_requests' must be in range 0 - 4294967295, or 'default'."
        )

    @property
    def known_methods(self):
        if self._values['enforcement'] is None:
            return None
        defaults = ['CONNECT', 'DELETE', 'GET', 'HEAD', 'LOCK', 'OPTIONS', 'POST', 'PROPFIND', 'PUT', 'TRACE', 'UNLOCK']
        known = self._values['enforcement']['known_methods']
        if known is None:
            return None
        if len(known) == 1:
            if known[0] == 'default':
                return defaults
            if known[0] == '':
                return []
        if 'default' in known:
            to_return = [method for method in known if method != 'default']
            to_return.extend(defaults)
            return to_return
        result = [method for method in known]
        return result

    @property
    def poll_interval(self):
        if self._values['sflow'] is None:
            return None
        if self._values['sflow']['poll_interval'] is None:
            return None
        if 0 <= self._values['sflow']['poll_interval'] <= 4294967295:
            return self._values['sflow']['poll_interval']
        raise F5ModuleError(
            "Valid 'poll_interval' must be in range 0 - 4294967295 seconds."
        )

    @property
    def sampling_rate(self):
        if self._values['sflow'] is None:
            return None
        if self._values['sflow']['sampling_rate'] is None:
            return None
        if 0 <= self._values['sflow']['sampling_rate'] <= 4294967295:
            return self._values['sflow']['sampling_rate']
        raise F5ModuleError(
            "Valid 'sampling_rate' must be in range 0 - 4294967295 packets."
        )

    @property
    def poll_interval_global(self):
        if self._values['sflow'] is None:
            return None
        result = flatten_boolean(self._values['sflow']['poll_interval_global'])
        return result

    @property
    def sampling_rate_global(self):
        if self._values['sflow'] is None:
            return None
        result = flatten_boolean(self._values['sflow']['sampling_rate_global'])
        return result


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
    def explicit_proxy(self):
        result = dict()
        if self._values['dns_resolver'] is not None:
            result['dnsResolver'] = self._values['dns_resolver']
        if self._values['dns_resolver_address'] is not None:
            result['dnsResolverReference'] = self._values['dns_resolver_address']
        if not result:
            return None
        return result

    @property
    def hsts(self):
        result = dict()
        if self._values['hsts_mode'] is not None:
            result['mode'] = self._values['hsts_mode']
        if self._values['maximum_age'] is not None:
            result['maximumAge'] = self._values['maximum_age']
        if self._values['include_subdomains'] is not None:
            result['includeSubdomains'] = self._values['include_subdomains']
        if not result:
            return None
        return result

    @property
    def enforcement(self):
        to_filter = dict(
            excessClientHeaders=self._values['excess_client_headers'],
            excessServerHeaders=self._values['excess_server_headers'],
            knownMethods=self._values['known_methods'],
            maxHeaderCount=self._values['max_header_count'],
            maxHeaderSize=self._values['max_header_size'],
            maxRequests=self._values['max_requests'],
            oversizeClientHeaders=self._values['oversize_client_headers'],
            oversizeServerHeaders=self._values['oversize_server_headers'],
            pipeline=self._values['pipeline'],
            truncatedRedirects=self._values['truncated_redirects'],
            unknownMethod=self._values['unknown_method']
        )
        result = self._filter_params(to_filter)
        if result:
            return result

    @property
    def sflow(self):
        to_filter = dict(
            pollInterval=self._values['poll_interval'],
            pollIntervalGlobal=self._values['poll_interval_global'],
            samplingRate=self._values['sampling_rate'],
            samplingRateGlobal=self._values['sampling_rate_global'],
        )
        result = self._filter_params(to_filter)
        if result:
            return result


class ReportableChanges(Changes):
    returnables = [
        'parent',
        'description',
        'insert_xforwarded_for',
        'redirect_rewrite',
        'encrypt_cookies',
        'proxy_type',
        'explicit_proxy',
        'dns_resolver',
        'hsts_mode',
        'maximum_age',
        'include_subdomains',
        'server_agent_name',
        'header_erase',
        'header_insert',
        'accept_xff',
        'xff_alternative_names',
        'fallback_host',
        'fallback_status_codes',
        'oneconnect_transformations',
        'request_chunking',
        'response_chunking',
        'enforcement',
        'sflow'
    ]

    @property
    def insert_xforwarded_for(self):
        if self._values['insert_xforwarded_for'] is None:
            return None
        elif self._values['insert_xforwarded_for'] == 'enabled':
            return 'yes'
        return 'no'

    @property
    def hsts_mode(self):
        if self._values['hsts_mode'] is None:
            return None
        elif self._values['hsts_mode'] == 'enabled':
            return 'yes'
        return 'no'

    @property
    def include_subdomains(self):
        if self._values['include_subdomains'] is None:
            return None
        elif self._values['include_subdomains'] == 'enabled':
            return 'yes'
        return 'no'

    @property
    def maximum_age(self):
        if self._values['maximum_age'] is None:
            return None
        if self._values['maximum_age'] == 4294967295:
            return 'indefinite'
        return int(self._values['maximum_age'])

    @property
    def truncated_redirects(self):
        result = flatten_boolean(self._values['truncated_redirects'])
        return result

    @property
    def max_header_count(self):
        if self._values['max_header_count'] is None:
            return None
        if self._values['max_header_count'] == 64:
            return 'default'
        return str(self._values['max_header_count'])

    @property
    def max_header_size(self):
        if self._values['max_header_size'] is None:
            return None
        if self._values['max_header_size'] == 32768:
            return 'default'
        return str(self._values['max_header_size'])

    @property
    def max_requests(self):
        if self._values['max_requests'] is None:
            return None
        if self._values['max_requests'] == 0:
            return 'default'
        return str(self._values['max_requests'])

    @property
    def known_methods(self):
        defaults = ['CONNECT', 'DELETE', 'GET', 'HEAD', 'LOCK', 'OPTIONS', 'POST', 'PROPFIND', 'PUT', 'TRACE', 'UNLOCK']
        known = self._values['known_methods']
        if known is None:
            return None
        if not known:
            return ['']
        if set(known) == set(defaults):
            return ['default']
        if set(known).issuperset(set(defaults)):
            result = [item for item in known if item not in defaults]
            result.append('default')
            return result
        return known

    @property
    def enforcement(self):
        to_filter = dict(
            excess_client_headers=self._values['excess_client_headers'],
            excess_server_headers=self._values['excess_server_headers'],
            known_methods=self.known_methods,
            max_header_count=self.max_header_count,
            max_header_size=self.max_header_size,
            max_requests=self.max_requests,
            oversize_client_headers=self._values['oversize_client_headers'],
            oversize_server_headers=self._values['oversize_server_headers'],
            pipeline=self._values['pipeline'],
            truncated_redirects=self.truncated_redirects,
            unknown_method=self._values['unknown_method']
        )
        result = self._filter_params(to_filter)
        if result:
            return result

    @property
    def accept_xff(self):
        result = flatten_boolean(self._values['accept_xff'])
        return result

    @property
    def oneconnect_transformations(self):
        result = flatten_boolean(self._values['oneconnect_transformations'])
        return result

    @property
    def sflow(self):
        to_filter = dict(
            poll_interval=self._values['poll_interval'],
            poll_interval_global=self._values['poll_interval_global'],
            sampling_rate=self._values['sampling_rate'],
            sampling_rate_global=self._values['sampling_rate_global'],
        )
        result = self._filter_params(to_filter)
        if result:
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

    @property
    def parent(self):
        if self.want.parent != self.have.parent:
            raise F5ModuleError(
                "The parent http profile cannot be changed"
            )

    @property
    def dns_resolver(self):
        if self.want.dns_resolver is None:
            return None
        if self.want.dns_resolver == '':
            if self.have.dns_resolver is None or self.have.dns_resolver == 'none':
                return None
            elif self.have.proxy_type == 'explicit' and self.want.proxy_type is None:
                raise F5ModuleError(
                    "DNS resolver cannot be empty or 'none' if an existing profile proxy type is set to {0}.".format(self.have.proxy_type)
                )
            elif self.have.dns_resolver is not None:
                return self.want.dns_resolver
        if self.have.dns_resolver is None:
            return self.want.dns_resolver

    @property
    def header_erase(self):
        if self.want.header_erase is None:
            return None
        if self.want.header_erase in ['none', '']:
            if self.have.header_erase in [None, 'none']:
                return None
        if self.want.header_erase != self.have.header_erase:
            return self.want.header_erase

    @property
    def header_insert(self):
        if self.want.header_insert is None:
            return None
        if self.want.header_insert in ['none', '']:
            if self.have.header_insert in [None, 'none']:
                return None
        if self.want.header_insert != self.have.header_insert:
            return self.want.header_insert

    @property
    def server_agent_name(self):
        if self.want.server_agent_name is None:
            return None
        if self.want.server_agent_name in ['none', '']:
            if self.have.server_agent_name in [None, 'none']:
                return None
        if self.want.server_agent_name != self.have.server_agent_name:
            return self.want.server_agent_name

    @property
    def encrypt_cookies(self):
        if self.want.encrypt_cookies is None:
            return None
        if self.have.encrypt_cookies in [None, []]:
            if not self.want.encrypt_cookies:
                return None
            else:
                return self.want.encrypt_cookies
        if set(self.want.encrypt_cookies) != set(self.have.encrypt_cookies):
            return self.want.encrypt_cookies

    @property
    def encrypt_cookie_secret(self):
        if self.want.encrypt_cookie_secret != self.have.encrypt_cookie_secret:
            if self.want.update_password == 'always':
                result = self.want.encrypt_cookie_secret
                return result

    @property
    def xff_alternative_names(self):
        result = cmp_simple_list(self.want.xff_alternative_names, self.have.xff_alternative_names)
        return result

    @property
    def fallback_status_codes(self):
        result = cmp_simple_list(self.want.fallback_status_codes, self.have.fallback_status_codes)
        return result

    @property
    def known_methods(self):
        result = cmp_simple_list(self.want.known_methods, self.have.known_methods)
        return result


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

    def absent(self):
        if self.exists():
            return self.remove()
        return False

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
        self._set_changed_options()
        if self.module.check_mode:
            return True
        self.create_on_device()
        return True

    def exists(self):
        uri = "https://{0}:{1}/mgmt/tm/ltm/profile/http/{2}".format(
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

    def create_on_device(self):
        params = self.changes.api_params()
        params['name'] = self.want.name
        params['partition'] = self.want.partition
        uri = "https://{0}:{1}/mgmt/tm/ltm/profile/http/".format(
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
        uri = "https://{0}:{1}/mgmt/tm/ltm/profile/http/{2}".format(
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

    def remove_from_device(self):
        uri = "https://{0}:{1}/mgmt/tm/ltm/profile/http/{2}".format(
            self.client.provider['server'],
            self.client.provider['server_port'],
            transform_name(self.want.partition, self.want.name)
        )
        response = self.client.api.delete(uri)
        if response.status == 200:
            return True
        raise F5ModuleError(response.content)

    def read_current_from_device(self):
        uri = "https://{0}:{1}/mgmt/tm/ltm/profile/http/{2}".format(
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
        self.chunk = ['rechunk', 'selective', 'preserve']
        self.choices = ['pass-through', 'reject']
        self.select = ['allow', 'pass-through', 'reject']
        argument_spec = dict(
            name=dict(required=True),
            parent=dict(default='/Common/http'),
            description=dict(),
            accept_xff=dict(type='bool'),
            xff_alternative_names=dict(type='list'),
            fallback_host=dict(),
            fallback_status_codes=dict(type='list'),
            oneconnect_transformations=dict(type='bool'),
            request_chunking=dict(choices=self.chunk),
            response_chunking=dict(choices=self.chunk),
            proxy_type=dict(
                choices=[
                    'reverse',
                    'transparent',
                    'explicit'
                ]
            ),
            dns_resolver=dict(),
            insert_xforwarded_for=dict(type='bool'),
            redirect_rewrite=dict(
                choices=[
                    'none',
                    'all',
                    'matching',
                    'nodes'
                ]
            ),
            encrypt_cookies=dict(type='list'),
            encrypt_cookie_secret=dict(no_log=True),
            update_password=dict(
                default='always',
                choices=['always', 'on_create']
            ),
            header_erase=dict(),
            header_insert=dict(),
            server_agent_name=dict(),
            hsts_mode=dict(type='bool'),
            maximum_age=dict(),
            include_subdomains=dict(type='bool'),
            enforcement=dict(
                type='dict',
                options=dict(
                    truncated_redirects=dict(type='bool'),
                    excess_client_headers=dict(choices=self.choices),
                    excess_server_headers=dict(choices=self.choices),
                    oversize_client_headers=dict(choices=self.choices),
                    oversize_server_headers=dict(choices=self.choices),
                    pipeline=dict(choices=self.select),
                    unknown_method=dict(choices=self.select),
                    max_header_count=dict(),
                    max_header_size=dict(),
                    max_requests=dict(),
                    known_methods=dict(type='list'),
                )
            ),
            sflow=dict(
                type='dict',
                options=dict(
                    poll_interval=dict(type='int'),
                    poll_interval_global=dict(type='bool'),
                    sampling_rate=dict(type='int'),
                    sampling_rate_global=dict(type='bool'),
                )
            ),
            state=dict(
                default='present',
                choices=['present', 'absent']
            ),
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
