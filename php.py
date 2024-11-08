import requests

cookies = {
    '_ga_8YVML7ZXLV': 'GS1.1.1728771017.1.0.1728771017.0.0.0',
    '_ga': 'GA1.1.955541208.1728771018',
    '__stripe_mid': 'a760aad9-49eb-4694-b601-500fb05d05f8251c68',
    '__stripe_sid': '371d155d-6242-4b73-81ee-eedf7e8b7858ec36a6',
}

headers = {
    'authority': 'remoteservices.uk',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_ga_8YVML7ZXLV=GS1.1.1728771017.1.0.1728771017.0.0.0; _ga=GA1.1.955541208.1728771018; __stripe_mid=a760aad9-49eb-4694-b601-500fb05d05f8251c68; __stripe_sid=371d155d-6242-4b73-81ee-eedf7e8b7858ec36a6',
    'origin': 'https://remoteservices.uk',
    'referer': 'https://remoteservices.uk/method-statement-2-2-2-2/',
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
    't': '1728771099355',
}

data = {
    'data': '__fluent_form_embded_post_id=3636&_fluentform_41_fluentformnonce=72835207ce&_wp_http_referer=%2Fmethod-statement-2-2-2-2%2F&names%5Bfirst_name%5D=Mas&names%5Blast_name%5D=Walker&email=maswalkerus01%40gmail.com&password=maswalker2002&gdpr-agreement=on&payment_input=15&item-quantity=1&payment_method=stripe&__stripe_payment_method_id=pm_1Q9DXCBnUoXblJsZY9JTbwtK',
    'action': 'fluentform_submit',
    'form_id': '41',
}

response = requests.post(
    'https://remoteservices.uk/wp-admin/admin-ajax.php',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)

import requests

headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

