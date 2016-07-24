# WhatsSMS
Get important messages from Whatsapp groups as SMS on your mobile,for free. Save yourself from scrolling down through 500 messages to find the important ones.Yay!

###Requirements
  1. Python2.7 or Python3.4

  2. Way2SMS account(www.way2sms.com)
  3. Install git
 
          $ sudo apt-get install git (For Ubuntu)    or    $ sudo dnf install git (For Fedora)
  4. Install yowsup2 by: 

          $ sudo pip install yowsup2


###QuickStart

  1.Setting up Whatsapp Account

  (a) Request for Code through sms
  
            $ yowsup-cli registration --requestcode sms --phone <YOUR-PHONE-NUMBER> --cc <country-code>
    
          Eg: $yowsup-cli registration --requestcode sms --phone 919569252871 --cc 91
  
  (b) After receiving confirmation code through sms on YOUR-PHONE-NUMBER ,
  
             $yowsup-cli registration --register xxx-xxx --phone <YOUR-PHONE-NUMBER> --cc <country-code>
              
          Eg: yowsup-cli registration --register 594-816 --phone 919569252871 --cc 91
          
You will get your LOGIN(which will be the number you entered) and PASSWORD as the output. 

Copy your password, we'll need that later!

2.Create NewDirectory whatssms (just to keep things clean) and copy the project: 

          $ mkdir ~/whatssms && cd ~/whatssms
          
          $ git clone https://github.com/goru001/whatssms.git
          
3.Configure:

          $ python start.py
          
You will be asked about :

(a). WhatsappLogin -----> YOUR-PHONE-NUMBER      

          Login-----> 919569252871

(b). WhatsappPassword -----> PASSWORD      

          Password -----> pt9idIEzfW0GP/LfGGXjpSrmxGI=

(c). Way2SMSLogin -----> WAY2SMS-LOGIN                  

          Way2SMSLogin ----->  9569252871

(d). Way2SMSPassword -----> WAY2SMS-PASSWORD            

          Way2SMSPassword -----> goru

(e). Keyword------> this-is-the-keyword-by-which-all-the-messages-in-the-group-will-be-filtered 

          Keyword------> #important

(f). groupname-----> this-is-the-group-name-to-which-you-want-to-apply-the-filter    

          groupname-----> Important Notices

          
###Usage

(a). Add YOUR-PHONE-NUMBER to the WhatsappGroup from which you want filtered messages.

(b). Now, anyone can send a whatsapp message to this number to add a Recepient to the list of recepients who want to receive filtered SMS.

i.e Anyone can Send Whatsapp Message to YOUR-PHONE-NUMBER:

            add <recepient-phone-number>        Eg: add 8965235885

And Done! recepient-phone-number will receive all the pending messages as sms which would start with the KEYWORD, whenever you'll execute:

            $ python run.py.

You have saved yours and your groupmates lot of time! Congratulations! 
 



