from enum import Enum


class MediaProgress(Enum):
    not_started = "not_started"
    in_progress = "in_progress"
    completed = "completed"


MediaProgress.not_started.label = "Not Started"
MediaProgress.in_progress.label = "In Progress"
MediaProgress.completed.label = "Completed"

MEDIA_PROGRESS_CHOICES = [(t.value, t.label) for t in MediaProgress]


class MediaRating(Enum):
    bad = "1"
    okay = "1"
    good = "2"
    great = "4"
    excellent = "5"


MediaRating.bad.label = "Bad"
MediaRating.okay.label = "Okay"
MediaRating.good.label = "Good"
MediaRating.great.label = "Great"
MediaRating.excellent.label = "Excellent"

MEDIA_RATING_CHOICES = [(t.value, t.label) for t in MediaRating]


class MediaStatus(Enum):
    iopc = "i_own_a_physical_copy"
    iodc = "i_own_a_digital_copy"
    btf = "i_borrowed_this_from_a_friend"
    btl = "i_borrowed_this_from_the_local_library"


MediaStatus.iopc.label = "I own a physical copy"
MediaStatus.iodc.label = "I own a digital copy"
MediaStatus.btf.label = "I borrowed this from a friend"
MediaStatus.btl.label = "I borrowed this from the local library"

MEDIA_STATUS_CHOICES = [(t.value, t.label) for t in MediaStatus]


class MediaType(Enum):
    book = "book"
    movie = "movie"
    tv_show = "tv_show"
    podcast = "podcast"
    music = "music"
    game = "game"
    theater = "theater"
    artifact = "artifact"
    discovery = "discovery"


MediaType.book.label = "Book"
MediaType.movie.label = "Movie"
MediaType.tv_show.label = "TV Show"
MediaType.podcast.label = "PodCast"
MediaType.music.label = "Musical Piece/Song"
MediaType.game.label = "Game"
MediaType.theater.label = "Theatical prodcution"
MediaType.artifact.label = "Artifact"
MediaType.discovery.label = "Discovery Item"

MEDIA_TYPE_CHOICES = [(t.value, t.label) for t in MediaType]


class MediaOTypes(Enum):
    fiction = "fiction"
    real = "real"


MediaOTypes.fiction.label = "Fiction"
MediaOTypes.real.label = "Real"

MEDIA_O_TYPES_CHOICES = [(t.value, t.label) for t in MediaOTypes]


class BookFormat(Enum):
    hardcover = "hardcover"
    paperback = "paperback"
    ebook = "ebook"
    audiobook = "audiobook"
    other = "other"


BookFormat.hardcover.label = "Hardcover"
BookFormat.paperback.label = "Paperback"
BookFormat.ebook.label = "Ebook"
BookFormat.audiobook.label = "Audiobook"
BookFormat.other.label = "Other"

BOOK_FORMAT_CHOICES = [(t.value, t.label) for t in BookFormat]


class MovieFormat(Enum):
    dvd = "dvd"
    bluray = "bluray"
    vhs = "vhs"
    streaming = "streaming"
    other = "other"


MovieFormat.dvd.label = "DVD"
MovieFormat.bluray.label = "Blu-Ray"
MovieFormat.vhs.label = "Vhs"
MovieFormat.streaming.label = "Streaming"
MovieFormat.other.label = "Other"

MOVIE_FORMAT_CHOICES = [(t.value, t.label) for t in MovieFormat]


class MediaCreditRoles(Enum):
    author = "author"
    director = "director"
    creator = "creator"
    composer = "composer"
    play_wright = "play_wright"
    developer = "developer"
    host = "host"


MediaCreditRoles.author.label = "Author"
MediaCreditRoles.director.label = "Director"
MediaCreditRoles.creator.label = "Creator"
MediaCreditRoles.composer.label = "Composer or Perfromer"
MediaCreditRoles.play_wright.label = "PlayWright"
MediaCreditRoles.developer.label = "Developer"
MediaCreditRoles.host.label = "Host"

