#Three hosts connected to one switch
############################################
from mininet.topo import Topo

class MyTopo( Topo ):
	"Simple Topology."
	def _init_( self ):
		"create custom topo."
		#initialize topology
		Topo._init_( self )
		
		#add hosts and switch
		host_1 = self.addHost( "h1" )
		host_2 = self.addHost( "h2" )
		host_3 = self.addHost( "h3" )
		switch = self.addSwitch( "s1" )

		#add links
		self.addLink( host_1, switch )
		self.addLink( host_2, switch )
		self.addLink( host_3, switch )
	
	topos = { 'mytopo': ( lambda: MyTopo() ) }

