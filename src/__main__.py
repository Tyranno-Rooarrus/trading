#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.client.Client import Client


if __name__ == '__main__':
  client: Client = Client()
  client.start()