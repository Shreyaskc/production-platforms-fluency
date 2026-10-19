# Lightweight failure laboratory
Run `python3 labs/failure_labs.py all` from the project root. Python 3 standard library only; milliseconds of CPU, no network or writes. Each lab asserts both the bad outcome and repaired invariant. Read the code after predicting its output.

| Lab | Injection | Answer key | Production boundary not modeled |
| --- | --- | --- | --- |
| replay | Crash after effect before offset | Two deliveries, one durable-inbox effect | Real transaction isolation, retention, side effects outside DB |
| revocation | Cached allow predates removal | Required revision 2 rejects stale cache; revision 3 fails closed | Group graph, distributed invalidation, in-flight output |
| backfill | Old snapshot arrives after deletion | Version 5 tombstone wins over version 4 | Log retention, source epochs, snapshot consistency |
| partition | Old owner resumes after election | Sink rejects epoch 7 after epoch 8 | Consensus, durability and token issuance |

Extensions: add a second tenant with the same document ID; insert a duplicate delete; request an unavailable policy revision; test an old owner before and after the new owner's first write. Explain why a fencing token is ineffective if the sink ignores it. Check equal-version conflicts explicitly: real systems need a deterministic source contract; this model ignores equal versions.

Game-day safety: use only synthetic data. Record predictions, observed output, invariant, mitigation and recovery proof. Stop on unexpected host load. These simulations are intentionally bounded and are not real cluster chaos tests.
