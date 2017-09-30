#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import PyPDF2

filename = input('\nFilename:')

pdfFileObj = open('oposicion.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages

pageObj = pdfReader.getPage(0)
pageObj.extractText()

