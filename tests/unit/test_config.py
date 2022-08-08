#!/usr/bin/env python3
# Copyright 2022 Canonical Ltd.
# See LICENSE file for licensing details.

import unittest

import ops.testing
from ops.testing import Harness

from charm import KafkaK8sCharm

ops.testing.SIMULATE_CAN_CONNECT = True


class TestKafkaConfig(unittest.TestCase):
    def setUp(self):
        self.harness = Harness(KafkaK8sCharm)
        self.addCleanup(self.harness.cleanup)
        self.harness.begin_with_initial_hooks()
        self.relation_id = self.harness.add_relation("zookeeper", "kafka-k8s")

    def test_zookeeper_config_succeeds_fails_config(self):
        self.harness.update_relation_data(
            self.relation_id,
            self.harness.charm.app.name,
            {
                "chroot": "/kafka",
                "username": "moria",
                "endpoints": "1.1.1.1,2.2.2.2",
                "uris": "1.1.1.1:2181,2.2.2.2:2181/kafka",
            },
        )
        self.assertDictEqual(self.harness.charm.kafka_config.zookeeper_config, {})

    def test_zookeeper_config_succeeds_valid_config(self):
        self.harness.update_relation_data(
            self.relation_id,
            self.harness.charm.app.name,
            {
                "chroot": "/kafka",
                "username": "moria",
                "password": "mellon",
                "endpoints": "1.1.1.1,2.2.2.2",
                "uris": "1.1.1.1:2181/kafka,2.2.2.2:2181/kafka",
            },
        )
        self.assertIn("connect", self.harness.charm.kafka_config.zookeeper_config.keys())
        self.assertEqual(
            self.harness.charm.kafka_config.zookeeper_config["connect"],
            "1.1.1.1:2181,2.2.2.2:2181/kafka",
        )
