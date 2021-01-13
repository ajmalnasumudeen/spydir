#!/usr/bin/env python
import time
import requests
import re, time, sys

import urllib.parse as urlparse
from bs4 import BeautifulSoup
 
 
class Scanner:
    def __init__(self, url, ignore_links):
        self.session = requests.Session()
        self.target_url = url
        self.target_links = []
        self.ignored_links = ignore_links
 
    def links_extractor(self, url):
        response = self.session.get(url)
        return re.findall('(?:href=")(.*?)"', response.content.decode())
 
    def crawl(self, url=None):
        if url == None:
            url = self.target_url
        href_links = self.links_extractor(url)
        for link in href_links:
            link = urlparse.urljoin(url, link)
 
            if "#" in link:
                link = link.split("#")[0]
 
            if self.target_url in link and link not in self.target_links and link not in self.ignored_links:
                self.target_links.append(link)
                print(link)
                self.crawl(link)
 
    def extract_forms(self, url):
        response = self.session.get(url)
        parsed_html = BeautifulSoup(response.content, features="html.parser")
        return parsed_html.findAll("form")
 
    def submit_form(self, form, value, url):
        action = form.get("action")
        post_url = urlparse.urljoin(url, action)
        method = form.get("method")
 
        inputs_list = form.findAll("input")
        post_data = {}
        for input in inputs_list:
            input_name = input.get("name")
            input_type = input.get("type")
            input_value = input.get("value")
            if input_type == "text":
                input_value = value
 
            post_data[input_name] = input_value
        if method == "post":
            return self.session.post(post_url, data=post_data)
        return self.session.get(post_url, params=post_data)
 
    def run(self):
        print("\n [+] Testing Initialized \n")
        for link in self.target_links:
            forms = self.extract_forms(link)
            
            for form in forms:
                print("[+] Testing forms in " + link)
                xss_vulnerable = self.forms_xss(form, link)
                if xss_vulnerable:
                    print("\n\n\n[*******] XSS discovered in " + link + "in the following form\n\n\n")
                    print(form)
 
            if "=" in link:
                
                print("[+] Testing " + link)
                xss_vulnerable = self.link_xss(link)
                if xss_vulnerable:
                    print("\n\n\n[*******] XSS discovered in " + link + "\n\n\n")
 
    def link_xss(self, url):
        xss_test_script = "<sCript>alert('test')</scriPt>"
        url = url.replace("=", "=" + xss_test_script)
        response = self.session.get(url)
        return xss_test_script in response.content.decode(errors='ignore')
 
    def forms_xss(self, form, url):
        xss_test_script = "<sCript>alert('test')</scriPt>"
        response = self.submit_form(form, xss_test_script, url)
        return xss_test_script in response.content.decode(errors='ignore')