"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2016 The TensorFlow Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================
"""

import builtins
import typing

import google.protobuf.descriptor
import google.protobuf.message
import tensorflow.core.protobuf.cluster_pb2
import tensorflow.core.protobuf.config_pb2
import tensorflow.core.protobuf.device_filters_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class ServerDef(google.protobuf.message.Message):
    """Defines the configuration of a single TensorFlow server."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_FIELD_NUMBER: builtins.int
    JOB_NAME_FIELD_NUMBER: builtins.int
    REPLICA_FIELD_NUMBER: builtins.int
    TASK_INDEX_FIELD_NUMBER: builtins.int
    DEFAULT_SESSION_CONFIG_FIELD_NUMBER: builtins.int
    PROTOCOL_FIELD_NUMBER: builtins.int
    PORT_FIELD_NUMBER: builtins.int
    CLUSTER_DEVICE_FILTERS_FIELD_NUMBER: builtins.int
    job_name: builtins.str
    """The name of the job of which this server is a member.

    NOTE(mrry): The `cluster` field must contain a `JobDef` with a `name` field
    that matches this name.
    """
    replica: builtins.int
    """Replica this server manages."""
    task_index: builtins.int
    """The task index of this server in its job.

    NOTE: The `cluster` field must contain a `JobDef` with a matching `name`
    and a mapping in its `tasks` field for this index.
    """
    protocol: builtins.str
    """The protocol to be used by this server.

    Acceptable values include: "grpc", "grpc+verbs".
    """
    port: builtins.int
    """The server port. If not set, then we identify the port from the job_name."""
    @property
    def cluster(self) -> tensorflow.core.protobuf.cluster_pb2.ClusterDef:
        """The cluster of which this server is a member."""

    @property
    def default_session_config(self) -> tensorflow.core.protobuf.config_pb2.ConfigProto:
        """The default configuration for sessions that run on this server."""

    @property
    def cluster_device_filters(self) -> tensorflow.core.protobuf.device_filters_pb2.ClusterDeviceFilters:
        """Device filters for remote tasks in the cluster.
        NOTE: This is an experimental feature and only effective in TensorFlow 2.x.
        """

    def __init__(
        self,
        *,
        cluster: tensorflow.core.protobuf.cluster_pb2.ClusterDef | None = ...,
        job_name: builtins.str | None = ...,
        replica: builtins.int | None = ...,
        task_index: builtins.int | None = ...,
        default_session_config: tensorflow.core.protobuf.config_pb2.ConfigProto | None = ...,
        protocol: builtins.str | None = ...,
        port: builtins.int | None = ...,
        cluster_device_filters: tensorflow.core.protobuf.device_filters_pb2.ClusterDeviceFilters | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing.Literal[
            "cluster",
            b"cluster",
            "cluster_device_filters",
            b"cluster_device_filters",
            "default_session_config",
            b"default_session_config",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "cluster",
            b"cluster",
            "cluster_device_filters",
            b"cluster_device_filters",
            "default_session_config",
            b"default_session_config",
            "job_name",
            b"job_name",
            "port",
            b"port",
            "protocol",
            b"protocol",
            "replica",
            b"replica",
            "task_index",
            b"task_index",
        ],
    ) -> None: ...

global___ServerDef = ServerDef
