#!/usr/bin/perl -w

use IO::Socket;
use strict;

my($sock, $msg, $port, $ipaddr, $hishost, $MAXLEN, $PORTNO, $TIMEOUT);

$MAXLEN  = 1024;
$PORTNO  = 53008;
$TIMEOUT = 5;

if ($#ARGV+1 > 1)
{
  $ipaddr = $ARGV[0];
  $msg = $ARGV[1];
}
elsif ($#ARGV+1 == 1)
{
  $ipaddr = '192.168.0.99';
  $msg = $ARGV[0];
}
else
{
  print "usage: ./client.pl [IP ADDRESS OF BBSB CONTROLLER] <message>\n";
  exit;
}

$sock = IO::Socket::INET->new(Proto => 'udp', PeerPort => $PORTNO, PeerAddr => $ipaddr) or die "Creating socket: $!\n";

$sock->send($msg) or die "send: $!";
