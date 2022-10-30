from telebot import types
import telebot.types
from telebot import TeleBot
    
bot = TeleBot('5750665963:AAEJP12QWonHXi0asBFMTZjlv4cLB8ezipM')

@bot.message_handler(commands=['start'])
def send_start_message(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text= ('Для действий с телефонной книгой доступны следующие функции:\n'
                                                      'Чтение /read \n'
                                                      'Поиск /search \n'
                                                      'Импорт /import \n'
                                                      'Эскпорт /export\n'))

# загрузка в бот файла телефонной книги
@bot.message_handler(commands=['read'])
def read_phonebook(msg: telebot.types.Message):
    with open('phone_book.txt', 'r', encoding='utf-8'):
        bot.send_document(chat_id=msg.from_user.id, document=open('phone_book.txt', 'rb'))        

# Импорт данных
@bot.message_handler(commands=['import'])
def import_phonebook(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text= "загрузите документ")
    @bot.message_handler(content_types=['document'])
    def document_imp(msg: telebot.types.Message):
        file = bot.get_file(msg.document.file_id)
        downloaded_file = bot.download_file(file.file_path)
        with open(msg.document.file_name, 'wb') as f_out:
            f_out.write(downloaded_file)
        with open(msg.document.file_name, "r", encoding='utf-8') as f, open('phone_book.txt', "a", encoding='utf-8') as g:
                g.writelines('\n')
                for line in f:
                    if len(line) > 20:
                        g.writelines(line)
                        g.writelines('\n')
                if len(line) < 20:
                    with open(msg.document.file_name, encoding='utf-8') as k:
                        lines = k.readlines()
                    with open('phone_book.txt', "a", encoding='utf-8') as l:
                        j = 0
                        lst1 = []
                        for each in lines:
                            if not each.__contains__(','):
                                if each != '\n':
                                    lst1.append(each.replace("\n", ""))
                                    j += 1
                                    if j == 4:
                                        l.writelines(', '.join(lst1))
                                        l.writelines('\n')
                                        j = 0
                                        lst1 = []    


# экспорт данных
@bot.message_handler(commands=['export'])
def export_phonebook(msg: telebot.types.Message):
    with open('phone_book.txt', "r", encoding='utf-8') as f:
            with open('phone_book_exp.txt', "w", encoding='utf-8') as g:
                for line in f:
                    g.write(line)
    bot.send_document(chat_id=msg.from_user.id, document=open('phone_book_exp.txt', 'rb'))  
      
      
# поиск данных
@bot.message_handler(commands=['search'])
def search_data(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text= "Введите данные для поиска:")
    @bot.message_handler(content_types=['text'])
    def searching(msg: telebot.types.Message):
        search_value = msg.text

        with open('phone_book.txt','r', encoding='utf-8') as file:
            count = 0
            for line in file:
            
                if search_value in line:
                    bot.send_message(chat_id=msg.from_user.id, text= line)
                    count+=1
            if count == 0:
                bot.send_message(chat_id=msg.from_user.id, text= 'Не найдено')
    
bot.polling(none_stop=True)       