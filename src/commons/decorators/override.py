#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import TypeVar
from types import FunctionType

"""
@author: https://github.com/mkorpela/overrides
"""
_WrappedMethod = TypeVar("_WrappedMethod", bound = FunctionType)

def Override(interfaceClass):
  """
  """
    
  def overrider(method: _WrappedMethod) -> _WrappedMethod:
    """
    """

    assert(method.__name__ in dir(interfaceClass))
    
    return method
  
  return overrider
