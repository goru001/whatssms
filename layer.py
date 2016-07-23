from yowsup.layers.interface                           import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities  import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities      import OutgoingAckProtocolEntity
# For sms
import urllib2
import cookielib
import imaplib
import datetime
import re
#For converting unicode strings to ascii 
import unicodedata

class EchoLayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        #send receipt otherwise we keep receiving the same message over and over

        if True:
            receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom(), 'read', messageProtocolEntity.getParticipant())
            sender = messageProtocolEntity.getFrom()
            sender = str(sender)
            stype = 0   #Sender is of individual type 
            reply = 'UnImportant'
			fo = open("GROUP_NAME.txt","r")
			GROUP_NAME= fo.read()
			fo.close()
			fo = open("KEYWORD.txt","r")
			KEYWORD= fo.read()
			fo.close()
			fo = open("WAY2SMS_LOGIN.txt","r")
			WAY2SMS_LOGIN= fo.read()
			fo.close()
			fo = open("WAY2SMS_PASSWORD.txt","r")
			WAY2SMS_PASSWORD= fo.read()
			fo.close()
            groupName = GROUP_NAME
            keyword = KEYWORD
            for i in xrange(0,len(sender)):
				if sender[i] == '@':
					if i>12:
						stype = 1	#sender is of group type
					break
            #Sending sms to people
            if stype==1:
				msg = messageProtocolEntity.getBody()
				message = unicodedata.normalize('NFKD', msg).encode('ascii','ignore')
				msg1 = message
				msg1 = msg1.strip()
				msg1 = msg1.lower()
				keyword = keyword.lower()
				index = msg1.find(keyword,0,17)
				#preparing the message to be sent
				msg = re.findall(r"[\w'.,?\\%@!^/$#&*)(]+", message)
				res =""
				i = 1
				if index != -1:
					while i<len(msg):
						if (len(res)+len(msg[i])) <= 115:
							res = res+msg[i]+" "
							i = i+1
						else:		#message is sent in this else
							tosend = res.strip()+"..."
							fo = open("PHONE.txt","r")
							content = fo.read()
							y = content.strip().split(",")
							allnumbers = y[1:]
							for number in allnumbers:
								username = WAY2SMS_LOGIN 
								passwd = WAY2SMS_PASSWORD
								message = '%s'%(groupName)+'\n'+tosend
								url ='http://site24.way2sms.com/Login1.action?'
								data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
								cj= cookielib.CookieJar()
								opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
								opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
								usock = opener.open(url, data)
								jession_id =str(cj).split('~')[1].split(' ')[0]
								send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
								send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+str(number)+'&message='+message+'&msgLen=136'
								opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
								sms_sent_page = opener.open(send_sms_url,send_sms_data)
							res = "..."+msg[i].strip()+" "
							i = i+1
					if res:
						tosend = res
						fo = open("PHONE.txt","r")
						content = fo.read()
						y = content.strip().split(",")
						allnumbers = y[1:]
						for number in allnumbers:
							username = WAY2SMS_LOGIN 
							passwd = WAY2SMS_PASSWORD
							message = '%s'%(groupName)+'\n'+tosend
							url ='http://site24.way2sms.com/Login1.action?'
							data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
							cj= cookielib.CookieJar()
							opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
							opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
							usock = opener.open(url, data)
							jession_id =str(cj).split('~')[1].split(' ')[0]
							send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
							send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+str(number)+'&message='+message+'&msgLen=136'
							opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
							sms_sent_page = opener.open(send_sms_url,send_sms_data)
					reply = 'Thankyou :)'
            #SMS has been sent to people
            if stype==0:
				msg = messageProtocolEntity.getBody()
				msg = unicodedata.normalize('NFKD', msg).encode('ascii','ignore')
				msg = msg.strip()
				msg = msg.lower()
				index = msg.find('add',0,3)
				if index==-1:
					index = 5;
					reply = "I can't understand you. :( . Please ask gaurav to do something."
				if index==0:
					if len(msg) > 14 or len(msg) < 14 or msg[3]!=' ':
						reply = 'Invalid Format.Please try again.\n Valid Format is:\n\nadd 9569252871 \n\n(where 9569252871 will be replaced by the number you want to add)'
					if len(msg)==14 and msg[3]==' ':
						number = msg[4:]
						isNumber = number.isdigit()
						if isNumber==True:
							fo = open("PHONE.txt","r")
							content = fo.read()
							y = content.strip().split(",")
							allnumbers = y[1:]
							fo.close()
							if int(number) in allnumbers:
								reply = "I've already added you! :) "
							else:
								username = WAY2SMS_LOGIN 
								passwd = WAY2SMS_PASSWORD
								message = 'You\'ve been added to receive %s messages from %s group on Whatsapp,by %s'%(keyword,groupName,sender[:12])
								url ='http://site24.way2sms.com/Login1.action?'
								data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
								cj= cookielib.CookieJar()
								opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
								opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
								usock = opener.open(url, data)
								jession_id =str(cj).split('~')[1].split(' ')[0]
								send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
								send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+str(number)+'&message='+message+'&msgLen=136'
								opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
								sms_sent_page = opener.open(send_sms_url,send_sms_data)
								#allNumbers.append(number)#open a file to add new number at the end
								fo = open("PHONE.txt","a+")
								fo.write(","+str(number))
								fo.close()	# new number added
								reply = 'Awww!Thankyou :).I\'ll text %s all the %s messages from now on :)'%(number,keyword)
						if isNumber==False:
							reply = 'Enter a valid phone number please'
            self.toLower(receipt)
            if index != -1:
				outgoingMessageProtocolEntity = TextMessageProtocolEntity(reply,to = messageProtocolEntity.getFrom())
				self.toLower(outgoingMessageProtocolEntity)

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", entity.getType(), entity.getFrom())
        self.toLower(ack)
