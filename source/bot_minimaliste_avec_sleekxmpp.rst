Bot minimaliste avec SleekXMPP
##############################

:date: 2012-05-27 18:16:00
:tags: python, xmpp, bot, jabber
:category: python
:blog:
:template: article.html

C'est toujours rigolo de faire un bot jabber, j'ai découvert il y a peu un framework XMPP qui me semble sympathique SleekXMPP_. 

L'installation du framework c'est comme d'habitude pour ma part :

- Création d'un virtualenv :
	>>> virtualenv sleekxmpp
	>>> source sleekxmpp/bin/activate

- Installation de sleekxmpp :
	>>> easy_install sleekxmpp

Le gros plus par rapport aux autres framework que j'avais déjà testé c'est qu'il ne possède quasi pas de dépendance. Donc pour tester je me suis amusé à faire un bot tout simple :

.. code-block:: python

	import logging
	from sleekxmpp import ClientXMPP
	from sleekxmpp.exceptions import IqError, IqTimeout

	class TimeTrackBot(ClientXMPP):

		my_jid = ""

		def __init__(self, jid, password):
			ClientXMPP.__init__(self, jid, password)
			self.my_jid = jid
			self.add_event_handler("session_start", self.session_start)
			self.add_event_handler("message", self.message)

		def session_start(self, event):
			self.send_presence()
			self.get_roster()

		def message(self, msg):
			if msg['type'] in ('chat', 'normal'):
				commande = msg['body'].split(' ')
				msg['body'] = " ".join(commande[1:])
				try:
					retour = getattr(self, "cmd_"+commande[0])(msg)
					msg.reply(retour).send() 
				except:
					self.not_found(msg)

		def not_found(self, msg):
			msg.reply('Commande introuvable.').send()

		""" 
			Commande utilisateur
		"""
		def cmd_bonjour(self, msg):
			username 	= str(msg['from']).split('@')[0]
			message 	= str(msg['body']).split("@") # Juste pour info le message ce trouve ici
			return 'Bonjour {0}.format(username)

		def autrecmd(self, msg):
			return "STUB"

	if __name__ == '__main__':
		logging.basicConfig(level=logging.DEBUG,format='%(levelname)-8s %(message)s')

		xmpp = TimeTrackBot('username@server', 'password')
		xmpp.connect()
		xmpp.process(block=True)

ça reste ultra minimaliste, mais si ça peu aider quelqu'un pour un petit bot ;).

.. _SleekXMPP: http://sleekxmpp.com