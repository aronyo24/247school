JAZZMIN_SETTINGS = {
    "site_title": "Admin",
    "site_header": "Admin",
    "site_brand": "Aadmin",
    "welcome_sign": "Welcome to 247school admin Portal",

    "site_logo": "static/images/logo.png",
    "login_logo": "staogo.tic/images/lpng",
    "site_icon": None,
    "user_avatar": None,

    "language_chooser": False,
    "copyright": "School247",

    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"app": "auth"},
        {"model": "auth.User"},
    ],

    "order_with_respect_to": [
        "auth",
        "schoolapp",
        "team",
        "content",
    ],

    "custom_links": {
        "schoolapp": [
            {
                "name": "Dashboard",
                "url": "dashboard",
                "icon": "fas fa-tachometer-alt",
            },
        ],
        "content": [
            {"name": "Standards", "url": "/admin/content/a_standard/", "icon": "fas fa-layer-group"},
            {"name": "Subjects", "url": "/admin/content/b_subject/", "icon": "fas fa-book"},
            {"name": "Sections", "url": "/admin/content/c_section/", "icon": "fas fa-bookmark"},
            {"name": "Lessons", "url": "/admin/content/d_lesson/", "icon": "fas fa-video"},
            {"name": "Subsections", "url": "/admin/content/e_subsection/", "icon": "fas fa-clipboard-list"},
            {"name": "Quizzes", "url": "/admin/content/f_quiz/", "icon": "fas fa-question-circle"},
            {"name": "Notes", "url": "/admin/content/g_note/", "icon": "fas fa-file-alt"},
        ],
    },

    # Optional: hide models from main menu if needed
     "hide_models": [
         "content.a_standard", "content.b_subject", "content.c_section",
         "content.d_lesson", "content.e_subsection", "content.f_quiz", "content.g_note"
     ],

    "related_modal_active": True,
    "changeform_format": "single",
    "use_google_fonts_cdn": True,
    "show_sidebar": True,
    "navigation_expanded": True,
}
