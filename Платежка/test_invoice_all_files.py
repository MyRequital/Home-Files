# ====== Глобальные переменные, зависимости, и прочее ======
import asyncio
import os
import uuid

from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
from yookassa import Payment

from _configs.log_config import logger
from tools.delete_message import delete_message_safe
from ykassa_payments import invoices


load_dotenv()


# ====== Блок создания ОБЪЕКТА платежа ======
def create_invoice(user_id,             # Аргумент user_id, передающийся как metadata платежа
                   cost: int,           # Аргумент цены (int) товара\услуги
                   task: str,           # Аргумент номера задания по модулю
                   material_name: str   # Аргумент названия материала
                   ):

    return Payment.create({             # Метод создания ОБЪЕКТА платежа
        "amount": {                     # Стоимость
            "value": f"{cost}.00",          # Цена
            "currency": "RUB"               # Валюта
        },
        "payment_method_data": {        # Тип оплаты
            "type": "bank_card"             # Выбор типа
        },
        "confirmation": {               # "по окончанию"
            "type": "redirect",                             # Действие (редирект - пересылка)
            "return_url": "https://t.me/EroNoSekaiBot"      # Пересылка куда (то куда отправит сайт после оплаты)
        },
        'metadata': {                   # Метаданные платежа
            'user_id': user_id              # То что мы даем в метадату (user_id)
        },
        "capture": True,
        "description": f"Сборник материалов для задания {task} по {material_name}"      # Описание
    },
        str(uuid.uuid4())   # Назначение уникального ключа-платежа
    )

# ====== Блок отвечающий за создание сообщения (текстовый визуал) информации о платеже ======
account_number = os.getenv('YOOMONEY_ACCOUNT')  # Номер счета ЮMoney из переменных окружения

async def send_payment_message(callback: types.CallbackQuery, # CallbackQuery от aiogram
                               item_name: str,                   # Название товара/услуги
                               subject_to_return,            # callback для (отмены) платежа "то куда возвращаться после нажатия (отмена)"
                               cost: int = 0,                  # Цена (int) товара/услуги, по умолчанию 0
                               task: str = "",                 # Номер задания, по умолчанию пустая строка
                               material_name: str = ""):  # Название материала, по умолчанию пустая строка

    global account_number  # Глобальная переменная с номером счета ЮMoney

    user_id = callback.from_user.id  # user_id пользователя, инициировавшего callback

    task_invoice = invoices.create_invoice(user_id,  # Создание счета
                                           cost=cost,  # Передача цены
                                           task=task,  # Передача номера задания
                                           material_name=material_name  # Передача названия материала
                                           )

    payment_id, value, currency, description, payment_link = (  # Распаковка данных из счета
        task_invoice.id, task_invoice.amount['value'], task_invoice.amount['currency'],  # ID, цена, валюта
        task_invoice.description, task_invoice.confirmation.confirmation_url  # Описание, ссылка для подтверждения
    )

    support_url = "https://t.me/ZorngeistQual"                  # URL поддержки
    payment_message = await callback.message.answer(            # Отправка сообщения с информацией о платеже
        f'💰 Оплата: {item_name}\n\n'                            # Сообщение об оплате
        f'💳 Счёт: {payment_id}\n'                               # Сообщение со счетом
        f'📌 Сумма: {value} {currency}\n\n'                       # Сообщение с суммой
        f'❗️ Поддерживаются карты РФ и платёжная система МИР.\n\n'  # Предупреждение
        f'👇 Нажмите на кнопку ниже для перехода к оплате и получения {item_name}.\n\n'  # Инструкция
        f'💬 В случае возникновения вопросов, свяжитесь с поддержкой.\n\n'  # Ссылка на поддержку
        f'💡 После завершения оплаты отправьте чек администраторам для подтверждения, чтобы получить свой '  # Инструкция
        f'{item_name}. Администратор: ZorngeistQual\n\n'  # Ссылка на администратора
        f'⚠️ Это сообщение будет удалено через 2 минуты.',  # Предупреждение об удалении
        disable_web_page_preview=True,  # Отключение предпросмотра веб-страницы
        reply_markup=payment_keyboard(payment_link, subject_to_return)  # Клавиатура с кнопкой оплаты
    )

    return payment_message  # Возврат сообщения


# ====== Обработка и отправка сообщения с платежом ======
async def handle_task(callback: types.CallbackQuery,  # CallbackQuery от aiogram
                      task_id: str,                       # ID задания
                      item_name: str,                     # Название товара/услуги
                      cost: int = 100,                    # Цена (int) товара/услуги, по умолчанию 100
                      material_name: str = "Математика",  # Название материала, по умолчанию "Математика"
                      subject_to_return: str = "subject_math"): # callback для (отмены) платежа "то куда возвращаться после нажатия (отмена)", по умолчанию "subject_math"
    try:
        task_invoice = create_invoice(              # Создание объекта счета
            user_id=callback.from_user.id,          # ID пользователя
            cost=cost,                              # Цена
            task=task_id,                           # ID задания
            material_name=material_name             # Название материала
        )

        initial_message = await callback.message.answer( # Отправка начального сообщения
            f"Вы выбрали задание {task_id}\nСоздание ссылки на оплату..." # Текст сообщения
        )

        await initial_message.edit_text("Ссылка на оплату готова!") # Редактирование сообщения
        _ = asyncio.create_task(delete_message_safe(initial_message, 2)) # Удаление начального сообщения через 2 секунды

        payment_message = await send_payment_message( # Отправка сообщения с информацией о платеже
            callback, # CallbackQuery
            item_name=item_name, # Название товара/услуги
            subject_to_return=subject_to_return, # callback для (отмены) платежа "то куда возвращаться после нажатия (отмена)"
            cost=cost, # Цена
            task=task_id, # ID задания
            material_name=material_name # Название материала
        )

        if payment_message: # Если сообщение с информацией о платеже было отправлено
            _ = asyncio.create_task(delete_message_safe(payment_message, 120)) # Удаление сообщения с информацией о платеже через 120 секунд

    except Exception as e: # Обработка исключений
        logger.error(f"Ошибка при обработке задания {task_id}: {e}") # Логирование ошибки
        await callback.message.answer("Произошла ошибка, попробуйте позже.") # Отправка сообщения об ошибке


# ====== Клавиатура работы с платежом ======
def payment_keyboard(url, subject_to_return):
    """
    Создает клавиатуру для оплаты
    Принимает:
        url - ссылка платежа
        subject_to_return - колбэк для возврата в прошлое меню
    :param url:
    :param subject_to_return:
    :return:
    """
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Оплатить', url=url),
                InlineKeyboardButton(text='Отказ', callback_data="refusal")
            ]
        ]
    )