MEDIA_CREDIT_ROLE_CHOICES = [(t.value, t.label) for t in MediaCreditRoles]


class MusicFormat(Enum):
    cd = "cd"
    vinyl = "vinyl"
    cassette = "cassette"
    streaming = "streaming"
    other = "other"


MusicFormat.cd.label = "CD"
MusicFormat.vinyl.label = "Vinyl"
MusicFormat.cassette.label = "Cassette"
MusicFormat.streaming.label = "Streaming"
MusicFormat.other.label = "Other"

MUSIC_FORMAT_CHOICES = [(t.value, t.label) for t in MusicFormat]


class PodCastFormat(Enum):
    podcast = "podcast"
    audiobook = "audiobook"
    other = "other"


PodCastFormat.podcast.label = "Podcast"
PodCastFormat.audiobook.label = "Audiobook"
PodCastFormat.other.label = "Other"

PODCAST_FORMAT_CHOICES = [(t.value, t.label) for t in PodCastFormat]


class GameFormat(Enum):
    video_game = "video_game"
    board_game = "board_game"
    mobile_game = "mobile_game"
    tabletop_game = "tabletop_game"
    other = "other"


GameFormat.video_game.label = "Video Game"
GameFormat.board_game.label = "Board Game"
GameFormat.mobile_game.label = "Mobile Game"
GameFormat.tabletop_game.label = "Tabletop RPG"
GameFormat.other.label = "Other"

GAME_FORMAT_CHOICES = [(t.value, t.label) for t in GameFormat]


class TheaterFormat(Enum):
    live_performance = "live_performance"
    recording = "recording"
    other = "other"


TheaterFormat.live_performance.label = "Live Performance"
TheaterFormat.recording.label = "Recording"
TheaterFormat.other.label = "Other"

THEATER_FORMAT_CHOICES = [(t.value, t.label) for t in TheaterFormat]


class ArtifactFormat(Enum):
    sculpture = "sculpture"
    painting = "painting"
    other = "other"


ArtifactFormat.sculpture.label = "Sculpture"
ArtifactFormat.painting.label = "Painting"
ArtifactFormat.other.label = "Other"

ARTIFACT_FORMAT_CHOICES = [(t.value, t.label) for t in ArtifactFormat]

MEDIA_FORMAT_CHOICES = (
    BOOK_FORMAT_CHOICES
    + MOVIE_FORMAT_CHOICES
    + MUSIC_FORMAT_CHOICES
    + PODCAST_FORMAT_CHOICES
    + GAME_FORMAT_CHOICES
    + THEATER_FORMAT_CHOICES
    + ARTIFACT_FORMAT_CHOICES
)


class SourceType(Enum):
    native = "native"
    mentioned = "mentioned"


SourceType.native.label = "Native"
SourceType.mentioned.label = "Mentioned"

SOURCE_TYPE_CHOICES = [(t.value, t.label) for t in SourceType]


# class PlaceType(Enum):
#     real = "real"
#     fictional = "fictional"


# PlaceType.real.label = "Real"
# PlaceType.fictional.label = "Fictional"

# PLACE_TYPE_CHOICES = [(t.value, t.label) for t in PlaceType]


class GenreApplicableFormat(Enum):
    book = "book"
    movie = "movie"
    music = "music"
    game = "game"
    theater = "theater"
    artifact = "artifact"


GenreApplicableFormat.book.label = "Book"
GenreApplicableFormat.movie.label = "Movie"
GenreApplicableFormat.music.label = "Music"
GenreApplicableFormat.game.label = "Game"
GenreApplicableFormat.theater.label = "Theater"
GenreApplicableFormat.artifact.label = "Artifact"

GENRE_APPLICABLE_FORMAT_CHOICES = [(t.value, t.label) for t in GenreApplicableFormat]
