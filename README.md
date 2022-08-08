## Kafka K8s Operator - a Charmed Operator for running Apache Kafka on Kubernetes from Canonical

This repository hosts the Kubernetes Python Operator for [Apache Kafka](https://kafka.apache.org).
The Kafka K8s Operator is a Python script that uses the latest upstream Kafka binaries released by the The Apache Software Foundation that comes with Kafka, made available using the [`ubuntu/kafka` OCI image](https://registry.hub.docker.com/r/ubuntu/kafka) distributed by Canonical.

As currently Kafka requires a paired ZooKeeper deployment in production, this operator makes use of the [ZooKeeper K8s Operator](https://github.com/canonical/zookeeper-k8s-operator) for various essential functions. 

### Usage

The Kafka and ZooKeeper operators can both be deployed and connected to each other using the Juju command line as follows:

```bash
$ juju deploy zookeeper-k8s -n 3
$ juju deploy kafka-k8s -n 3
$ juju relate kafka-k8s zookeeper-k8s
```

## A fast and fault-tolerant, real-time event streaming platform!

Manual, Day 2 operations for deploying and operating Apache Kafka, topic creation, client authentication, ACL management and more are all handled automatically using the [Juju Operator Lifecycle Manager](https://juju.is/docs/olm).

### Key Features
- SASL/SCRAM auth for Broker-Broker and Client-Broker authenticaion enabled by default.
- Access control management supported with user-provided ACL lists.
- Fault-tolerance, replication and high-availability out-of-the-box.
- Streamlined topic-creation through [Juju Actions](https://juju.is/docs/olm/working-with-actions) and [application relations](https://juju.is/docs/olm/relations)


### Checklist

- [x] Super-user creation
- [x] Inter-broker auth
- [x] Horizontally scale brokers
- [x] Username/Password creation for related applications
- [ ] Automatic topic creation with associated user ACLs
- [ ] Partition rebalancing during broker scaling
- [ ] Rack awareness support
- [ ] Persistent storage support with [Juju Storage](https://juju.is/docs/olm/defining-and-using-persistent-storage)
- [ ] TLS/SSL support

## Usage

This charm is still in active development. If you would like to contribute, please refer to [CONTRIBUTING.md](https://github.com/canonical/kafka-k8s-operator/blob/main/CONTRIBUTING.md)
