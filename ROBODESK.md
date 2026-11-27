# RoboDesk — development notes

Robolution Technologies Ltd. | Development target 0.1.0

This is a derivative of RustDesk. Preserve upstream copyright, AGPL-3.0 license notices and applicable corresponding-source obligations. This branch is an initial branding change, not a release.

## Scope
- Android and Windows display branding. Preserve internal identifiers until migration and compatibility are reviewed.
- Company logo assets, runtime name, signing identities and build outputs remain pending.
- Planned self-hosted ID and relay service; no production endpoint or key has been provisioned. Do not use this branch for confidential sessions.
- No server secrets, credentials, operational location data or private signing keys in this public repository.

## Release gates
- Inspect runtime branding and upstream update/network endpoints.
- Compile and test Android and Windows clients; verify signatures and package identities.
- Configure organization-controlled server, authenticate approved endpoints and verify encrypted connections and network egress.
- Validate screen sharing and general authorized desktop support on non-operational test devices. Not a flight-control system.
- Review upstream license obligations, dependencies and security before distribution.
