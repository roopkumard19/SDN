from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
        Switch = self.addSwitch( 's1' )
       

        # Add links
        self.addLink( leftHost, Switch )
        self.addLink( rightHost, Switch )

topos = { 'mytopo': ( lambda: MyTopo() ) }
