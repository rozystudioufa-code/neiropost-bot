from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from bot.keyboards.main_kb import main_menu

router = Router()

WELCOME_TEXT = (
    "Привет, <b>{name}</b>! 👋\n\n"
    "Я <b>НейроПост</b> — твой личный AI-помощник для соцсетей.\n\n"
    "Каждый день я сам <b>пишу, оформляю и публикую</b> посты в твой канал — "
    "пока ты занимаешься своим делом.\n\n"
    "<b>Для кого я создан:</b>\n"
    "• Эксперты и специалисты\n"
    "• Владельцы малого бизнеса\n"
    "• Все, кто хочет вести соцсети, но нет времени\n\n"
    "Готова начать? 🚀"
)


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        WELCOME_TEXT.format(name=message.from_user.first_name),
        reply_markup=main_menu(),
    )


@router.callback_query(lambda c: c.data == "start_onboarding")
async def cb_onboarding(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "Отлично! Сейчас настроим бота под тебя.\n\n"
        "Это займёт меньше минуты — ответишь на 5 коротких вопросов, "
        "и я покажу тебе пример поста ещё <b>до оплаты</b>.\n\n"
        "<i>Эта функция появится в следующем шаге разработки 🔧</i>"
    )


@router.callback_query(lambda c: c.data == "show_pricing")
async def cb_pricing(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "<b>Тарифы НейроПост:</b>\n\n"
        "🟢 <b>Старт</b> — 490 ₽/мес\n"
        "1 платформа · 3 поста/нед · текст + карточка\n\n"
        "🔵 <b>Про</b> — 990 ₽/мес\n"
        "2 платформы · 7 постов/нед · история постов\n\n"
        "🟣 <b>Бизнес</b> — 2 490 ₽/мес\n"
        "3 платформы · безлимит · приоритетная поддержка\n\n"
        "Первые 7 дней — бесплатно, карта не нужна 🎁\n\n"
        "<i>Оплата появится в следующих шагах разработки 🔧</i>"
    )


@router.callback_query(lambda c: c.data == "show_referral")
async def cb_referral(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "<b>Реферальная программа:</b>\n\n"
        "Приглашай друзей — получай бонусы:\n\n"
        "• За каждого оплатившего друга → <b>+1 месяц бесплатно</b>\n"
        "• Твой друг получает расширенный триал <b>14 дней</b> вместо 7\n\n"
        "<i>Реферальные ссылки появятся позже 🔧</i>"
    )


@router.callback_query(lambda c: c.data == "show_help")
async def cb_help(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "<b>Помощь:</b>\n\n"
        "/start — главное меню\n\n"
        "По всем вопросам пиши в поддержку.\n\n"
        "<i>Раздел помощи будет расширен 🔧</i>"
    )
