from aiogram import types

from keyboards.inline.menu import kurslar, menu_start
from  loader import dp,bot


#Biz haqimizda tugmasi uchun handler
@dp.callback_query_handler(text="about")
async def about_page(call:types.CallbackQuery):
    text="""
         Bizning o'quv markazimiz
    IT ning barcha yo'nalishlarini qamrab oladi 
    
    """
    await call.message.edit_text(text,reply_markup=menu_start,parse_mode="Markdown")

#ALOQA  tugmasi uchun hadndler
@dp.callback_query_handler(text="contact")
async def contact_page(call:types.CallbackQuery):
    text="""
    ☎️Number:12354684
    ☎️Number:46432157
      
    
    """
    await call.message.edit_text(text,reply_markup=menu_start,parse_mode="Markdown")

#Yangiliklar tugmasi uchun handler
@dp.callback_query_handler(text="news")
async def news_page(call:types.CallbackQuery):
    text="""
    Kelasi hafta bizning o'quv markazimizda backend boyicha musobaqa bo'lib otadi
    
    """
    await call.message.edit_text(text,reply_markup=menu_start,parse_mode="Markdown")

#Mavjud kurslar uchun handler
@dp.callback_query_handler(text="courses")
async def kurslar_page(call:types.CallbackQuery):
      await call.message.edit_text("Bizda mavjud kurslar",reply_markup=kurslar,parse_mode="Markdown")

#ortga
@dp.callback_query_handler(text="back")
async def ortga_page(callback:types.CallbackQuery):
    await bot.send_message(callback.from_user.id,"Asosiy menyuga qaytdik!",reply_markup=menu_start)
    await callback.message.delete()

#location
@dp.callback_query_handler(text="location")
async def manzil_page(call:types.CallbackQuery):
    text="""
    Samarqand shahar Ipoteka bank yon tarafida
    """
    await call.message.delete()
    await call.message.answer(text)
#backend
@dp.callback_query_handler(text="backend")
async def backend_page(call:types.CallbackQuery):
    text="""
    Backend kursimiz
    davomiyligi:6 oy
    """
    await call.message.delete()
    await call.message.answer(text)

#frontend
@dp.callback_query_handler(text="frontend")
async def frontend_page(call:types.CallbackQuery):
    text="""
    frontend kursimiz
    davomiyligi:6 oy
    """
    await call.message.delete()
    await call.message.answer(text)

#SMM
@dp.callback_query_handler(text="smm")
async def smm_page(call:types.CallbackQuery):
    text="""
    SMM kursimiz
    davomiyligi:2 oy
    """
    await call.message.delete()
    await call.message.answer(text)

#Grafik dizayn
@dp.callback_query_handler(text="dizayn")
async def dizayn_page(call:types.CallbackQuery):
    text="""
    Grafik dizayn kursimiz
    davomiyligi:5 oy
    """
    await call.message.delete()
    await call.message.answer(text)

#foundation
@dp.callback_query_handler(text="fount")
async def fount_page(call:types.CallbackQuery):
    text="""
    Fountdation kursimiz
    davomiyligi:2 oy
    """
    await call.message.delete()
    await call.message.answer(text)

#robototexnika
@dp.callback_query_handler(text="robot")
async def robot_page(call:types.CallbackQuery):

    text="""
    Robototexnika kursimiz
    davomiyligi:6 oy
    """
    await call.message.delete()
    await call.message.answer(text)







