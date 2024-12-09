from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from db.urls import router as db_router


api = NinjaAPI()

@api.get("")
def index(request):
    return {"넌 뭐야!!!":"나가"}

api.add_router("db", db_router)


urlpatterns = [
    path("", api.urls),
    path('admin/', admin.site.urls),
]
