from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .enums import (
    MOVIE_FORMAT_CHOICES,
    BOOK_FORMAT_CHOICES,
    MediaType,
    MUSIC_FORMAT_CHOICES,
    PODCAST_FORMAT_CHOICES,
    GAME_FORMAT_CHOICES,
    THEATER_FORMAT_CHOICES,
    ARTIFACT_FORMAT_CHOICES,
)
from discovery.models import Media


@method_decorator(login_required, name="dispatch")
@method_decorator(staff_member_required, name="dispatch")
class FormatChoicesView(View):
    def get(self, request, *args, **kwargs):
        media_type_id = self.request.GET.get("media_type_id")
        object_id = self.request.GET.get("obj_id")
        try:
            media = Media.objects.get(id=object_id)
            media_format = media.format
        except Exception as e:
            media_format = ""

        if not media_type_id:
            return JsonResponse({})
        if media_type_id == MediaType.book.value:
            choices = {obj[0]: obj[1] for obj in BOOK_FORMAT_CHOICES}
        elif media_type_id == MediaType.movie.value:
            choices = {obj[0]: obj[1] for obj in MOVIE_FORMAT_CHOICES}
        elif media_type_id == MediaType.tv_show.value:
            choices = {obj[0]: obj[1] for obj in MOVIE_FORMAT_CHOICES}
        elif media_type_id == MediaType.music.value:
            choices = {obj[0]: obj[1] for obj in MUSIC_FORMAT_CHOICES}
        elif media_type_id == MediaType.podcast.value:
            choices = {obj[0]: obj[1] for obj in PODCAST_FORMAT_CHOICES}
        elif media_type_id == MediaType.game.value:
            choices = {obj[0]: obj[1] for obj in GAME_FORMAT_CHOICES}
        elif media_type_id == MediaType.theater.value:
            choices = {obj[0]: obj[1] for obj in THEATER_FORMAT_CHOICES}
        elif media_type_id == MediaType.artifact.value:
            choices = {obj[0]: obj[1] for obj in ARTIFACT_FORMAT_CHOICES}
        else:
            choices = {"choices": {}, "selected": media_format}
        return JsonResponse({"choices": choices, "selected": media_format})
