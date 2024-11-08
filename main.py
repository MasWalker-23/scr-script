import telebot
import os
import random
import string
import requests
import time
from gatet import Tele
from telebot import types
from datetime import datetime, timedelta

# Set up your bot token and admin ID
# Replace with your actual bot token
token = '7306965687:AAFO-pgHkI1I3_lwsenonWtpcyJC-pLVysc'
admin_id = '5696299308'# Replace with your actual admin user ID
bot = telebot.TeleBot(token, parse_mode="HTML")

# Store redeem codes and user redeem status
redeem_codes = {}
user_redeemed_status = {}  # Track redeem status by user ID

# Load redeemed users from file


def load_redeemed_users():
    if os.path.exists('users.txt'):
        with open('users.txt', 'r') as file:
            for line in file:
                if line.strip() == "":
                    continue
                parts = line.strip().split(',')
                if len(parts) == 3:
                    user_id, code, expiry_date = parts
                    user_redeemed_status[user_id] = (
                        code.strip(), expiry_date.strip())
                else:
                    print(f"Invalid line in users.txt: {line.strip()}")  # Log invalid lines
    else:
        with open('users.txt', 'w') as file:
            pass  # Create file if it doesn't exist

# Save redeemed users to file


def save_redeemed_user(user_id, code, expiry_date):
    with open('users.txt', 'a') as file:
        file.write(f"{user_id},{code},{expiry_date}\n")

# Function to generate random redeem codes with a prefix


def generate_redeem_code(prefix='', length=10):
    characters = string.ascii_letters + string.digits
    random_code = ''.join(random.choice(characters) for _ in range(length))
    return f"{prefix}{random_code}"  # Return code with the prefix

# Function to generate expiration date for a code


def get_expiration_date(days_valid=7):
    return (datetime.now() + timedelta(days=days_valid)).strftime("%Y-%m-%d %H:%M:%S")


load_redeemed_users()  # Load existing redeemed users


@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Welcome! Please provide a redeem code to access the bot features.")


@bot.message_handler(commands=["code"])
def generate_code(message):
    if str(message.chat.id) != admin_id:
        bot.reply_to(
            message, "You do not have permission to use this command.")
        return

    try:
        # Get the number of days for the validity period and the prefix from the message
        parts = message.text.split()
        days_valid = int(parts[1])
        # Use an empty string if no prefix is provided
        prefix = parts[2] if len(parts) > 2 else ''
    except (IndexError, ValueError):
        bot.reply_to(message, "Usage: /generate_code <days> [prefix]")
        return

    new_code = generate_redeem_code(prefix)  # Generate code with the prefix
    # Set expiration date for the new code
    expiration_date = get_expiration_date(days_valid)
    # Store the code with its expiration date
    redeem_codes[new_code] = expiration_date
    bot.reply_to(message, f"New redeem code generated: {new_code} (Expires on: {expiration_date})")
    print(f"Generated code: {new_code} (Expires on: {expiration_date})")


@bot.message_handler(commands=["redeem"])
def redeem_code(message):
    if len(message.text.split()) != 2:
        bot.reply_to(message, "Usage: /redeem <code>")
        return

    code = message.text.split()[1]
    current_datetime = datetime.now()

    # Check if the code exists and is not expired
    if code in redeem_codes:
        expiration_date = datetime.strptime(
            redeem_codes[code], "%Y-%m-%d %H:%M:%S")
        if current_datetime <= expiration_date:  # If not expired
            user_redeemed_status[str(message.chat.id)] = (
                code, redeem_codes[code])  # Store the code and expiration
            save_redeemed_user(message.chat.id, code,
                               redeem_codes[code])  # Save to file
            bot.reply_to(
                message, "Code redeemed successfully! You can now use the bot.")
        else:
            bot.reply_to(
                message, "The code you entered has expired. Please try a new one.")
    else:
        bot.reply_to(
            message, "Invalid or already redeemed code. Please try again.")




