# RoboDesk V0.1 — Lab acceptance plan

Status: prepared, no device tests performed. Scope: authorized remote support of ordinary test phones and lab PCs only. Use synthetic data, explicit local session consent, and an isolated test network. No operational controller or live vehicle tests.

## Build acceptance
- [ ] Record exact Git commit, run ID, job conclusions and artifact IDs.
- [ ] Obtain Android ARM64/ARMv7 and Windows x64 artifacts directly from the approved build run. Reject incomplete or expired artifacts.
- [ ] Record archive and extracted binary SHA-256 hashes, scan files, inspect Android manifest and signing certificate, inspect Windows signatures and package dependencies.
- [ ] Label debug-signed APK and unsigned Windows folder as lab-only; never distribute as production packages.
- [ ] Verify that displayed branding matches approved source artwork and that upstream notices remain present.

## Authorized lab testing
- [ ] Use a disposable Android phone and Windows test PC with no confidential data.
- [ ] Verify app installation, display label, icons, launch, exit, and uninstall.
- [ ] Check screen sharing with explicit local consent and a visible session indicator.
- [ ] Confirm that denying permissions or ending a session prevents continued access.
- [ ] Verify a disconnected network stops the session; re-establishment requires the approved authorization policy.
- [ ] Measure responsiveness of ordinary UI screen sharing and document device/OS compatibility.
- [ ] Inspect outbound network requests and reject unexpected third-party services; verify approved host and authenticated endpoint identity.
- [ ] Verify session logs exclude passwords, private keys and captured screen content.

## Release blockers
Any failed authorization, unexpected network egress, missing provenance, unknown dependency, unsigned production executable, or unreviewed identity migration blocks release. A passing build alone is not an acceptance result.

## Evidence
Record tester, date, hardware/OS, commit, build artifact, expected result, observed result, status, and redacted evidence. Keep actual test logs on organization-controlled storage, not in this public repository.
