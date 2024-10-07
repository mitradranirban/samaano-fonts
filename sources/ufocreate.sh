#!/bin/bash
sfd2ufo Samaano-Bold.sfd Samaano-Bold.ufo
sfd2ufo Samaano-Wide-Bold.sfd Samaano-Wide-Bold.ufo
sfd2ufo Samaano-Wide-Thin.sfd Samaano-Wide-Thin.ufo
sfd2ufo Samaano-Thin.sfd Samaano-Thin.ufo
# patch  -c Samaano*.ufo/fontinfo.plist fontlinfo.plist.patch
cp Samaano-Bold.ufo/features.fea Samaano-Thin.ufo/
cp Samaano-Bold.ufo/features.fea Samaano-Wide-Thin.ufo/
cp Samaano-Bold.ufo/features.fea Samaano-Wide-Bold.ufo/
