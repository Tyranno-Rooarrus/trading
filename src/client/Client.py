#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

    print ("Test")
    