#!/usr/bin/perl -wT

use strict;
use CGI;

my $q = new CGI;
print $q->header( "text/html" );

open (MYFILE,"<data.txt");
print MYFILE "data Akhil wrote: ";
close(MYFILE);

print "Registered Succesfully:<P>";



print "These are the details that you entered:<P>";

my( $name, $value );

foreach $name ( $q->param ) {
    print "$name:";
    foreach $value ( $q->param( $name ) ) {
        print "  $value<br>";
    }
}


print("<meta http-equiv='refresh' content='2;url=../sample_login.html' />");









# #!/usr/bin/perl -wT

# use strict;
# use CGI;

# my $q = new CGI;
# print $q->header( "text/html" );


# print "Registered Succesfully:<P>";

# print "These are the details that you entered:<P>";




# my( $name, $value );

# foreach $name ( $q->param ) {
#     print "$name:";
#     foreach $value ( $q->param( $name ) ) {
#         print "  $value<br>";
#     }
# }


# print("<meta http-equiv='refresh' content='2;url=../sample_login.html' />");

