from telebot import types
import telebot.types
from telebot import TeleBot
    
bot = TeleBot('5750665963:AAEJP12QWonHXi0asBFMTZjlv4cLB8ezipM')

kb = types.InlineKeyboardMarkup(row_width=4)
butn1 = types.InlineKeyboardButton(text = 'Простые числа', callback_data='simple')
butn2 = types.InlineKeyboardButton(text = 'Комплексные числа', callback_data='komplex')
kb.add(butn1,butn2)

def find_sign_simple(txt):
   return ''.join([char for char in "+-/*" if char in txt])

def komplex(txt):
    res = None
    lst = text.split()
    if lst[1] == '-':
        res = complex(lst[0]) - complex(lst[2])
        return str(res)
    elif lst[1] == '+':
        res = complex(lst[0]) + complex(lst[2])
        return str(res)
    elif lst[1] == '/':
        res = complex(lst[0]) / complex(lst[2])
        return str(res)
    elif lst[1] == '*':
        res = complex(lst[0]) * complex(lst[2])
        return str(res)    


@bot.message_handler(commands=['start'])
def but_ts(msg):
    bot.send_message(msg.chat.id, f'Привет,{msg.from_user.first_name}! Это бот калькулятор. Нажмите нужную кнопку.'
        , reply_markup = kb)
    
@bot.callback_query_handler(func= lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'simple':
            bot.send_message(call.message.chat.id, 'Введите два числа и действие между ними, например: 15 - 8')

            @bot.message_handler(content_types=['text'])
            def searching(msg: telebot.types.Message):
                res = 0
                if len(find_sign_simple(msg.text)) == 1:
                    if find_sign_simple(msg.text) == "-":
                        lst = msg.text.split("-")
                        res = float(lst[0]) - float(lst[1])
                        bot.send_message(call.message.chat.id, res)
                    
                    if find_sign_simple(msg.text) == "+":
                        lst = msg.text.split("+")
                        res = float(lst[0]) - float(lst[1])
                        bot.send_message(call.message.chat.id, res)
                        
                    if find_sign_simple(msg.text) == "*":
                        lst = msg.text.split("*")
                        res = float(lst[0]) * float(lst[1])
                        bot.send_message(call.message.chat.id, res)
                    
                    if find_sign_simple(msg.text) == "/":
                        lst = msg.text.split("/")
                        res = float(lst[0]) - float(lst[1])
                        bot.send_message(call.message.chat.id, res)

        if call.data == 'komplex':
            bot.send_message(call.message.chat.id, 'Введите два комплексных числа и действие между ними, например: 15+8j - 17+2j')

            @bot.message_handler(content_types=['text'])
            def searching(msg: telebot.types.Message):
                txt = msg.text
                res = None
                lst = txt.split()
                if lst[1] == '-':
                    res = complex(lst[0]) - complex(lst[2])
                    bot.send_message(call.message.chat.id, res)
                elif lst[1] == '+':
                    res = complex(lst[0]) + complex(lst[2])
                    bot.send_message(call.message.chat.id, res)
                elif lst[1] == '/':
                    res = complex(lst[0]) / complex(lst[2])
                    bot.send_message(call.message.chat.id, res)
                elif lst[1] == '*':
                    res = complex(lst[0]) * complex(lst[2])             
                    bot.send_message(call.message.chat.id, res)
def simple_calc(msg: telebot.types.Message):
        bot.send_message(chat_id=msg.from_user.id, text=calc(msg.text))
        

bot.polling()