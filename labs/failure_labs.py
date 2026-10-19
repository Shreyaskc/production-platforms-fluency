"""Deterministic teaching models; no external services, I/O, or dependencies."""
import sys

def replay():
    # Inject crash between external effect and offset commit: source redelivers.
    deliveries = [('acme', 'doc-7', 3), ('acme', 'doc-7', 3)]
    naive = len(deliveries)
    inbox, effects = set(), 0
    for key in deliveries:
        if key not in inbox:
            # Modeled as one atomic transaction; a real DB must enforce it.
            inbox.add(key)
            effects += 1
    assert naive == 2 and effects == 1
    print('replay: bad effects=2; atomic inbox effects=1 PASS')

def revocation():
    cache = {'revision': 1, 'allow': True}
    authority = {'revision': 2, 'allow': False}
    leaked = cache['allow']
    def authorize(min_revision):
        decision = cache if cache['revision'] >= min_revision else authority
        return decision['revision'] >= min_revision and decision['allow']
    assert leaked and not authorize(2)
    # If the authority cannot prove the required revision, deny.
    assert not authorize(3)
    print('revocation: stale cache leaked=True; revision-gated allow=False PASS')

def backfill():
    live_delete = {'version': 5, 'deleted': True}
    old_snapshot = {'version': 4, 'deleted': False}
    naive = dict(old_snapshot)
    guarded = dict(live_delete)
    for event in [old_snapshot, live_delete, old_snapshot]:
        if event['version'] > guarded['version']:
            guarded = dict(event)
    assert not naive['deleted'] and guarded['deleted'] and guarded['version'] == 5
    print('backfill: naive resurrected=True; guarded deleted=True version=5 PASS')

def partition():
    writes = [(8, 'new leader'), (7, 'stale leader')]
    naive = writes[-1][1]
    epoch, value = 0, None
    for token, candidate in writes:
        if token >= epoch:
            epoch, value = token, candidate
    assert naive == 'stale leader' and value == 'new leader' and epoch == 8
    print('partition: unfenced=stale leader; sink-fenced=new leader PASS')

LABS = dict(replay=replay, revocation=revocation, backfill=backfill, partition=partition)
if __name__ == '__main__':
    name = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if name != 'all' and name not in LABS:
        sys.exit('Choose all, replay, revocation, backfill, or partition')
    for lab in LABS.values() if name == 'all' else [LABS[name]]:
        lab()
