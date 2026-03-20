from django.urls import path
from .views import *

urlpatterns = [
    path('', login_and_register_page, name='login_and_register_page'),
    path('register_to_classroom/', register_to_classroom, name='register_to_classroom'),
    path('login_to_classroom/', login_to_classroom, name='login_to_classroom'),
    path('logout/', logout_from_classroom, name='logout_from_classroom'),
    path('main/', main_page, name='main_page'),
    path('create-classroom/', create_classroom, name='create_classroom'),
    path('join-classroom-request/', join_classroom_request, name='join_classroom_request'),
    path('classroom/<int:classroom_id>/', classroom_detail_page, name='classroom_detail_page'),
    path('classroom/<int:classroom_id>/exit-or-kick/', exit_or_kick_classroom, name='exit_or_kick_classroom'),
    path('classroom/<int:classroom_id>/homework/<int:homework_id>/edit/', browser_editor_page,
         name='browser_editor_page'),
    path('classroom/<int:classroom_id>/homework/<int:homework_id>/save-editor/', save_browser_editor,
         name='save_browser_editor'),

    # ── Image upload for browser editor ──────────────────────────────
    path('classroom/<int:classroom_id>/homework/<int:homework_id>/upload-image/', upload_editor_image,
         name='upload_editor_image'),
]