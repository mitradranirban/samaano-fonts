use strict;
use warnings;

# Usage: perl addfixed.pl /path/to/fontinfo.plist

my $file = shift or die "Usage: $0 /path/to/fontinfo.plist\n";

# Define the pattern to be replaced and replacement content (preserving spaces/newlines)
my $KEY = qq{  </dict>\n</plist>};
my $DATA = <<"END_XML";
<key>postscriptIsFixedPitch</key>
    <true/>
    <key>openTypeOS2Selection</key>
    <array>
    <integer>7</integer>
   </array>
  </dict>
</plist>
END_XML

# Read file content in one shot
open my $fh, '<', $file or die "Could not open $file: $!";
local $/ = undef;
my $content = <$fh>;
close $fh;

# Perform literal, multi-line replacement
$content =~ s/\Q$KEY\E/$DATA/s;

# Write updated content back to the same file
open my $ofh, '>', $file or die "Could not write $file: $!";
print $ofh $content;
close $ofh;

print "Replacement done in $file\n";

