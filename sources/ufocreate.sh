#!/bin/bash
sfd2ufo Samaano-Bold.sfd Samaano-Bold.ufo
sfd2ufo Samaano-Wide-Bold.sfd Samaano-Wide-Bold.ufo
sfd2ufo Samaano-Wide-Thin.sfd Samaano-Wide-Thin.ufo
sfd2ufo Samaano-Thin.sfd Samaano-Thin.ufo 
cp Samaano-Bold.ufo/features.fea Samaano-Thin.ufo/
cp Samaano-Bold.ufo/features.fea Samaano-Wide-Thin.ufo/
cp Samaano-Bold.ufo/features.fea Samaano-Wide-Bold.ufo/
ufonormalizer -a Samaano-Bold.ufo
ufonormalizer -a Samaano-Wide-Bold.ufo
ufonormalizer -a Samaano-Thin.ufo
ufonormalizer -a Samaano-Wide-Thin.ufo
