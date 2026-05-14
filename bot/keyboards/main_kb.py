from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚀 Настроить бота", callback_data="start_onboarding")],
        [InlineKeyboardButton(text="💳 Тарифы", callback_data="show_pricing")],
        [InlineKeyboardButton(text="🔗 Пригласить друга", callback_data="show_referral")],
        [InlineKeyboardButton(text="❓ Помощь", callback_data="show_help")],
    ])
