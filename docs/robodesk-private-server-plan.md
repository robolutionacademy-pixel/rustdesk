# RoboDesk private server — deployment planning
Status: not deployed. This document covers authorized general desktop support on lab computers and ordinary Android test phones, not operational vehicle control.

- Reserve an organization-owned Linux host on an isolated test network. No public exposure by default.
- Review and pin an official RustDesk Server OSS image to a tested version and digest, record its license and provenance.
- Official deployment reference: https://rustdesk.com/docs/en/self-host/rustdesk-server-oss/docker/
- Use the organization-managed identity and relay services (hbbs/hbbr). Establish host access controls, updates, backups, firewall review and monitoring before connecting clients.
- Proposed DNS name desk.robolutionbd.com is unverified. Do not hardcode it or any server key until the owner verifies DNS, deployment and the public key fingerprint.
- Keep credentials, private keys, session records and real network identifiers outside this public repository.
- Release gate: demonstrate that lab clients use the approved endpoint and reject unknown endpoints, inspect outgoing connections including update checks, test session consent and revocation, verify access logs and review dependencies. Self-hosting alone is not a security guarantee.
- Production sign-off requires independent security review and owner authorization. No server access or DNS administration has been provided yet.
