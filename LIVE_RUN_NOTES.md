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

## An optional step is an offer, run 6

The hand-over chooses the step, so no offer is ever raised.

## The ancestry question

A live run of the question an extension asks core about what contains what.

Somebody else's later change.
Second live run: a commit that does not exist yet.
A commit nobody has pushed yet.
Third live run: an answer about other commits.
Fourth live run: the subject moves.

## A run with no release server (2026-08-18)

The release server this run reads is a stand-in serving what the real one
answers, on loopback, from a file. Nothing outward reaches anything.

The containment question is answered from a real mirror of a real repository.

A later commit on develop, carrying whatever came before it.

A write recorded and then answered with an error is the case the receipt exists for.

The receipt read first is what makes a lost answer safe.

Live run: a step somebody chose under confirmation

Live run: a target a deny pattern catches

A change that is later overtaken

A change that overtakes the first

A change the source never carries
