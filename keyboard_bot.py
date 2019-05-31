import telebot

def menu():

    markup = telebot.types.ReplyKeyboardMarkup(True,False)
    m_btn_table_cl = telebot.types.KeyboardButton('Table CL')
    m_btn_table_pl = telebot.types.KeyboardButton('Table PL')
    m_btn_table_pd = telebot.types.KeyboardButton('Table PD')
    m_btn_table_match = telebot.types.KeyboardButton('Matches')
    m_btn_table_hist = telebot.types.KeyboardButton('History')
    markup.add(m_btn_table_cl,m_btn_table_pl,m_btn_table_pd)
    markup.add(m_btn_table_match)
    markup.add(m_btn_table_hist)
    return markup

def menu_group():

	markup = telebot.types.ReplyKeyboardMarkup(True,False)
	m_btn_cansel = telebot.types.KeyboardButton('Back✖️')
	markup.add(m_btn_cansel)
	return markup
