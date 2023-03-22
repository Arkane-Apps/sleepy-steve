from twisted.internet import reactor
from quarry.net.client import ClientFactory, ClientProtocol


class PingProtocol(ClientProtocol):
    def status_response(self, data):
        for k, v in sorted(data.items()):
            if k != "favicon":
                print("%s --> %s" % (k, v))

        reactor.stop()


class PingFactory(ClientFactory):
    protocol = PingProtocol
    protocol_mode_next = "status"


factory = PingFactory()
factory.connect("SERVER_URL", 25565)
reactor.run(factory)
