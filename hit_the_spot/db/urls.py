from django.urls import path
from ninja import Router
from django.shortcuts import get_object_or_404
from db.models import Music

router = Router()

# 모든 데이터 가져오기
@router.get('')
def get_musics(request):
    musics = Music.objects.all()
    serialized_data = [
        {
            "number": music.number,
            "title": music.title,
            "singer": music.singer,
            "composer": music.composer,
            "star": music.star,
        }
        for music in musics
    ]
    return {"musics": serialized_data}

# 특정 음악 삭제
@router.delete('/{music_number}')
def delete_music(request, music_number: int):
    music = get_object_or_404(Music, number=music_number)
    music.delete()
    return {"message": f"Music with ID {music_number} has been deleted."}
