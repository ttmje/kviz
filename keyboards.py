from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
add_word_btn1 = InlineKeyboardButton('Да', callback_data='Да')
add_word_btn2 = InlineKeyboardButton('Нет', callback_data='Нет')
inline_kb1 = InlineKeyboardMarkup(row_width=2).row(add_word_btn1, add_word_btn2)
