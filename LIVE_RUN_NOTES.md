2026-08-11T04:58:54Z - live run for a-branch-goes-whoever-merged-it

## extension-stages: a chain of one workflow stage

The chain that follows a merge, run for real for the first time.
The repository declares one step, `workflow`, which waits for the runs the merge itself started on `develop`.
Charon is in recording mode, so the merge is performed by a person and charon observes it.

## An optional step is an offer, run 1

The chain ends at the workflow stage and the promotion is offered rather than waited on.

## An optional step is an offer, run 2

The offer this one raises is the one that gets overtaken.

## An optional step is an offer, run 3

This one is taken first, which is what leaves run 2 behind.

## An optional step is an offer, run 4

This one is left behind on purpose.

## An optional step is an offer, run 5

This one goes further, so run 4 must be refused.
