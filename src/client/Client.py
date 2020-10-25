#!/usr/bin/env python
# -*- coding: utf-8 -*-
import client.quickstart

from client.AbstractBaseClient import AbstractBaseClient
from commons.decorators.override import Override


"""
"""
class Client(AbstractBaseClient):
  """
  """

  def __init__(self) -> None:
    """
    """

    super().__init__()


  @Override(AbstractBaseClient)
  def start(self) -> None:
    
    self.quickstart


  #@Override(AbstractBaseClient)
  #def start1(self) -> None:

    # Python code to illustrate Sending mail from  
    # your Gmail account  
  #  import smtplib 
      
    # creates SMTP session 
  #  s = smtplib.SMTP('smtp.gmail.com', 587) 
      
    # start TLS for security 
  #  s.starttls() 
      
    # Authentication 
  #  s.login("kobstaedt.finances@gmail.com", "Trilobit#2018") 
      
    # message to be sent 
  #  message = "Message_you_need_to_send"
      
    # sending the mail 
    #s.sendmail("sender_email_id", "receiver_email_id", message) 
      
    # terminating the session 
  #  s.quit() 