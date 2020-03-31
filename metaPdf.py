#!/usr/bin/python3
# Author: Mark Kaiser
# Date: 01/26/2020
# Description: takes a pdf file and extracts the metadata

import PyPDF2
import argparse
from PyPDF2 import PdfFileReader

def printMeta(fileName):
    pdfFile = PdfFileReader(open(fileName, 'rb'))
    docMinfo = pdfFile.getDocumentInfo()
    print('[*] PDF Metadata For: ' + str(fileName))
    for meta in docMinfo:
        print('[+] ' + meta + ':', docMinfo[meta])

def main():
    parser = argparse.ArgumentParser(description='Provide a pdf file to extract the metadata')
    parser.add_argument('-v', '--version', dest='ver', required=False, action='store_true', help='display version number.')
    parser.add_argument('-f', '--file', dest='file', required=False, type=str, help="provide a filename")
    args = parser.parse_args()
    if args.ver:
        print("metaPdf version 0.1")
        exit()
    fileName = args.file
    if fileName == None:
        print('Usage: python3 metaPdf.py -f file.pdf')
        exit(0)
    else:
        printMeta(fileName)
        
if __name__ == '__main__':
    main()