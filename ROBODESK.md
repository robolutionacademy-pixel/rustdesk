# RoboDesk — development notes

Robolution Technologies Ltd. | Development target 0.1.0

This is a derivative of RustDesk. Preserve upstream copyright, AGPL-3.0 license notices and applicable corresponding-source obligations. This branch is an initial branding change, not a release.

## Scope
- Android and Windows display branding. Preserve internal identifiers until migration and compatibility are reviewed.
- Android and Windows launcher assets and display labels are committed. Runtime identity, original artwork fidelity, signing identities and verified build outputs remain pending.
- Planned self-hosted ID and relay service; no production endpoint or key has been provisioned. Do not use this branch for confidential sessions.
- No server secrets, credentials, operational location data or private signing keys in this public repository.

## Release gates
- Inspect runtime branding and upstream update/network endpoints.
- Compile and test Android and Windows clients; verify signatures and package identities.
- Configure organization-controlled server, authenticate approved endpoints and verify encrypted connections and network egress.
- Validate screen sharing and general authorized desktop support on non-operational test devices. Not a flight-control system.
- Review upstream license obligations, dependencies and security before distribution.

## Lab build (development only)
The RoboDesk lab build workflow derives Android ARM64/ARMv7 and Windows x64 build jobs from upstream Flutter CI. It gates compilation on branding preflight, uploads short-lived test artifacts, and does not publish a release or pass production signing secrets. Android artifacts use debug signing; Windows artifacts are unsigned application folders, not final installers. Internal filenames and package identifiers may still say RustDesk. Do not deploy to operational equipment or enter confidential information.
