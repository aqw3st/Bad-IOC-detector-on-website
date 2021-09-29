import re

def find_CVE(text_data):
	cve_pattern = 'CVE-\d{4}-\d{4,7}' 
	cve_find = re.findall(cve_pattern, text_data)
	return cve_find 

def find_APT(text_data):
	apt_pattern = 'APT[0-9]{1,2}'
	apt_find = re.findall(apt_pattern, text_data)
	return apt_find 	

def find_HASH(text_data):
	hash_pattern = '[a-fA-F\d]{32}'
	hash_find = re.findall(hash_pattern, text_data)
	return hash_find

def find_URL(text_data):
	url_pattern = '''(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?'''
	url_find = re.findall(url_pattern, text_data)
	return url_find

def find_IP(text_data):
	ip_pattern = '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|\[.])(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|\[.])(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|\[.])(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
	ip_find = re.findall(ip_pattern, text_data)
	ips = []
	# convert list to string by element
	for i in range(len(ip_find)):
		ips.append(''.join(ip_find[i]))	
	return ips

def find_DOMAIN(text_data):
	domain_pattern = '^(((?!-))(xn--)?[a-z0-9][a-z0-9-_]{0,61}[a-z0-9]{0,1}\.)?(x--)?([a-z0-9\-]{1,61}|[a-z0-9-]{1,30}\.[a-z]{2,})\.?$'
	domain_find = re.findall(domain_pattern, text_data)
	return domain_find

def find_MALWARE(doc):	
	malwares = []
	for ents in doc.ents:
		if ents.label_ == 'Malware':
		    malwares.append(ents)
	return malwares


def highlight_html(cve_find, hash_find, malwares, domain_find, ips, apt_find, text_data):
	
	#highlights iocs on html page
	mark = '<mark>{}</mark>'
	for cve in cve_find:
		if cve in text_data:
		    text_data = text_data.replace(cve,mark.format(cve))

	for hash in hash_find:
		if hash in text_data:
		    text_data = text_data.replace(hash,mark.format(hash))

	for malware in malwares:
		if str(malware) in text_data:
		    text_data = text_data.replace(str(malware),mark.format(str(malware)))
		
	for domain in domain_find:
		if domain in text_data:
			text_data = text_data.replace(domain,mark.format(domain))

	for ip in ips:
		if ip in text_data:
			text_data = text_data.replace(ip,mark.format(ip))

	for apt in apt_find:
		if apt in text_data:
			text_data = text_data.replace(apt,mark.format(apt))

	return text_data