@bot.message_handler(content_types=["document"])
def main(message):
    # Check if the user is an admin or has redeemed a valid code before allowing them to use the bot
    user_id_str = str(message.chat.id)
    if user_id_str != admin_id:
        # Check if the user has a redeemed code and if it is still valid
        if user_id_str not in user_redeemed_status:
            bot.reply_to(
                message, "You must redeem a valid code before using this feature.")
            return
        else:
            code, expiry_date = user_redeemed_status[user_id_str]
            current_date = datetime.now().strftime("%Y-%m-%d")
            if current_date > expiry_date:  # Check if the code is expired
                bot.reply_to(
                    message, "Your code has expired. Please redeem a new code to continue using the bot.")
                return
            dd = 0
        live = 0
        ch = 0
        ko = (bot.reply_to(message, "Checking Your Cards...⌛").message_id)
        ee = bot.download_file(bot.get_file(
            message.document.file_id).file_path)
        with open("combo.txt", "wb") as w:
            w.write(ee)
        try:
            with open("combo.txt", 'r') as file:
                lino = file.readlines()
                total = len(lino)
                for cc in lino:
                    current_dir = os.getcwd()
                    for filename in os.listdir(current_dir):
                        if filename.endswith(".stop"):
                            bot.edit_message_text(
                                chat_id=message.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @maswalker23')
                            os.remove('stop.stop')
                            return
                    try:
                        data = requests.get(
                            'https://lookup.binlist.net/'+cc[:6]).json()

                    except:
                        pass
                    try:
                        bank = (data['bank']['name'])
                    except:
                        bank = ('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
                    try:
                        emj = (data['country']['emoji'])
                    except:
                        emj = ('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
                    try:
                        cn = (data['country']['name'])
                    except:
                        cn = ('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
                    try:
                        dicr = (data['scheme'])
                    except:
                        dicr = ('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
                    try:
                        typ = (data['type'])
                    except:
                        typ = ('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
                    try:
                        url = (data['bank']['url'])
                    except:
                        url = ('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')

                    try:
                        last = str(Tele(cc))
                    except Exception as e:
                        print(e)
                        last = "ERROR"
                    if 'risk' in last:
                        last = 'declined'
                    elif 'Duplicate' in last:
                        last = 'Approved'
                    mes = types.InlineKeyboardMarkup(row_width=1)
                    cm1 = types.InlineKeyboardButton(
                        f"• {cc} •", callback_data='u8')
                    status = types.InlineKeyboardButton(
                        f"• 𝗦𝗧𝗔𝗧𝗨𝗦 ➜ {last} •", callback_data='u8')
                    cm3 = types.InlineKeyboardButton(
                        f"• 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 🟢➜ [ {live} ] •", callback_data='x')
                    cm4 = types.InlineKeyboardButton(
                        f"• 𝗗𝗘𝗖𝗟𝗜𝗡𝗘𝗗 🔴 ➜ [ {dd} ] •", callback_data='x')
                    cm5 = types.InlineKeyboardButton(
                        f"• 𝗧𝗢𝗧𝗔𝗟  ➜ [ {total} ] •", callback_data='x')
                    stop = types.InlineKeyboardButton(
                        f"[ 𝐒𝐓𝐎𝐏 ]", callback_data='stop')
                    mes.add(cm1, status, cm3, cm4, cm5, stop)
                    bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''Wait for processing 
𝒃𝒚 ➜ @maswalker23 ''', reply_markup=mes)
                    msg = f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc.strip()}
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 🔥
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝘾𝙑𝙑 𝘾𝙃𝘼𝙍𝙂𝙀𝘿 $1
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝙎𝙏𝙍𝙄𝙋𝙀 𝘼𝙐𝙏𝙃
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ}
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj}
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @maswalker23
◆𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
                    print(last)
                    if 'Thank you.' in last:
                        live += 1
                        bot.reply_to(message, msg)
                    elif 'security code is incorrect' in last or 'security code is invalid' in last:
                        msg = f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc.strip()}
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 🟡
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝘾𝘾𝙉 𝙇𝙄𝙑𝙀
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝙎𝙏𝙍𝙄𝙋𝙀 𝘼𝙐𝙏𝙃
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ}
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj}
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @maswalker23
◆𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
                        live += 1
                        bot.reply_to(message, msg)
                    elif 'insufficient funds' in last:
                        msg = f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc.strip()}
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 🟢
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝐈𝐧𝐬𝐮𝐟𝐟𝐢𝐜𝐢𝐞𝐧𝐭 𝐟𝐮𝐧𝐝𝐬
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝙎𝙏𝙍𝙄𝙋𝙀 𝘼𝙐𝙏𝙃
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ}
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj}
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @maswalker23
◆𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
                        live += 1
                        bot.reply_to(message, msg)
                    elif 'Verifying strong customer authentication. Please wait...' in last:
                        msg = f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc.strip()}
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 🟡
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝟑𝐃 𝐜𝐚𝐫𝐝
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝙎𝙏𝙍𝙄𝙋𝙀 𝘼𝙐𝙏𝙃
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ}
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj}
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @maswalker23
◆𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
                        live += 1
                        bot.reply_to(message, msg)
                    else:
                        dd += 1
                        time.sleep(1)
        except Exception as e:
            print(e)
        video_url = f'https://t.me/tesstt23/4'
        bot.send_video(chat_id=message.chat.id,
                       video=video_url, caption='Thank you ♥️')

        bot.edit_message_text(chat_id=message.chat.id, message_id=ko,
                              text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @maswalker23')


@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
    with open("stop.stop", "w") as file:
        pass


print("Starting ....")
bot.polling()
