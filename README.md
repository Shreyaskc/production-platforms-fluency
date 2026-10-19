# Production Platforms Fluency

A buildless, accessible learning app for principal-level enterprise data and AI platform reasoning. Original hypothetical content; no hiring guarantees or employer-private claims.

## Run locally

From this directory: `python3 -m http.server 8084`, then open `http://localhost:8084`. No install, API keys, cloud resources or paid services. Python labs: `python3 labs/failure_labs.py all`.

## Navigate

- Learning path: 14 sequenced lessons, about 13 hours plus practice. Every lesson has a numerical exercise, hidden hint/worked solution, failure-boundary scenario and defense prompt.
- Failure laboratory: four runnable deterministic Python models and an interactive backlog calculator.
- Incident reviews: three original synthetic postmortems, containment and measurable follow-ups.
- Glossary: precise definitions and explicitly labeled analogies.
- Cheat sheets: operational formulas and rollout/incident checklists.
- Architecture defense: timed capstone, game-day injects and six-dimension rubric.
- Sources: primary references and role-alignment limitations.

Coverage: replication/quorums/fencing; indexes/query plans; CDC/backfills/schema evolution; checkpoints/idempotency/outbox; isolation/admission; ACL revocation; secure connectors; ACL-aware retrieval/DLP/audit; freshness/SLOs/budgets; incident command; capacity/cost/storage; Kubernetes/networking; migrations/rollback; architecture defense.

Prerequisites are linked to AI Learning, System Design Fluency and DSA Fluency via the Courses registry in `app.js`. Add future courses only with `launched:true` after verifying their live URLs. Do not pre-link planned siblings. Existing sites were supplied by the user; connectivity limitations during creation are documented in TESTING.md.

## Content and contribution

`content.js` holds lesson data. `app.js` holds views, glossary, case studies and registry. `style.css` handles responsive layout. Keep lesson IDs stable for saved browser progress. Add original exercises with unit-bearing calculations, failure timelines and primary references. State assumptions and implementation boundaries. Never add private examples, personal achievements or copied paid content. Validate references for the deployed software version.

Local storage key `ppf-v1` stores only notes and completed IDs; no analytics or backend. Reset prompts before deleting local progress. Storage failure leaves notes editable but unsaved.

## Test

`node --check app.js`, `node --check content.js`, `python3 labs/failure_labs.py all`.

Browser QA should cover search, lesson navigation, details disclosures, note persistence, completion persistence, reset cancellation, calculator overload handling, unknown routes and mobile overflow. See TESTING.md for the actual executed checks. Labs are deterministic models, not production integration or real Kubernetes failure testing.

## Publication

Public repository and GitHub Pages release authorized in the parent conversation. No credential changes, scope expansion, paid services or edits to sibling repositories. Static branch deployment needs only these source files; no build step.
