from django.urls import path
from ninja import Router, Schema
from django.shortcuts import get_object_or_404
from db.croll import croll
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

#노래 제목 검색
@router.get("search")
def search(request, a:str):
    if(Music.objects.filter(title__icontains=a).count() > 0):
        result = [
            {
                "number": music.number,
                "title": music.title,
                "singer": music.singer,
                "composer": music.composer,
                "star": music.star,
            }
            for music in Music.objects.filter(title__icontains=a).all()
        ]
    else:
        result = croll(a)

    return {"searchRes": result}

# 특정 음악 삭제
@router.delete('/{music_number}')
def delete_music(request, music_number: int):
    music = get_object_or_404(Music, number=music_number)
    music.delete()
    return {"message": f"Music with ID {music_number} has been deleted."}

class musicItem(Schema):
    number: int
    title: str
    singer: str
    composer: str

# 특정 음악 추가
@router.post('')
def add_music(request, music: musicItem):
    # 전달받은 음악 데이터로 새로운 음악 객체 생성
    new_music = Music(
        number=music.number,
        title=music.title,
        singer=music.singer,
        composer=music.composer,
    )

    # 새 음악 저장
    new_music.save()
    return {"저장됨": new_music.title}