data = 'type=card&card[number]=4427550219459113&card[cvc]=185&card[exp_month]=07&card[exp_year]=28&guid=7399b302-2138-4af2-ace0-1e1ad1d628f72141ad&muid=a760aad9-49eb-4694-b601-500fb05d05f8251c68&sid=371d155d-6242-4b73-81ee-eedf7e8b7858ec36a6&pasted_fields=number&payment_user_agent=stripe.js%2F89bde95bba%3B+stripe-js-v3%2F89bde95bba%3B+card-element&referrer=https%3A%2F%2Fremoteservices.uk&time_on_page=84774&key=pk_live_51OSc6MBnUoXblJsZzPe64PJ6kULncEuMZ2F36JcdMaW0Wp8rvRGy75zFche1N53Rd1qAkWh0sCrzxtvGgc9QbVA600Cc0eKwTW&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoickRYZGRYWmVua2VyaE1oc2g2NXE2TzNEY3U3UEVCMFF4TUZZVjlnOFhsNVcyRmNxQ3E2SmhJSmR1UzFVcUVTZTJjV0hMNmladVdyZVI4YzlTV3cyM2xhTTVlaklpMm9rZ1Y1bXEyZ3ZrY1VRN2kxa0JORVBsZE00RUJOSUR1cXFzcDE5anhTOUpZZXBNbjhweGpOeGZENlYvem8zdUVRMkY0TW1TMkFMckZzUzU2MkR5SzlCMkhXdVNSaXJCL256TnhjUWFFZWtsSWRpaTNwMUkrNlE4YmxheE1JVU81ZnlYOTJnUFduY29KdHV6R0sxdFlaakt4cWg2K2xOVFZUQ0lLd2J6NkhzTVJxMzZkN0x2ZkpURDhXMnZMSkRseXV0UldIL0lTWDdaSDJIUG5LSmozWTVTM05RbFlsNGs5T28yV3lXNjZFRXpvQWVkNDU5WG1ROUN0UEVQOXRseWtmdHhtRVkwdVMwYnVUMjF4YU9DZ09mdnQ4WklkTmVlQ0UzY2N1ek9OYTg0QjlqUU04dDVUSzgvWWZQdDYrY3d2akg3RVVPVzA5c0R1aGJ6cWNtMlIvL0lqdzVvZUJFbVlWUjZRV09KbVp6ZlVPbXd5SWhZNjQxRnd5U2NRMk9valNHRiswcFgwM20wWkQ4WGdLdGpodk42Y0RFVTFKU3pFejJ6b21YZ0xiOGdIMEovazN4UUl6WjhSS2NoYUVST1pySFlWUkxUU3dQN29LNkg4bUk2b3ZMSk1mMUtsUThqKzBnMVFoalFGMjhiRTVlNVNzZUQ3bFBJMVE4NnNHYnVmclhhRVpjQjVBNGp6dTVTakNxREk2UWJETU9VU0s2ekpYKzFJQU03aGIrVlhBWHg0L1RVRUg1eFR0aEgraXhEdng5NW5weC9oNjNnT1gvN3g4ckszN09KOEJyS1N1ZU1yUk93RTdOdEJmWkgwRjZPYUZpcmN2eHFhZnduUzFKYjFCYU9DSHRraVBJZVpMRVVZaytzd01pbCtxWGJxb01tZjVpTTNLZ1E1RlN3WnlWdHlNMW1ocjV2dkM3a3g3MmNvYUVDbXNqb3hUcWJtdnEvTE44V01wWURreTROeW5xNnpmQ1VNWS9KSXV1cm1BZW9CQ1UvUGxuY3QxeFpMZUFpdHEzS05rT2VLR0wyUkNLblJXSUVMRkhlM3FOUjFSY3Y0dHVqUnR2TFB1QWpOUDZVQU0vOHBaREh0TVhDanZ6U0NBYTBQWnUvU0NJd1o0SHIwKzgreVdUbXpvTmJyaUJlNE9qWnJTMVBlYnBuaTdBVFF5QWV5K0d0WWdyQ1lPaWRjSXFYRXlONHlvZTV5d2VGYU9BY1UyYlh2M3VwYklUR2dsdmdPVUNUcm56bHFCbUVHQ2kxeS9mVHQ0N1dvTU9odXFoQmdUMmhzcSszSjBITENEVlpMRFp0akFIYXF6SEUwb0lqbUU4cmp3T2E2TnVydDlWSUFrRkF2eTJJbWJ4dXBpa3hqSlF1TUlXc0d2U0hiS2xNM3l2M29YUTExYnJkeXF6NzhyQlBDRStKaEFndERlK1E3b3FqampKVjZwKzlLRjNMQ21DSGcrYTZUaGx1ZmJIN29DWnBPRFBqMTIvNUl3SWtQMk5wMytOTkVoaHNuZDdmaklCZ1c0TldNb1NoaEY0VmxWOWxRRGppaVBQREtLV1ltaytBTTYwcFA1MjVneGhMVXU2UFNrRzE5WHcybm1FZDlzdWJYWU13bDh5NWdPeW9OUnJjZi9OQkdYUkVNNG1qSGZXaGtOTnlKSnRsVDZyNldxeEYzQWowSDJ5TXByVzMvQldCdmtlWDd5Vy9jVkxCRnRVeG1Yb040N0hIT2hxbGlScG9UUUJjZVRtM2wzODl5OG1tMCtRN3IxT3JwT1NkSDg3eGJMNCt1UGRPVTlXbVZENVZTMk5uWDJzQTZHVW9oN0NnRVAzZmRvYVlBeGlEY3Vrckd1VFlhYjRHVlE3ZTdhWXhieHo3bllIYlFnUXVWQzZ6QWd3STdIQkdvcmdnQ1AySHE2azFRK2NmYUVBSlBHNnplLy9GblFWVGtHS01QVjVEWkVlTU1EMmF4MHc3UHlubHBYeVZGK2s3cWpWcTdWQ01RYUlHMjJDSmxQUStJdVZSc3F1ZDYyTTVSNUxxSG5pUmNDMWtTNzJtUXF1UnhLcThicGhZV0VYWG5YaG0yb1JZQkJ2blBYdE9QcXQ2am5vTWViNkxQY296MHdzYk4vTllVVDdMMmxtVnZwWEgwdXlidXZ0VEVhNTNKazRHRm1tdkdJZm9TYWMwdnVnOG1SdHprOEo2eWRnd2UxV0VxcUFKTUJqT1k4RDZoRERDNVRzM0gwNjVxMnhYTHhvS213TjRpbmJjakxaRzN3aHordjVaaTAxVGg4K2VTdW12L1ZFN25naHBqQ29NU3NCb3NJTGZlWVF0WXNBOERPVHRMZGtZc0M1U0hUcS9pYkRZdDRFWmZHYlhrSG5tbnpYYnhFTFFTUXBLdkRucVcxTEllei81MlMvYlNxTHBFWHpZM1d3NlFBQkZJVTZRUjZRL3ZYbXRQcldIZWNhall5WHdFSzdCeUZzSFhEOGlIT1pmdEh2dmhNQWxsdFdjZTVSZzdKZG1POHN5OTNXMEU2Um1jaWdaMjVvQWhpVVNtUTNEYTIxKzV4dHMvdzFFUXhyeEdwcXNHR0p1WmNFYzFwTGdFZmkwNWk4dFBDS2k0RlRvaVBHWlZpblhJcFpoUUhZc0dsdktTVW1MNHlTbjFLRWZJNU9QWVhBYTBtVEkvOWc2L2NZN0cxTW5YRmYrWXBCdXdCRiIsImV4cCI6MTcyODc3MTE1MSwic2hhcmRfaWQiOjMzOTUxMDMwMywia3IiOiJiNjhkYTIyIiwicGQiOjAsImNkYXRhIjoiaUgvUWUza2wrdFJIVkhZdXM1cVA1UWpoNzlMM210RUZENy80bnFQQzBTTi9DdHlyR0JiSGpJTDRtbzdSQ25ReVZjaXJJSitmMGFIdW5BZXBiQ1J6bXg2enpVc040V09VcHcvUnlVOSs0c0RpQzRwLytzbWJEWjdUdVdLUEgrbGJncWtlVEpjOTMvMHQzMlk5dVF4ZjRtWVBRdDZXQmdETmdvNW0wV3c5NW1EQ3NIRCtjTnBsb1loY3JzQmlqYUNHTHBGeUpLUkRIaE1HUXRvdCJ9.czDNE0mg2ZuqRAcSgR11H9NOAkc22lZwb2DCiKZrVtk'

response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)