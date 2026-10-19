# Validation — 2026-10-19

Passed:
- Node syntax checks for app.js/content.js.
- Four Python failure labs: assertions verify incorrect outcome and repair for replay, ACL revocation, stale backfill and split-brain fencing.
- Installed Chrome via Playwright: search results, hidden hint disclosure, note persistence after reload, completion persistence after reload, backlog calculation (1200 seconds), overload refusal, unknown-route fallback, zero uncaught JS errors.
- Viewports 390×900 and 1440×900: no horizontal overflow; full-page screenshots visually inspected at both sizes.
- All 14 official reference links plus three course-navigation links: HTTP 200 with existing network access. URL checks establish reachability, not correctness of every referenced document.

Browser suite: `PLAYWRIGHT_MODULE=/path/to/playwright node tests/browser.cjs`. Uses installed Chrome; do not install a browser on a resource-constrained host without need. Override `COURSE_URL` with a served/live root URL (including final slash). Browser tests use an isolated temporary profile and synthetic notes. Screenshots go to /tmp.

Limits: local loopback preview timed out in the automation environment, so initial interaction checks used file URLs. Manual screen-reader/keyboard-only audits, Safari/Firefox, real distributed databases, real connectors, real Kubernetes, real cloud costs and real tenant security integration were not tested. Failure labs are bounded teaching simulations, not a demonstration of production exactly-once or revocation guarantees. NVIDIA JR2021526's exact posting was not independently retrievable; alignment is thematic only. Live deployment verification is recorded separately after publication.
