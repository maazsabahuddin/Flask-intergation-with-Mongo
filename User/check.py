from functools import wraps
import re
import emoji


def makebold(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        return "<b>" + fn(*args, **kwargs) + "</b>"
    return wrapped


def makeitalic(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        return "<i>" + fn(*args, **kwargs) + "</i>"
    return wrapped


@makebold
@makeitalic
def hello():
    return "hello world"


@makebold
@makeitalic
def log(s):
    return s


# print(hello())       # returns "<b><i>hello world</i></b>"
# print(hello.__name__) # with functools.wraps() this returns "hello"
# print(log('hello'))   # returns "<b><i>hello</i></b>"


def mymethod(**data):
    email = data.get('email')
    print(email)
    for key, value in data.items():
        print('{} - {}'.format(key, value))


# dic = {1: 2, 2: 3, 3: 4}
# mymethod(email='Maaz', age=21)


def validate_full_name(full_name):
    """ verifies if the full name follows the validations """

    full_regex_unicode = r'[\u0020-\u00d7ff]{0,}'
    emoticon_regex = emoji.get_emoji_regexp()
    special_character_regex = r'[.+-@_!#$%^&*()<>?/\'"\\"|}{~:0-9]'

    if not full_name:
        return False
    if re.search(special_character_regex, full_name):
        return False
    if emoticon_regex.search(full_name):
        return False
    if re.match(full_regex_unicode, full_name, re.UNICODE):
        return True

    return False


def test_validate_full_name():
    """
    The function will print True or False as per the below list of full_names
    :return:
    """
    # should return True
    full_name_different_languages = ['Maaz Sabah Uddin ', 'معاذ صباح الدین', 'Garçon', 'يبتس', '你好', 'አምኒግሎት',
                                     'ᨕᨚᨆᨊᨗᨁᨒᨚᨈ', 'သြပ်နိဂ်လောိတသ ြပ်နိဂ်လောိတ', '奥姆尼格洛特 àomǔnígéluòtè', 'Ⲟⲙⲛⲓⲅⲗⲟⲧ',
                                     'Всепереводчик']

    # should return False
    full_name_with_face_emoticons = ['😂🙊😌🚄💯😑😉😀🤦‍♂😐', '😂', '😤🙄😬😵😝🙈', '😱😍❤', '👍😎🚅🖐️']

    # should return False
    full_name_with_different_types_of_emoji = ['🌎🌾💐', '🌷🥀🌺🌸', '🌟✨🌼', '🌻⚡🦡🐎', '🦬🦀🦂🕸', '️🐨🐭', '🙊🪰🐋🐊']

    # should return False
    full_name_with_special_characters = [',', '+', '-', '_', '@', '1', '9', '_', '!', '#', '$', '%', '^', '&', '*', '(',
                                         ')', '<', '>', '?', '/', '\\', '|', '{', '}', '~', ':', '\'', '"']

    # return True False accordingly
    full_name_random = ['Maaz"\\"', 'Maaz.', 'maaz@gmail.com', ' Ⲟⲙⲛⲓⲅⲗⲟ معاذ Maaz ', 'သြပ်နိဂ်လောိတသ',
                        'Ẫ ẫ Ẩ ẩ Ả ả Ǎ ǎ Ⱥ ⱥ Ȧ ȧ Ǡ', '', 'معاذ صباح الدین']

    for full_name in full_name_different_languages:
        assert validate_full_name(full_name) is True, "Condition False"
        # print(validate_full_name(full_name))


test_validate_full_name()

# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))
#
#
# has_emoji = bool(emoji.get_emoji_regexp().search('Maaz😂'))
#
#
# def char_is_emoji(character):
#     return character in emoji.UNICODE_EMOJI
#
#
# def text_has_emoji(text):
#     for character in text:
#         if character in emoji.UNICODE_EMOJI:
#             return True
#     return False


# print(text_has_emoji('Maaz😂'))
# print(has_emoji)
# import sys
# print(hex(sys.maxunicode))
# print(hex(ord('😌')))
