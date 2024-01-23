JAZZMIN_SETTINGS = {
    # заголовок окна
    'site_title':'LocalLibrary Admin Panel',
    # Название на экране входа в систему
    'site_header':'LocalLibrary Admin Panel',
    # Название бренда
    'site_brand':'You order we Delivered',
    # Классы CSS, которые применяются к логотипу выше
    'site_logo_classes':'img-circle',
    # Логотип для использования на вашем сайте должен присутствовать в статических файлах и использоваться для логотипа формы входа.
    "login_logo": None,
    # Логотип для формы входа в темных темах (по умолчанию — login_logo).
    "login_logo_dark": None,
    # Относительный путь к значку вашего сайта, по умолчанию будет site_logo, если он отсутствует.
    "site_icon": None,
    # Текст приветствия на экране входа в систему
    'welcome_sign':'Welcome to the Admin Panel Locallibrary',
    # Список администраторов модели для поиска из панели поиска, панель поиска опускается, если она исключена
    "search_model": ["auth.User", "auth.Group"],
    # Авторские права в нижнем колонтитуле
    'copyright':'Geeks Pro',

    # Имя поля в модели пользователя, которое содержит аватар ImageField/URLField/Charfield или вызываемый объект, который получает пользователя
     "user_avatar": 'None',

    ############
    # Top Menu #
    ############

    # Ссылки для размещения в верхнем меню
     "topmenu_links": [
        # url, который меняется на противоположный (можно добавить разрешения)
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        # внешний URL-адрес, который открывается в новом окне (можно добавить разрешения)
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
     ],

    #############
    # Side Menu #
    #############

    # Отображать ли боковое меню
    "show_sidebar": True,
    # Стоит ли автоматически расширять меню
    "navigation_expanded": True,
    # Скрыть эти приложения при создании бокового меню, например (аутентификация)
    "hide_apps": [],
    # Скрыть эти модели при создании бокового меню
    "hide_models": [],

# Значки, которые используются, если они не указаны вручную
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-thumbtack",

    #################
    # Related Modal #
    #################
    # Используйте модальные окна вместо всплывающих окон
    "related_modal_active": True,

    #############
    # UI Tweaks #
    #############
    # Относительные пути к пользовательским сценариям CSS/JS (должны присутствовать в статических файлах)
    "custom_css": None,
    "custom_js": None,
    # Показывать ли настройщик пользовательского интерфейса на боковой панели
    "show_ui_builder": False,

    ###############
    # Change view #
    ###############
    # Отображение представления изменений в виде отдельной формы или вкладок, текущие параметры
    # - одинокий
    # - горизонтальные_табы (по умолчанию)
    # - вертикальные_табы
    # - складной
    # - карусель
    "changeform_format": "horizontal_tabs",
    # переопределить формы изменений для каждого администратора модели
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
}


JAZZMIN_UI_TWEAKS = {
    "theme": "slate",
    "navbar_small_text": False,
    "footer_small_text": True,
    "body_small_text": False,
    "brand_small_text": True,
    "brand_colour": "navbar-dark",
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-warning",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": True,
    "sidebar_nav_flat_style": False,
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success"
    },
    "actions_sticky_top": False

}