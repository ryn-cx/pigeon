from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from datetime import date, time
from typing import Any
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field, NaiveDatetime

class Links(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    self: str | Any = Field(default=None, union_mode='left_to_right')

class Images(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    node_types: list[str] | Any = Field(None, alias='nodeTypes', union_mode='left_to_right')
    count: int | Any = Field(default=None, union_mode='left_to_right')

class FirstEp(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    node_types: list[str] | Any = Field(None, alias='nodeTypes', union_mode='left_to_right')
    count: int | Any = Field(default=None, union_mode='left_to_right')

class Shortforms(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    node_types: list[str] | Any = Field(None, alias='nodeTypes', union_mode='left_to_right')
    count: int | Any = Field(default=None, union_mode='left_to_right')

class FreeEpisodes(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    node_types: list[Any] | Any = Field(None, alias='nodeTypes', union_mode='left_to_right')
    count: int | Any = Field(default=None, union_mode='left_to_right')

class Clips(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    node_types: list[str] | Any = Field(None, alias='nodeTypes', union_mode='left_to_right')
    count: int | Any = Field(default=None, union_mode='left_to_right')

class LinkedAssets(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    node_types: list[str] | Any = Field(None, alias='nodeTypes', union_mode='left_to_right')
    count: int | Any = Field(default=None, union_mode='left_to_right')

class Items(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    node_types: list[str] | Any = Field(None, alias='nodeTypes', union_mode='left_to_right')
    count: int | Any = Field(default=None, union_mode='left_to_right')

class Trailers(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    node_types: list[str] | Any = Field(None, alias='nodeTypes', union_mode='left_to_right')
    count: int | Any = Field(default=None, union_mode='left_to_right')

class Collections(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    node_types: list[str] | Any = Field(None, alias='nodeTypes', union_mode='left_to_right')
    count: int | Any = Field(default=None, union_mode='left_to_right')

class Latest(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    node_types: list[str] | Any = Field(None, alias='nodeTypes', union_mode='left_to_right')
    count: int | Any = Field(default=None, union_mode='left_to_right')

class ChildTypes(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    images: Images | Any = Field(default=None, union_mode='left_to_right')
    first_ep: FirstEp | Any = Field(default=None, union_mode='left_to_right')
    shortforms: Shortforms | Any = Field(default=None, union_mode='left_to_right')
    free_episodes: FreeEpisodes | Any = Field(default=None, union_mode='left_to_right')
    clips: Clips | Any = Field(default=None, union_mode='left_to_right')
    linked_assets: LinkedAssets | Any = Field(default=None, union_mode='left_to_right')
    items: Items | Any = Field(default=None, union_mode='left_to_right')
    trailers: Trailers | Any = Field(default=None, union_mode='left_to_right')
    collections: Collections | Any = Field(default=None, union_mode='left_to_right')
    latest: Latest | Any = Field(default=None, union_mode='left_to_right')

class AudienceLevelItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    scheme_provider: str | Any = Field(None, alias='schemeProvider', union_mode='left_to_right')
    segment_code: str | Any = Field(None, alias='segmentCode', union_mode='left_to_right')
    target_segment: str | Any = Field(None, alias='targetSegment', union_mode='left_to_right')

class VideoFormat(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_format: str | Any = Field(None, alias='videoFormat', union_mode='left_to_right')
    colour_spaces: list[str] | Any = Field(None, alias='colourSpaces', union_mode='left_to_right')
    audio_tracks: list[str] | Any = Field(None, alias='audioTracks', union_mode='left_to_right')

class TuneInBadgingEditorialTexts(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    short: str | Any = Field(default=None, union_mode='left_to_right')
    long: str | Any = Field(default=None, union_mode='left_to_right')

class TuneInBadging(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tune_in_badging_editorial_texts: TuneInBadgingEditorialTexts | Any = Field(None, alias='tuneInBadgingEditorialTexts', union_mode='left_to_right')

class Badging(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_formats: list[VideoFormat] | Any = Field(None, alias='videoFormats', union_mode='left_to_right')
    audio_tracks: list[str] | Any = Field(None, alias='audioTracks', union_mode='left_to_right')
    tune_in_badging: TuneInBadging | Any = Field(None, alias='tuneInBadging', union_mode='left_to_right')

class LogoItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    key: str | Any = Field(default=None, union_mode='left_to_right')
    template: str | Any = Field(default=None, union_mode='left_to_right')

class Channel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    access_channel: str | Any = Field(None, alias='accessChannel', union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    logo_style: str | Any = Field(None, alias='logoStyle', union_mode='left_to_right')
    provider_id: str | Any = Field(None, alias='providerId', union_mode='left_to_right')
    logo: list[LogoItem] | Any = Field(default=None, union_mode='left_to_right')
    sections: list[str] | Any = Field(default=None, union_mode='left_to_right')
    logo_height_percentage: int | Any = Field(None, alias='logoHeightPercentage', union_mode='left_to_right')

class DeviceAvailability(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    format: str | Any = Field(default=None, union_mode='left_to_right')
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    offer_stage: str | Any = Field(None, alias='offerStage', union_mode='left_to_right')
    offer_start_ts: int | Any = Field(None, alias='offerStartTs', union_mode='left_to_right')
    offer_end_ts: int | Any = Field(None, alias='offerEndTs', union_mode='left_to_right')
    content_segment: str | Any = Field(None, alias='contentSegment', union_mode='left_to_right')
    video_format: str | Any = Field(None, alias='videoFormat', union_mode='left_to_right')
    video_format_variant: str | Any = Field(None, alias='videoFormatVariant', union_mode='left_to_right')
    colour_space: str | Any = Field(None, alias='colourSpace', union_mode='left_to_right')

class DeviceAvailability1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    available: bool | Any = Field(default=None, union_mode='left_to_right')

class FanCriticRatingItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | Any = Field(default=None, union_mode='left_to_right')
    fan_score: int | Any = Field(None, alias='fanScore', union_mode='left_to_right')
    critic_score: int | Any = Field(None, alias='criticScore', union_mode='left_to_right')

class AudioTracks(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    spa: list[str] | Any = Field(default=None, union_mode='left_to_right')
    eng: list[str] | Any = Field(default=None, union_mode='left_to_right')

class AvailableDevice(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    platform: str | Any = Field(default=None, union_mode='left_to_right')

class Availability(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    available: bool | Any = Field(default=None, union_mode='left_to_right')
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    offer_stage: str | Any = Field(None, alias='offerStage', union_mode='left_to_right')
    offer_start_ts: int | Any = Field(None, alias='offerStartTs', union_mode='left_to_right')
    offer_end_ts: int | Any = Field(None, alias='offerEndTs', union_mode='left_to_right')
    available_devices: list[AvailableDevice] | Any = Field(None, alias='availableDevices', union_mode='left_to_right')
    extended_offer_start_ts: int | Any = Field(None, alias='extendedOfferStartTs', union_mode='left_to_right')
    extended_offer_end_ts: int | Any = Field(None, alias='extendedOfferEndTs', union_mode='left_to_right')
    content_segment: str | Any = Field(None, alias='contentSegment', union_mode='left_to_right')
    video_format: str | Any = Field(None, alias='videoFormat', union_mode='left_to_right')
    video_format_variant: str | Any = Field(None, alias='videoFormatVariant', union_mode='left_to_right')
    colour_space: str | Any = Field(None, alias='colourSpace', union_mode='left_to_right')

class Hd(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    audio_tracks: AudioTracks | Any = Field(None, alias='audioTracks', union_mode='left_to_right')
    chapter_markers: list[Any] | Any = Field(None, alias='chapterMarkers', union_mode='left_to_right')
    event_stage: str | Any = Field(None, alias='eventStage', union_mode='left_to_right')
    availability: Availability | Any = Field(default=None, union_mode='left_to_right')
    start_of_credits: int | Any = Field(None, alias='startOfCredits', union_mode='left_to_right')

class Formats(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hd: Hd | Any = Field(None, alias='HD', union_mode='left_to_right')

class GenreDetail(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    primary: bool | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    term_id: str | Any = Field(None, alias='termId', union_mode='left_to_right')
    term_description: str | Any = Field(None, alias='termDescription', union_mode='left_to_right')
    code: str | Any = Field(default=None, union_mode='left_to_right')

class GenreListItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    subgenre: list[str] | Any = Field(default=None, union_mode='left_to_right')
    genre: list[str] | Any = Field(default=None, union_mode='left_to_right')

class Image(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')

class MediaType(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    count: int | Any = Field(default=None, union_mode='left_to_right')
    latest: int | Any = Field(default=None, union_mode='left_to_right')

class TargetAudience(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')

class Attributes(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    free_wheel_content_id: str | Any = Field(None, alias='FreeWheelContentID', union_mode='left_to_right')
    audience_level: list[AudienceLevelItem] | Any = Field(None, alias='audienceLevel', union_mode='left_to_right')
    audio_described: bool | Any = Field(None, alias='audioDescribed', union_mode='left_to_right')
    available_episode_count: int | Any = Field(None, alias='availableEpisodeCount', union_mode='left_to_right')
    available_season_count: int | Any = Field(None, alias='availableSeasonCount', union_mode='left_to_right')
    badging: Badging | Any = Field(default=None, union_mode='left_to_right')
    brands: list[str] | Any = Field(default=None, union_mode='left_to_right')
    cast: list[str] | Any = Field(default=None, union_mode='left_to_right')
    channel: Channel | Any = Field(default=None, union_mode='left_to_right')
    chapters_enabled: bool | Any = Field(None, alias='chaptersEnabled', union_mode='left_to_right')
    child_node_types: list[str] | Any = Field(None, alias='childNodeTypes', union_mode='left_to_right')
    classification: list[str] | Any = Field(default=None, union_mode='left_to_right')
    collection_pdp: str | Any = Field(None, alias='collectionPdp', union_mode='left_to_right')
    content_segments: list[str] | Any = Field(None, alias='contentSegments', union_mode='left_to_right')
    created_date: int | Any = Field(None, alias='createdDate', union_mode='left_to_right')
    desc_long_seo: str | Any = Field(None, alias='descLongSeo', union_mode='left_to_right')
    device_availabilities: list[DeviceAvailability] | Any = Field(None, alias='deviceAvailabilities', union_mode='left_to_right')
    device_availability: DeviceAvailability1 | Any = Field(None, alias='deviceAvailability', union_mode='left_to_right')
    fan_critic_rating: list[FanCriticRatingItem] | Any = Field(None, alias='fanCriticRating', union_mode='left_to_right')
    formats: Formats | Any = Field(default=None, union_mode='left_to_right')
    genre_details: list[GenreDetail] | Any = Field(None, alias='genreDetails', union_mode='left_to_right')
    genre_list: list[GenreListItem] | Any = Field(None, alias='genreList', union_mode='left_to_right')
    genres: list[str] | Any = Field(default=None, union_mode='left_to_right')
    gracenote_id: str | Any = Field(None, alias='gracenoteId', union_mode='left_to_right')
    gracenote_series_id: str | Any = Field(None, alias='gracenoteSeriesId', union_mode='left_to_right')
    images: list[Image] | Any = Field(default=None, union_mode='left_to_right')
    media_types: list[MediaType] | Any = Field(None, alias='mediaTypes', union_mode='left_to_right')
    merlin_id: str | Any = Field(None, alias='merlinId', union_mode='left_to_right')
    merlin_series_id: str | Any = Field(None, alias='merlinSeriesId', union_mode='left_to_right')
    nbcu_id: str | Any = Field(None, alias='nbcuId', union_mode='left_to_right')
    nbcu_series_id: str | Any = Field(None, alias='nbcuSeriesId', union_mode='left_to_right')
    ott_certificate: str | Any = Field(None, alias='ottCertificate', union_mode='left_to_right')
    provider_series_id: str | Any = Field(None, alias='providerSeriesId', union_mode='left_to_right')
    reverse_order: bool | Any = Field(None, alias='reverseOrder', union_mode='left_to_right')
    section_navigation: str | Any = Field(None, alias='sectionNavigation', union_mode='left_to_right')
    series_native_id: str | Any = Field(None, alias='seriesNativeId', union_mode='left_to_right')
    series_uuid: UUID | Any = Field(None, alias='seriesUuid', union_mode='left_to_right')
    slug: str | Any = Field(default=None, union_mode='left_to_right')
    smart_call_to_action: str | Any = Field(None, alias='smartCallToAction', union_mode='left_to_right')
    sort_title: str | Any = Field(None, alias='sortTitle', union_mode='left_to_right')
    synopsis_long: str | Any = Field(None, alias='synopsisLong', union_mode='left_to_right')
    target_audience: TargetAudience | Any = Field(None, alias='targetAudience', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    title_medium: str | Any = Field(None, alias='titleMedium', union_mode='left_to_right')
    title_seo: str | Any = Field(None, alias='titleSeo', union_mode='left_to_right')
    synopsis: str | Any = Field(default=None, union_mode='left_to_right')
    synopsis_short: str | Any = Field(None, alias='synopsisShort', union_mode='left_to_right')
    title_medium_seo: str | Any = Field(None, alias='titleMediumSeo', union_mode='left_to_right')

class FreeEpisodes1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    node_types: list[str] | Any = Field(None, alias='nodeTypes', union_mode='left_to_right')
    count: int | Any = Field(default=None, union_mode='left_to_right')

class NextClips(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    node_types: list[str] | Any = Field(None, alias='nodeTypes', union_mode='left_to_right')
    count: int | Any = Field(default=None, union_mode='left_to_right')

class NextShortforms(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    node_types: list[str] | Any = Field(None, alias='nodeTypes', union_mode='left_to_right')
    count: int | Any = Field(default=None, union_mode='left_to_right')

class ChildTypes1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    images: Images | Any = Field(default=None, union_mode='left_to_right')
    first_ep: FirstEp | Any = Field(default=None, union_mode='left_to_right')
    shortforms: Shortforms | Any = Field(default=None, union_mode='left_to_right')
    free_episodes: FreeEpisodes1 | Any = Field(default=None, union_mode='left_to_right')
    clips: Clips | Any = Field(default=None, union_mode='left_to_right')
    items: Items | Any = Field(default=None, union_mode='left_to_right')
    latest: Latest | Any = Field(default=None, union_mode='left_to_right')
    trailers: Trailers | Any = Field(default=None, union_mode='left_to_right')
    collections: Collections | Any = Field(default=None, union_mode='left_to_right')
    next_clips: NextClips | Any = Field(default=None, union_mode='left_to_right')
    next_shortforms: NextShortforms | Any = Field(default=None, union_mode='left_to_right')
    linked_assets: LinkedAssets | Any = Field(default=None, union_mode='left_to_right')

class TuneInBadging1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    tune_in_badging_editorial_texts: TuneInBadgingEditorialTexts | Any = Field(None, alias='tuneInBadgingEditorialTexts', union_mode='left_to_right')

class Badging1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_formats: list[VideoFormat] | Any = Field(None, alias='videoFormats', union_mode='left_to_right')
    audio_tracks: list[str] | Any = Field(None, alias='audioTracks', union_mode='left_to_right')
    tune_in_badging: TuneInBadging1 | Any = Field(None, alias='tuneInBadging', union_mode='left_to_right')

class Channel1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    logo_style: str | Any = Field(None, alias='logoStyle', union_mode='left_to_right')
    access_channel: str | Any = Field(None, alias='accessChannel', union_mode='left_to_right')
    provider_id: str | Any = Field(None, alias='providerId', union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    logo: list[LogoItem] | Any = Field(default=None, union_mode='left_to_right')
    sections: list[str] | Any = Field(default=None, union_mode='left_to_right')
    logo_height_percentage: int | Any = Field(None, alias='logoHeightPercentage', union_mode='left_to_right')

class DeviceAvailability2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    format: str | Any = Field(default=None, union_mode='left_to_right')
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    offer_stage: str | Any = Field(None, alias='offerStage', union_mode='left_to_right')
    offer_start_ts: int | Any = Field(None, alias='offerStartTs', union_mode='left_to_right')
    offer_end_ts: int | Any = Field(None, alias='offerEndTs', union_mode='left_to_right')
    content_segment: str | Any = Field(None, alias='contentSegment', union_mode='left_to_right')
    video_format: str | Any = Field(None, alias='videoFormat', union_mode='left_to_right')
    video_format_variant: str | Any = Field(None, alias='videoFormatVariant', union_mode='left_to_right')
    colour_space: str | Any = Field(None, alias='colourSpace', union_mode='left_to_right')
    streamable: bool | Any = Field(default=None, union_mode='left_to_right')
    downloadable: bool | Any = Field(default=None, union_mode='left_to_right')

class DeviceAvailability3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    available: bool | Any = Field(default=None, union_mode='left_to_right')

class FanCriticRatingItem1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | Any = Field(default=None, union_mode='left_to_right')
    critic_score: int | Any = Field(None, alias='criticScore', union_mode='left_to_right')
    fan_score: int | Any = Field(None, alias='fanScore', union_mode='left_to_right')
    tags: list[str] | Any = Field(default=None, union_mode='left_to_right')

class AudioTracks1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    eng: list[str] | Any = Field(default=None, union_mode='left_to_right')
    spa: list[str] | Any = Field(default=None, union_mode='left_to_right')

class Availability1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    available: bool | Any = Field(default=None, union_mode='left_to_right')
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    offer_stage: str | Any = Field(None, alias='offerStage', union_mode='left_to_right')
    offer_start_ts: int | Any = Field(None, alias='offerStartTs', union_mode='left_to_right')
    offer_end_ts: int | Any = Field(None, alias='offerEndTs', union_mode='left_to_right')
    available_devices: list[AvailableDevice] | Any = Field(None, alias='availableDevices', union_mode='left_to_right')
    extended_offer_start_ts: int | Any = Field(None, alias='extendedOfferStartTs', union_mode='left_to_right')
    extended_offer_end_ts: int | Any = Field(None, alias='extendedOfferEndTs', union_mode='left_to_right')
    content_segment: str | Any = Field(None, alias='contentSegment', union_mode='left_to_right')
    video_format: str | Any = Field(None, alias='videoFormat', union_mode='left_to_right')
    video_format_variant: str | Any = Field(None, alias='videoFormatVariant', union_mode='left_to_right')
    colour_space: str | Any = Field(None, alias='colourSpace', union_mode='left_to_right')
    free_offer_end_ts: int | Any = Field(None, alias='freeOfferEndTs', union_mode='left_to_right')
    streamable: bool | Any = Field(default=None, union_mode='left_to_right')
    downloadable: bool | Any = Field(default=None, union_mode='left_to_right')

class Markers(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    socr: int | Any = Field(None, alias='SOCR', union_mode='left_to_right')
    solc: int | Any = Field(None, alias='SOLC', union_mode='left_to_right')
    eolc: int | Any = Field(None, alias='EOLC', union_mode='left_to_right')

class Hd1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    audio_tracks: AudioTracks1 | Any = Field(None, alias='audioTracks', union_mode='left_to_right')
    chapter_markers: list[Any] | Any = Field(None, alias='chapterMarkers', union_mode='left_to_right')
    event_stage: str | Any = Field(None, alias='eventStage', union_mode='left_to_right')
    availability: Availability1 | Any = Field(default=None, union_mode='left_to_right')
    start_of_credits: int | Any = Field(None, alias='startOfCredits', union_mode='left_to_right')
    content_id: str | Any = Field(None, alias='contentId', union_mode='left_to_right')
    markers: Markers | Any = Field(default=None, union_mode='left_to_right')

class Formats1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hd: Hd1 | Any = Field(None, alias='HD', union_mode='left_to_right')

class Fact(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    fact_icon: str | Any = Field(None, alias='factIcon', union_mode='left_to_right')
    fact_text: str | Any = Field(None, alias='factText', union_mode='left_to_right')

class AlternativeDateItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    value: date | Any = Field(default=None, union_mode='left_to_right')
    date_type: str | Any = Field(None, alias='dateType', union_mode='left_to_right')
    territory: str | Any = Field(default=None, union_mode='left_to_right')

class Attributes1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    free_wheel_content_id: str | Any = Field(None, alias='FreeWheelContentID', union_mode='left_to_right')
    audience_level: list[AudienceLevelItem] | Any = Field(None, alias='audienceLevel', union_mode='left_to_right')
    audio_described: bool | Any = Field(None, alias='audioDescribed', union_mode='left_to_right')
    available_episode_count: int | Any = Field(None, alias='availableEpisodeCount', union_mode='left_to_right')
    available_season_count: int | Any = Field(None, alias='availableSeasonCount', union_mode='left_to_right')
    badging: Badging1 | Any = Field(default=None, union_mode='left_to_right')
    brands: list[str] | Any = Field(default=None, union_mode='left_to_right')
    cast: list[str] | Any = Field(default=None, union_mode='left_to_right')
    channel: Channel1 | Any = Field(default=None, union_mode='left_to_right')
    chapters_enabled: bool | Any = Field(None, alias='chaptersEnabled', union_mode='left_to_right')
    child_node_types: list[str] | Any = Field(None, alias='childNodeTypes', union_mode='left_to_right')
    classification: list[str] | Any = Field(default=None, union_mode='left_to_right')
    content_segments: list[str] | Any = Field(None, alias='contentSegments', union_mode='left_to_right')
    created_date: int | Any = Field(None, alias='createdDate', union_mode='left_to_right')
    desc_long_seo: str | Any = Field(None, alias='descLongSeo', union_mode='left_to_right')
    device_availabilities: list[DeviceAvailability2] | Any = Field(None, alias='deviceAvailabilities', union_mode='left_to_right')
    device_availability: DeviceAvailability3 | Any = Field(None, alias='deviceAvailability', union_mode='left_to_right')
    fan_critic_rating: list[FanCriticRatingItem1] | Any = Field(None, alias='fanCriticRating', union_mode='left_to_right')
    formats: Formats1 | Any = Field(default=None, union_mode='left_to_right')
    genre_details: list[GenreDetail] | Any = Field(None, alias='genreDetails', union_mode='left_to_right')
    genre_list: list[GenreListItem] | Any = Field(None, alias='genreList', union_mode='left_to_right')
    genres: list[str] | Any = Field(default=None, union_mode='left_to_right')
    gracenote_id: str | Any = Field(None, alias='gracenoteId', union_mode='left_to_right')
    gracenote_series_id: str | Any = Field(None, alias='gracenoteSeriesId', union_mode='left_to_right')
    images: list[Image] | Any = Field(default=None, union_mode='left_to_right')
    media_types: list[MediaType] | Any = Field(None, alias='mediaTypes', union_mode='left_to_right')
    merlin_id: str | Any = Field(None, alias='merlinId', union_mode='left_to_right')
    merlin_series_id: str | Any = Field(None, alias='merlinSeriesId', union_mode='left_to_right')
    nbcu_id: str | Any = Field(None, alias='nbcuId', union_mode='left_to_right')
    nbcu_series_id: str | Any = Field(None, alias='nbcuSeriesId', union_mode='left_to_right')
    ott_certificate: str | Any = Field(None, alias='ottCertificate', union_mode='left_to_right')
    provider_series_id: str | Any = Field(None, alias='providerSeriesId', union_mode='left_to_right')
    reverse_order: bool | Any = Field(None, alias='reverseOrder', union_mode='left_to_right')
    section_navigation: str | Any = Field(None, alias='sectionNavigation', union_mode='left_to_right')
    series_native_id: str | Any = Field(None, alias='seriesNativeId', union_mode='left_to_right')
    series_uuid: UUID | Any = Field(None, alias='seriesUuid', union_mode='left_to_right')
    slug: str | Any = Field(default=None, union_mode='left_to_right')
    smart_call_to_action: str | Any = Field(None, alias='smartCallToAction', union_mode='left_to_right')
    sort_title: str | Any = Field(None, alias='sortTitle', union_mode='left_to_right')
    synopsis_long: str | Any = Field(None, alias='synopsisLong', union_mode='left_to_right')
    synopsis_short: str | Any = Field(None, alias='synopsisShort', union_mode='left_to_right')
    target_audience: TargetAudience | Any = Field(None, alias='targetAudience', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    title_medium: str | Any = Field(None, alias='titleMedium', union_mode='left_to_right')
    title_seo: str | Any = Field(None, alias='titleSeo', union_mode='left_to_right')
    synopsis: str | Any = Field(default=None, union_mode='left_to_right')
    facts: list[Fact] | Any = Field(default=None, union_mode='left_to_right')
    title_medium_seo: str | Any = Field(None, alias='titleMediumSeo', union_mode='left_to_right')
    director: list[str] | Any = Field(default=None, union_mode='left_to_right')
    alternative_date: list[AlternativeDateItem] | Any = Field(None, alias='alternativeDate', union_mode='left_to_right')
    closed_captioned: bool | Any = Field(None, alias='closedCaptioned', union_mode='left_to_right')
    cwm: str | Any = Field(default=None, union_mode='left_to_right')
    duration_milliseconds: int | Any = Field(None, alias='durationMilliseconds', union_mode='left_to_right')
    duration_minutes: int | Any = Field(None, alias='durationMinutes', union_mode='left_to_right')
    duration_seconds: int | Any = Field(None, alias='durationSeconds', union_mode='left_to_right')
    main_original_language: str | Any = Field(None, alias='mainOriginalLanguage', union_mode='left_to_right')
    native_id: str | Any = Field(None, alias='nativeId', union_mode='left_to_right')
    producer: list[str] | Any = Field(default=None, union_mode='left_to_right')
    production_language: str | Any = Field(None, alias='productionLanguage', union_mode='left_to_right')
    programme_uuid: UUID | Any = Field(None, alias='programmeUuid', union_mode='left_to_right')
    provider_id: str | Any = Field(None, alias='providerId', union_mode='left_to_right')
    provider_variant_id: UUID | Any = Field(None, alias='providerVariantId', union_mode='left_to_right')
    rating: str | Any = Field(default=None, union_mode='left_to_right')
    rating_percentage: int | Any = Field(None, alias='ratingPercentage', union_mode='left_to_right')
    runtime: time | Any = Field(default=None, union_mode='left_to_right')
    subtitled: bool | Any = Field(default=None, union_mode='left_to_right')
    synopsis_brief: str | Any = Field(None, alias='synopsisBrief', union_mode='left_to_right')
    title_long: str | Any = Field(None, alias='titleLong', union_mode='left_to_right')
    year: int | Any = Field(default=None, union_mode='left_to_right')
    desc_short_seo: str | Any = Field(None, alias='descShortSeo', union_mode='left_to_right')

class Datum(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    links: Links | Any = Field(default=None, union_mode='left_to_right')
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    child_types: ChildTypes1 | Any = Field(None, alias='childTypes', union_mode='left_to_right')
    attributes: Attributes1 | Any = Field(default=None, union_mode='left_to_right')

class Recs(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    data: list[Datum] | Any = Field(default=None, union_mode='left_to_right')

class ChildTypes2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    images: Images | Any = Field(default=None, union_mode='left_to_right')
    items: Items | Any = Field(default=None, union_mode='left_to_right')

class Badging2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_formats: list[VideoFormat] | Any = Field(None, alias='videoFormats', union_mode='left_to_right')
    audio_tracks: list[str] | Any = Field(None, alias='audioTracks', union_mode='left_to_right')

class Channel2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    access_channel: str | Any = Field(None, alias='accessChannel', union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    logo_style: str | Any = Field(None, alias='logoStyle', union_mode='left_to_right')
    provider_id: str | Any = Field(None, alias='providerId', union_mode='left_to_right')
    logo: list[LogoItem] | Any = Field(default=None, union_mode='left_to_right')
    sections: list[str] | Any = Field(default=None, union_mode='left_to_right')
    logo_height_percentage: int | Any = Field(None, alias='logoHeightPercentage', union_mode='left_to_right')

class DeviceAvailability4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    format: str | Any = Field(default=None, union_mode='left_to_right')
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    offer_stage: str | Any = Field(None, alias='offerStage', union_mode='left_to_right')
    offer_start_ts: int | Any = Field(None, alias='offerStartTs', union_mode='left_to_right')
    offer_end_ts: int | Any = Field(None, alias='offerEndTs', union_mode='left_to_right')
    content_segment: str | Any = Field(None, alias='contentSegment', union_mode='left_to_right')
    video_format: str | Any = Field(None, alias='videoFormat', union_mode='left_to_right')
    video_format_variant: str | Any = Field(None, alias='videoFormatVariant', union_mode='left_to_right')
    colour_space: str | Any = Field(None, alias='colourSpace', union_mode='left_to_right')

class DeviceAvailability5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    available: bool | Any = Field(default=None, union_mode='left_to_right')

class FanCriticRatingItem2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | Any = Field(default=None, union_mode='left_to_right')
    fan_score: int | Any = Field(None, alias='fanScore', union_mode='left_to_right')
    critic_score: int | Any = Field(None, alias='criticScore', union_mode='left_to_right')

class AudioTracks2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    spa: list[str] | Any = Field(default=None, union_mode='left_to_right')
    eng: list[str] | Any = Field(default=None, union_mode='left_to_right')

class Availability2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    available: bool | Any = Field(default=None, union_mode='left_to_right')
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    offer_stage: str | Any = Field(None, alias='offerStage', union_mode='left_to_right')
    offer_start_ts: int | Any = Field(None, alias='offerStartTs', union_mode='left_to_right')
    offer_end_ts: int | Any = Field(None, alias='offerEndTs', union_mode='left_to_right')
    available_devices: list[AvailableDevice] | Any = Field(None, alias='availableDevices', union_mode='left_to_right')
    extended_offer_start_ts: int | Any = Field(None, alias='extendedOfferStartTs', union_mode='left_to_right')
    extended_offer_end_ts: int | Any = Field(None, alias='extendedOfferEndTs', union_mode='left_to_right')
    content_segment: str | Any = Field(None, alias='contentSegment', union_mode='left_to_right')
    video_format: str | Any = Field(None, alias='videoFormat', union_mode='left_to_right')
    video_format_variant: str | Any = Field(None, alias='videoFormatVariant', union_mode='left_to_right')
    colour_space: str | Any = Field(None, alias='colourSpace', union_mode='left_to_right')

class Hd2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    audio_tracks: AudioTracks2 | Any = Field(None, alias='audioTracks', union_mode='left_to_right')
    chapter_markers: list[Any] | Any = Field(None, alias='chapterMarkers', union_mode='left_to_right')
    event_stage: str | Any = Field(None, alias='eventStage', union_mode='left_to_right')
    availability: Availability2 | Any = Field(default=None, union_mode='left_to_right')
    start_of_credits: int | Any = Field(None, alias='startOfCredits', union_mode='left_to_right')

class Formats2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hd: Hd2 | Any = Field(None, alias='HD', union_mode='left_to_right')

class Attributes2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    free_wheel_content_id: str | Any = Field(None, alias='FreeWheelContentID', union_mode='left_to_right')
    audio_described: bool | Any = Field(None, alias='audioDescribed', union_mode='left_to_right')
    badging: Badging2 | Any = Field(default=None, union_mode='left_to_right')
    channel: Channel2 | Any = Field(default=None, union_mode='left_to_right')
    chapters_enabled: bool | Any = Field(None, alias='chaptersEnabled', union_mode='left_to_right')
    child_node_types: list[str] | Any = Field(None, alias='childNodeTypes', union_mode='left_to_right')
    classification: list[str] | Any = Field(default=None, union_mode='left_to_right')
    content_segments: list[str] | Any = Field(None, alias='contentSegments', union_mode='left_to_right')
    created_date: int | Any = Field(None, alias='createdDate', union_mode='left_to_right')
    desc_long_seo: str | Any = Field(None, alias='descLongSeo', union_mode='left_to_right')
    device_availabilities: list[DeviceAvailability4] | Any = Field(None, alias='deviceAvailabilities', union_mode='left_to_right')
    device_availability: DeviceAvailability5 | Any = Field(None, alias='deviceAvailability', union_mode='left_to_right')
    fan_critic_rating: list[FanCriticRatingItem2] | Any = Field(None, alias='fanCriticRating', union_mode='left_to_right')
    formats: Formats2 | Any = Field(default=None, union_mode='left_to_right')
    genre_list: list[GenreListItem] | Any = Field(None, alias='genreList', union_mode='left_to_right')
    genres: list[str] | Any = Field(default=None, union_mode='left_to_right')
    gracenote_id: str | Any = Field(None, alias='gracenoteId', union_mode='left_to_right')
    gracenote_series_id: str | Any = Field(None, alias='gracenoteSeriesId', union_mode='left_to_right')
    images: list[Image] | Any = Field(default=None, union_mode='left_to_right')
    merlin_id: str | Any = Field(None, alias='merlinId', union_mode='left_to_right')
    merlin_series_id: str | Any = Field(None, alias='merlinSeriesId', union_mode='left_to_right')
    nbcu_id: str | Any = Field(None, alias='nbcuId', union_mode='left_to_right')
    nbcu_series_id: str | Any = Field(None, alias='nbcuSeriesId', union_mode='left_to_right')
    provider_season_id: str | Any = Field(None, alias='providerSeasonId', union_mode='left_to_right')
    provider_series_id: str | Any = Field(None, alias='providerSeriesId', union_mode='left_to_right')
    season_number: int | Any = Field(None, alias='seasonNumber', union_mode='left_to_right')
    season_uuid: UUID | Any = Field(None, alias='seasonUuid', union_mode='left_to_right')
    section_navigation: str | Any = Field(None, alias='sectionNavigation', union_mode='left_to_right')
    series_id: UUID | Any = Field(None, alias='seriesId', union_mode='left_to_right')
    series_name: str | Any = Field(None, alias='seriesName', union_mode='left_to_right')
    series_native_id: str | Any = Field(None, alias='seriesNativeId', union_mode='left_to_right')
    slug: str | Any = Field(default=None, union_mode='left_to_right')
    sort_title: str | Any = Field(None, alias='sortTitle', union_mode='left_to_right')
    synopsis_long: str | Any = Field(None, alias='synopsisLong', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    title_medium: str | Any = Field(None, alias='titleMedium', union_mode='left_to_right')
    title_seo: str | Any = Field(None, alias='titleSeo', union_mode='left_to_right')
    genre_details: list[GenreDetail] | Any = Field(None, alias='genreDetails', union_mode='left_to_right')
    synopsis_short: str | Any = Field(None, alias='synopsisShort', union_mode='left_to_right')
    title_medium_seo: str | Any = Field(None, alias='titleMediumSeo', union_mode='left_to_right')

class ChildTypes3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    images: Images | Any = Field(default=None, union_mode='left_to_right')

class Term(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    description: str | Any = Field(default=None, union_mode='left_to_right')
    abbreviation: str | Any = Field(default=None, union_mode='left_to_right')

class AdvisoryItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    terms: list[Term] | Any = Field(default=None, union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    group: int | Any = Field(default=None, union_mode='left_to_right')

class Badging3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_formats: list[VideoFormat] | Any = Field(None, alias='videoFormats', union_mode='left_to_right')
    audio_tracks: list[str] | Any = Field(None, alias='audioTracks', union_mode='left_to_right')

class Channel3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    access_channel: str | Any = Field(None, alias='accessChannel', union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    logo_style: str | Any = Field(None, alias='logoStyle', union_mode='left_to_right')
    provider_id: str | Any = Field(None, alias='providerId', union_mode='left_to_right')
    logo: list[LogoItem] | Any = Field(default=None, union_mode='left_to_right')
    sections: list[str] | Any = Field(default=None, union_mode='left_to_right')
    logo_height_percentage: int | Any = Field(None, alias='logoHeightPercentage', union_mode='left_to_right')

class DeviceAvailability6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    format: str | Any = Field(default=None, union_mode='left_to_right')
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    offer_stage: str | Any = Field(None, alias='offerStage', union_mode='left_to_right')
    offer_start_ts: int | Any = Field(None, alias='offerStartTs', union_mode='left_to_right')
    offer_end_ts: int | Any = Field(None, alias='offerEndTs', union_mode='left_to_right')
    streamable: bool | Any = Field(default=None, union_mode='left_to_right')
    downloadable: bool | Any = Field(default=None, union_mode='left_to_right')
    content_segment: str | Any = Field(None, alias='contentSegment', union_mode='left_to_right')
    video_format: str | Any = Field(None, alias='videoFormat', union_mode='left_to_right')
    video_format_variant: str | Any = Field(None, alias='videoFormatVariant', union_mode='left_to_right')
    colour_space: str | Any = Field(None, alias='colourSpace', union_mode='left_to_right')

class DeviceAvailability7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    available: bool | Any = Field(default=None, union_mode='left_to_right')

class Availability3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    available: bool | Any = Field(default=None, union_mode='left_to_right')
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    offer_stage: str | Any = Field(None, alias='offerStage', union_mode='left_to_right')
    offer_start_ts: int | Any = Field(None, alias='offerStartTs', union_mode='left_to_right')
    offer_end_ts: int | Any = Field(None, alias='offerEndTs', union_mode='left_to_right')
    streamable: bool | Any = Field(default=None, union_mode='left_to_right')
    downloadable: bool | Any = Field(default=None, union_mode='left_to_right')
    available_devices: list[AvailableDevice] | Any = Field(None, alias='availableDevices', union_mode='left_to_right')
    extended_offer_start_ts: int | Any = Field(None, alias='extendedOfferStartTs', union_mode='left_to_right')
    extended_offer_end_ts: int | Any = Field(None, alias='extendedOfferEndTs', union_mode='left_to_right')
    content_segment: str | Any = Field(None, alias='contentSegment', union_mode='left_to_right')
    video_format: str | Any = Field(None, alias='videoFormat', union_mode='left_to_right')
    video_format_variant: str | Any = Field(None, alias='videoFormatVariant', union_mode='left_to_right')
    colour_space: str | Any = Field(None, alias='colourSpace', union_mode='left_to_right')

class Markers1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    socr: int | Any = Field(None, alias='SOCR', union_mode='left_to_right')
    soi: int | Any = Field(None, alias='SOI', union_mode='left_to_right')
    hsi: int | Any = Field(None, alias='HSI', union_mode='left_to_right')
    spi: int | Any = Field(None, alias='SPI', union_mode='left_to_right')
    solc: int | Any = Field(None, alias='SOLC', union_mode='left_to_right')
    eolc: int | Any = Field(None, alias='EOLC', union_mode='left_to_right')
    sor: int | Any = Field(None, alias='SOR', union_mode='left_to_right')
    hsr: int | Any = Field(None, alias='HSR', union_mode='left_to_right')
    spr: int | Any = Field(None, alias='SPR', union_mode='left_to_right')

class Hd3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    audio_tracks: AudioTracks2 | Any = Field(None, alias='audioTracks', union_mode='left_to_right')
    chapter_markers: list[Any] | Any = Field(None, alias='chapterMarkers', union_mode='left_to_right')
    event_stage: str | Any = Field(None, alias='eventStage', union_mode='left_to_right')
    content_id: str | Any = Field(None, alias='contentId', union_mode='left_to_right')
    availability: Availability3 | Any = Field(default=None, union_mode='left_to_right')
    start_of_credits: int | Any = Field(None, alias='startOfCredits', union_mode='left_to_right')
    markers: Markers1 | Any = Field(default=None, union_mode='left_to_right')

class Formats3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hd: Hd3 | Any = Field(None, alias='HD', union_mode='left_to_right')

class Attributes3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    free_wheel_content_id: str | Any = Field(None, alias='FreeWheelContentID', union_mode='left_to_right')
    advisory: list[AdvisoryItem] | Any = Field(default=None, union_mode='left_to_right')
    audio_described: bool | Any = Field(None, alias='audioDescribed', union_mode='left_to_right')
    badging: Badging3 | Any = Field(default=None, union_mode='left_to_right')
    channel: Channel3 | Any = Field(default=None, union_mode='left_to_right')
    chapters_enabled: bool | Any = Field(None, alias='chaptersEnabled', union_mode='left_to_right')
    child_node_types: list[str] | Any = Field(None, alias='childNodeTypes', union_mode='left_to_right')
    classification: list[str] | Any = Field(default=None, union_mode='left_to_right')
    closed_captioned: bool | Any = Field(None, alias='closedCaptioned', union_mode='left_to_right')
    content_segments: list[str] | Any = Field(None, alias='contentSegments', union_mode='left_to_right')
    created_date: int | Any = Field(None, alias='createdDate', union_mode='left_to_right')
    cwm: str | Any = Field(default=None, union_mode='left_to_right')
    desc_long_seo: str | Any = Field(None, alias='descLongSeo', union_mode='left_to_right')
    device_availabilities: list[DeviceAvailability6] | Any = Field(None, alias='deviceAvailabilities', union_mode='left_to_right')
    device_availability: DeviceAvailability7 | Any = Field(None, alias='deviceAvailability', union_mode='left_to_right')
    duration_milliseconds: int | Any = Field(None, alias='durationMilliseconds', union_mode='left_to_right')
    duration_minutes: int | Any = Field(None, alias='durationMinutes', union_mode='left_to_right')
    duration_seconds: int | Any = Field(None, alias='durationSeconds', union_mode='left_to_right')
    episode_name: str | Any = Field(None, alias='episodeName', union_mode='left_to_right')
    episode_name_long: str | Any = Field(None, alias='episodeNameLong', union_mode='left_to_right')
    episode_number: int | Any = Field(None, alias='episodeNumber', union_mode='left_to_right')
    formats: Formats3 | Any = Field(default=None, union_mode='left_to_right')
    genre_list: list[GenreListItem] | Any = Field(None, alias='genreList', union_mode='left_to_right')
    genres: list[str] | Any = Field(default=None, union_mode='left_to_right')
    gracenote_id: str | Any = Field(None, alias='gracenoteId', union_mode='left_to_right')
    gracenote_series_id: str | Any = Field(None, alias='gracenoteSeriesId', union_mode='left_to_right')
    images: list[Image] | Any = Field(default=None, union_mode='left_to_right')
    last_in_season: bool | Any = Field(None, alias='lastInSeason', union_mode='left_to_right')
    main_original_language: str | Any = Field(None, alias='mainOriginalLanguage', union_mode='left_to_right')
    merlin_id: str | Any = Field(None, alias='merlinId', union_mode='left_to_right')
    merlin_series_id: str | Any = Field(None, alias='merlinSeriesId', union_mode='left_to_right')
    nbcu_id: str | Any = Field(None, alias='nbcuId', union_mode='left_to_right')
    nbcu_series_id: str | Any = Field(None, alias='nbcuSeriesId', union_mode='left_to_right')
    ott_certificate: str | Any = Field(None, alias='ottCertificate', union_mode='left_to_right')
    production_language: str | Any = Field(None, alias='productionLanguage', union_mode='left_to_right')
    programme_uuid: UUID | Any = Field(None, alias='programmeUuid', union_mode='left_to_right')
    provider_id: str | Any = Field(None, alias='providerId', union_mode='left_to_right')
    provider_season_id: str | Any = Field(None, alias='providerSeasonId', union_mode='left_to_right')
    provider_series_id: str | Any = Field(None, alias='providerSeriesId', union_mode='left_to_right')
    provider_variant_id: UUID | Any = Field(None, alias='providerVariantId', union_mode='left_to_right')
    runtime: time | Any = Field(default=None, union_mode='left_to_right')
    season_id: UUID | Any = Field(None, alias='seasonId', union_mode='left_to_right')
    season_number: int | Any = Field(None, alias='seasonNumber', union_mode='left_to_right')
    section_navigation: str | Any = Field(None, alias='sectionNavigation', union_mode='left_to_right')
    series_id: UUID | Any = Field(None, alias='seriesId', union_mode='left_to_right')
    series_name: str | Any = Field(None, alias='seriesName', union_mode='left_to_right')
    series_native_id: str | Any = Field(None, alias='seriesNativeId', union_mode='left_to_right')
    slug: str | Any = Field(default=None, union_mode='left_to_right')
    sort_title: str | Any = Field(None, alias='sortTitle', union_mode='left_to_right')
    subtitled: bool | Any = Field(default=None, union_mode='left_to_right')
    synopsis: str | Any = Field(default=None, union_mode='left_to_right')
    synopsis_brief: str | Any = Field(None, alias='synopsisBrief', union_mode='left_to_right')
    synopsis_long: str | Any = Field(None, alias='synopsisLong', union_mode='left_to_right')
    synopsis_short: str | Any = Field(None, alias='synopsisShort', union_mode='left_to_right')
    target_audience: TargetAudience | Any = Field(None, alias='targetAudience', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    title_long: str | Any = Field(None, alias='titleLong', union_mode='left_to_right')
    title_medium: str | Any = Field(None, alias='titleMedium', union_mode='left_to_right')
    title_seo: str | Any = Field(None, alias='titleSeo', union_mode='left_to_right')
    year: int | Any = Field(default=None, union_mode='left_to_right')
    cast: list[str] | Any = Field(default=None, union_mode='left_to_right')
    editorial_warning_text: str | Any = Field(None, alias='editorialWarningText', union_mode='left_to_right')
    genre_details: list[GenreDetail] | Any = Field(None, alias='genreDetails', union_mode='left_to_right')
    merlin_alternate_id: str | Any = Field(None, alias='merlinAlternateId', union_mode='left_to_right')

class Datum2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    links: Links | Any = Field(default=None, union_mode='left_to_right')
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    child_types: ChildTypes3 | Any = Field(None, alias='childTypes', union_mode='left_to_right')
    attributes: Attributes3 | Any = Field(default=None, union_mode='left_to_right')

class Items4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    data: list[Datum2] | Any = Field(default=None, union_mode='left_to_right')

class Relationships1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    items: Items4 | Any = Field(default=None, union_mode='left_to_right')

class Datum1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    links: Links | Any = Field(default=None, union_mode='left_to_right')
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    child_types: ChildTypes2 | Any = Field(None, alias='childTypes', union_mode='left_to_right')
    attributes: Attributes2 | Any = Field(default=None, union_mode='left_to_right')
    relationships: Relationships1 | Any = Field(default=None, union_mode='left_to_right')

class Items2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    data: list[Datum1] | Any = Field(default=None, union_mode='left_to_right')

class ChildTypes4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    images: Images | Any = Field(default=None, union_mode='left_to_right')

class AdvisoryItem1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    terms: list[Term] | Any = Field(default=None, union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    group: int | Any = Field(default=None, union_mode='left_to_right')

class Badging4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_formats: list[VideoFormat] | Any = Field(None, alias='videoFormats', union_mode='left_to_right')
    audio_tracks: list[str] | Any = Field(None, alias='audioTracks', union_mode='left_to_right')

class Channel4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    access_channel: str | Any = Field(None, alias='accessChannel', union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')

class DeviceAvailability8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    format: str | Any = Field(default=None, union_mode='left_to_right')
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    offer_stage: str | Any = Field(None, alias='offerStage', union_mode='left_to_right')
    offer_start_ts: int | Any = Field(None, alias='offerStartTs', union_mode='left_to_right')
    offer_end_ts: int | Any = Field(None, alias='offerEndTs', union_mode='left_to_right')
    streamable: bool | Any = Field(default=None, union_mode='left_to_right')
    downloadable: bool | Any = Field(default=None, union_mode='left_to_right')
    content_segment: str | Any = Field(None, alias='contentSegment', union_mode='left_to_right')
    video_format: str | Any = Field(None, alias='videoFormat', union_mode='left_to_right')
    video_format_variant: str | Any = Field(None, alias='videoFormatVariant', union_mode='left_to_right')
    colour_space: str | Any = Field(None, alias='colourSpace', union_mode='left_to_right')

class DeviceAvailability9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    available: bool | Any = Field(default=None, union_mode='left_to_right')

class AudioTracks4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    eng: list[str] | Any = Field(default=None, union_mode='left_to_right')

class Availability4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    available: bool | Any = Field(default=None, union_mode='left_to_right')
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    offer_stage: str | Any = Field(None, alias='offerStage', union_mode='left_to_right')
    offer_start_ts: int | Any = Field(None, alias='offerStartTs', union_mode='left_to_right')
    offer_end_ts: int | Any = Field(None, alias='offerEndTs', union_mode='left_to_right')
    streamable: bool | Any = Field(default=None, union_mode='left_to_right')
    downloadable: bool | Any = Field(default=None, union_mode='left_to_right')
    available_devices: list[AvailableDevice] | Any = Field(None, alias='availableDevices', union_mode='left_to_right')
    extended_offer_start_ts: int | Any = Field(None, alias='extendedOfferStartTs', union_mode='left_to_right')
    extended_offer_end_ts: int | Any = Field(None, alias='extendedOfferEndTs', union_mode='left_to_right')
    content_segment: str | Any = Field(None, alias='contentSegment', union_mode='left_to_right')
    video_format: str | Any = Field(None, alias='videoFormat', union_mode='left_to_right')
    video_format_variant: str | Any = Field(None, alias='videoFormatVariant', union_mode='left_to_right')
    colour_space: str | Any = Field(None, alias='colourSpace', union_mode='left_to_right')

class Hd4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    audio_tracks: AudioTracks4 | Any = Field(None, alias='audioTracks', union_mode='left_to_right')
    chapter_markers: list[Any] | Any = Field(None, alias='chapterMarkers', union_mode='left_to_right')
    event_stage: str | Any = Field(None, alias='eventStage', union_mode='left_to_right')
    content_id: str | Any = Field(None, alias='contentId', union_mode='left_to_right')
    availability: Availability4 | Any = Field(default=None, union_mode='left_to_right')
    start_of_credits: int | Any = Field(None, alias='startOfCredits', union_mode='left_to_right')

class Formats4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hd: Hd4 | Any = Field(None, alias='HD', union_mode='left_to_right')

class LinkedEpisode(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    node_id: UUID | Any = Field(None, alias='nodeId', union_mode='left_to_right')
    content_id: str | Any = Field(None, alias='contentId', union_mode='left_to_right')
    provider_variant_id: UUID | Any = Field(None, alias='providerVariantId', union_mode='left_to_right')
    format: str | Any = Field(default=None, union_mode='left_to_right')

class MainTitleInfoItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    node_id: UUID | Any = Field(None, alias='nodeId', union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    series_uuid: UUID | Any = Field(None, alias='seriesUuid', union_mode='left_to_right')
    provider_series_id: str | Any = Field(None, alias='providerSeriesId', union_mode='left_to_right')
    linked_episodes: list[LinkedEpisode] | Any = Field(None, alias='linkedEpisodes', union_mode='left_to_right')
    content_segments: list[str] | Any = Field(None, alias='contentSegments', union_mode='left_to_right')

class Attributes4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    free_wheel_content_id: str | Any = Field(None, alias='FreeWheelContentID', union_mode='left_to_right')
    advisory: list[AdvisoryItem1] | Any = Field(default=None, union_mode='left_to_right')
    audio_described: bool | Any = Field(None, alias='audioDescribed', union_mode='left_to_right')
    autoplay: bool | Any = Field(default=None, union_mode='left_to_right')
    badging: Badging4 | Any = Field(default=None, union_mode='left_to_right')
    channel: Channel4 | Any = Field(default=None, union_mode='left_to_right')
    chapters_enabled: bool | Any = Field(None, alias='chaptersEnabled', union_mode='left_to_right')
    child_node_types: list[str] | Any = Field(None, alias='childNodeTypes', union_mode='left_to_right')
    classification: list[str] | Any = Field(default=None, union_mode='left_to_right')
    closed_captioned: bool | Any = Field(None, alias='closedCaptioned', union_mode='left_to_right')
    content_segments: list[str] | Any = Field(None, alias='contentSegments', union_mode='left_to_right')
    created_date: int | Any = Field(None, alias='createdDate', union_mode='left_to_right')
    cwm: str | Any = Field(default=None, union_mode='left_to_right')
    device_availabilities: list[DeviceAvailability8] | Any = Field(None, alias='deviceAvailabilities', union_mode='left_to_right')
    device_availability: DeviceAvailability9 | Any = Field(None, alias='deviceAvailability', union_mode='left_to_right')
    duration_milliseconds: int | Any = Field(None, alias='durationMilliseconds', union_mode='left_to_right')
    duration_minutes: int | Any = Field(None, alias='durationMinutes', union_mode='left_to_right')
    duration_seconds: int | Any = Field(None, alias='durationSeconds', union_mode='left_to_right')
    formats: Formats4 | Any = Field(default=None, union_mode='left_to_right')
    free_wheel_creative_id: str | Any = Field(None, alias='freeWheelCreativeId', union_mode='left_to_right')
    genre_list: list[GenreListItem] | Any = Field(None, alias='genreList', union_mode='left_to_right')
    genres: list[str] | Any = Field(default=None, union_mode='left_to_right')
    images: list[Image] | Any = Field(default=None, union_mode='left_to_right')
    main_title_info: list[MainTitleInfoItem] | Any = Field(None, alias='mainTitleInfo', union_mode='left_to_right')
    merlin_id: str | Any = Field(None, alias='merlinId', union_mode='left_to_right')
    nbcu_id: str | Any = Field(None, alias='nbcuId', union_mode='left_to_right')
    ott_certificate: str | Any = Field(None, alias='ottCertificate', union_mode='left_to_right')
    provider_id: str | Any = Field(None, alias='providerId', union_mode='left_to_right')
    provider_variant_id: UUID | Any = Field(None, alias='providerVariantId', union_mode='left_to_right')
    runtime: time | Any = Field(default=None, union_mode='left_to_right')
    series_uuid: UUID | Any = Field(None, alias='seriesUuid', union_mode='left_to_right')
    slug: str | Any = Field(default=None, union_mode='left_to_right')
    synopsis_long: str | Any = Field(None, alias='synopsisLong', union_mode='left_to_right')
    synopsis_short: str | Any = Field(None, alias='synopsisShort', union_mode='left_to_right')
    target_audience: TargetAudience | Any = Field(None, alias='targetAudience', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    title_long: str | Any = Field(None, alias='titleLong', union_mode='left_to_right')
    title_medium: str | Any = Field(None, alias='titleMedium', union_mode='left_to_right')

class Datum3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    links: Links | Any = Field(default=None, union_mode='left_to_right')
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    child_types: ChildTypes4 | Any = Field(None, alias='childTypes', union_mode='left_to_right')
    attributes: Attributes4 | Any = Field(default=None, union_mode='left_to_right')

class Trailers2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    data: list[Datum3] | Any = Field(default=None, union_mode='left_to_right')

class Items5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    node_types: list[str] | Any = Field(None, alias='nodeTypes', union_mode='left_to_right')
    count: int | Any = Field(default=None, union_mode='left_to_right')

class ChildTypes5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    items: Items5 | Any = Field(default=None, union_mode='left_to_right')

class RenderHint(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group_template: str | Any = Field(None, alias='groupTemplate', union_mode='left_to_right')

class Attributes5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    alias: str | Any = Field(default=None, union_mode='left_to_right')
    child_node_types: list[str] | Any = Field(None, alias='childNodeTypes', union_mode='left_to_right')
    created_date: int | Any = Field(None, alias='createdDate', union_mode='left_to_right')
    render_hint: RenderHint | Any = Field(None, alias='renderHint', union_mode='left_to_right')
    section_navigation: str | Any = Field(None, alias='sectionNavigation', union_mode='left_to_right')
    slug: str | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')

class CurationConfig(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    node_types: list[str] | Any = Field(None, alias='nodeTypes', union_mode='left_to_right')
    count: int | Any = Field(default=None, union_mode='left_to_right')

class ChildTypes6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    items: Items5 | Any = Field(default=None, union_mode='left_to_right')
    curation_config: CurationConfig | Any = Field(None, alias='curation-config', union_mode='left_to_right')

class RenderHint1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    orientation: str | Any = Field(default=None, union_mode='left_to_right')
    sort: str | Any = Field(default=None, union_mode='left_to_right')
    view_all: str | Any = Field(None, alias='viewAll', union_mode='left_to_right')
    image_template: str | Any = Field(None, alias='imageTemplate', union_mode='left_to_right')

class Attributes6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    child_node_types: list[str] | Any = Field(None, alias='childNodeTypes', union_mode='left_to_right')
    collection_type: str | Any = Field(None, alias='collectionType', union_mode='left_to_right')
    content_level: str | Any = Field(None, alias='contentLevel', union_mode='left_to_right')
    created_date: int | Any = Field(None, alias='createdDate', union_mode='left_to_right')
    items_count: int | Any = Field(None, alias='itemsCount', union_mode='left_to_right')
    keep_if_empty: bool | Any = Field(None, alias='keepIfEmpty', union_mode='left_to_right')
    orientation: str | Any = Field(default=None, union_mode='left_to_right')
    rail_title_type: str | Any = Field(None, alias='railTitleType', union_mode='left_to_right')
    refresh_policy: str | Any = Field(None, alias='refreshPolicy', union_mode='left_to_right')
    render_hint: RenderHint1 | Any = Field(None, alias='renderHint', union_mode='left_to_right')
    section_navigation: str | Any = Field(None, alias='sectionNavigation', union_mode='left_to_right')
    slug: str | Any = Field(default=None, union_mode='left_to_right')
    sort_policy: str | Any = Field(None, alias='sortPolicy', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')

class ChildTypes7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    images: Images | Any = Field(default=None, union_mode='left_to_right')
    items: Items5 | Any = Field(default=None, union_mode='left_to_right')
    curation_config: CurationConfig | Any = Field(None, alias='curation-config', union_mode='left_to_right')

class Image5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')

class RenderHint2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    orientation: str | Any = Field(default=None, union_mode='left_to_right')
    autoplay: str | Any = Field(default=None, union_mode='left_to_right')
    sort: str | Any = Field(default=None, union_mode='left_to_right')
    image_template: str | Any = Field(None, alias='imageTemplate', union_mode='left_to_right')

class Badging5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    video_formats: list[VideoFormat] | Any = Field(None, alias='videoFormats', union_mode='left_to_right')
    audio_tracks: list[str] | Any = Field(None, alias='audioTracks', union_mode='left_to_right')

class Channel5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    access_channel: str | Any = Field(None, alias='accessChannel', union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    logo_style: str | Any = Field(None, alias='logoStyle', union_mode='left_to_right')
    provider_id: str | Any = Field(None, alias='providerId', union_mode='left_to_right')
    logo: list[LogoItem] | Any = Field(default=None, union_mode='left_to_right')
    sections: list[str] | Any = Field(default=None, union_mode='left_to_right')
    logo_height_percentage: int | Any = Field(None, alias='logoHeightPercentage', union_mode='left_to_right')

class DeviceAvailability10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    format: str | Any = Field(default=None, union_mode='left_to_right')
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    offer_stage: str | Any = Field(None, alias='offerStage', union_mode='left_to_right')
    offer_start_ts: int | Any = Field(None, alias='offerStartTs', union_mode='left_to_right')
    offer_end_ts: int | Any = Field(None, alias='offerEndTs', union_mode='left_to_right')
    streamable: bool | Any = Field(default=None, union_mode='left_to_right')
    downloadable: bool | Any = Field(default=None, union_mode='left_to_right')
    content_segment: str | Any = Field(None, alias='contentSegment', union_mode='left_to_right')
    video_format: str | Any = Field(None, alias='videoFormat', union_mode='left_to_right')
    video_format_variant: str | Any = Field(None, alias='videoFormatVariant', union_mode='left_to_right')
    colour_space: str | Any = Field(None, alias='colourSpace', union_mode='left_to_right')

class DeviceAvailability11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    available: bool | Any = Field(default=None, union_mode='left_to_right')

class AudioTracks5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    eng: list[str] | Any = Field(default=None, union_mode='left_to_right')
    spa: list[str] | Any = Field(default=None, union_mode='left_to_right')

class Availability5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    available: bool | Any = Field(default=None, union_mode='left_to_right')
    media_type: str | Any = Field(None, alias='mediaType', union_mode='left_to_right')
    offer_stage: str | Any = Field(None, alias='offerStage', union_mode='left_to_right')
    offer_start_ts: int | Any = Field(None, alias='offerStartTs', union_mode='left_to_right')
    offer_end_ts: int | Any = Field(None, alias='offerEndTs', union_mode='left_to_right')
    streamable: bool | Any = Field(default=None, union_mode='left_to_right')
    downloadable: bool | Any = Field(default=None, union_mode='left_to_right')
    available_devices: list[AvailableDevice] | Any = Field(None, alias='availableDevices', union_mode='left_to_right')
    extended_offer_start_ts: int | Any = Field(None, alias='extendedOfferStartTs', union_mode='left_to_right')
    extended_offer_end_ts: int | Any = Field(None, alias='extendedOfferEndTs', union_mode='left_to_right')
    content_segment: str | Any = Field(None, alias='contentSegment', union_mode='left_to_right')
    video_format: str | Any = Field(None, alias='videoFormat', union_mode='left_to_right')
    video_format_variant: str | Any = Field(None, alias='videoFormatVariant', union_mode='left_to_right')
    colour_space: str | Any = Field(None, alias='colourSpace', union_mode='left_to_right')

class Markers2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    socr: int | Any = Field(None, alias='SOCR', union_mode='left_to_right')
    soi: int | Any = Field(None, alias='SOI', union_mode='left_to_right')
    hsi: int | Any = Field(None, alias='HSI', union_mode='left_to_right')
    spi: int | Any = Field(None, alias='SPI', union_mode='left_to_right')

class Hd5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    audio_tracks: AudioTracks5 | Any = Field(None, alias='audioTracks', union_mode='left_to_right')
    chapter_markers: list[Any] | Any = Field(None, alias='chapterMarkers', union_mode='left_to_right')
    event_stage: str | Any = Field(None, alias='eventStage', union_mode='left_to_right')
    content_id: str | Any = Field(None, alias='contentId', union_mode='left_to_right')
    availability: Availability5 | Any = Field(default=None, union_mode='left_to_right')
    start_of_credits: int | Any = Field(None, alias='startOfCredits', union_mode='left_to_right')
    markers: Markers2 | Any = Field(default=None, union_mode='left_to_right')

class Formats5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hd: Hd5 | Any = Field(None, alias='HD', union_mode='left_to_right')

class AdvisoryItem2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    terms: list[Term] | Any = Field(default=None, union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    group: int | Any = Field(default=None, union_mode='left_to_right')

class Attributes7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    child_node_types: list[str] | Any = Field(None, alias='childNodeTypes', union_mode='left_to_right')
    collection_type: str | Any = Field(None, alias='collectionType', union_mode='left_to_right')
    content_level: str | Any = Field(None, alias='contentLevel', union_mode='left_to_right')
    created_date: int | Any = Field(None, alias='createdDate', union_mode='left_to_right')
    image_url: str | Any = Field(None, alias='imageUrl', union_mode='left_to_right')
    images: list[Image5] | Any = Field(default=None, union_mode='left_to_right')
    items_count: int | Any = Field(None, alias='itemsCount', union_mode='left_to_right')
    keep_if_empty: bool | Any = Field(None, alias='keepIfEmpty', union_mode='left_to_right')
    orientation: str | Any = Field(default=None, union_mode='left_to_right')
    promoted_item: bool | Any = Field(None, alias='promotedItem', union_mode='left_to_right')
    rail_title_type: str | Any = Field(None, alias='railTitleType', union_mode='left_to_right')
    refresh_policy: str | Any = Field(None, alias='refreshPolicy', union_mode='left_to_right')
    render_hint: RenderHint2 | Any = Field(None, alias='renderHint', union_mode='left_to_right')
    section_navigation: str | Any = Field(None, alias='sectionNavigation', union_mode='left_to_right')
    slug: str | Any = Field(default=None, union_mode='left_to_right')
    sort_policy: str | Any = Field(None, alias='sortPolicy', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    free_wheel_content_id: str | Any = Field(None, alias='FreeWheelContentID', union_mode='left_to_right')
    audio_described: bool | Any = Field(None, alias='audioDescribed', union_mode='left_to_right')
    badging: Badging5 | Any = Field(default=None, union_mode='left_to_right')
    channel: Channel5 | Any = Field(default=None, union_mode='left_to_right')
    chapters_enabled: bool | Any = Field(None, alias='chaptersEnabled', union_mode='left_to_right')
    classification: list[str] | Any = Field(default=None, union_mode='left_to_right')
    closed_captioned: bool | Any = Field(None, alias='closedCaptioned', union_mode='left_to_right')
    content_segments: list[str] | Any = Field(None, alias='contentSegments', union_mode='left_to_right')
    device_availabilities: list[DeviceAvailability10] | Any = Field(None, alias='deviceAvailabilities', union_mode='left_to_right')
    device_availability: DeviceAvailability11 | Any = Field(None, alias='deviceAvailability', union_mode='left_to_right')
    duration_milliseconds: int | Any = Field(None, alias='durationMilliseconds', union_mode='left_to_right')
    duration_minutes: int | Any = Field(None, alias='durationMinutes', union_mode='left_to_right')
    duration_seconds: int | Any = Field(None, alias='durationSeconds', union_mode='left_to_right')
    formats: Formats5 | Any = Field(default=None, union_mode='left_to_right')
    free_wheel_creative_id: str | Any = Field(None, alias='freeWheelCreativeId', union_mode='left_to_right')
    genre_list: list[GenreListItem] | Any = Field(None, alias='genreList', union_mode='left_to_right')
    genres: list[str] | Any = Field(default=None, union_mode='left_to_right')
    merlin_id: str | Any = Field(None, alias='merlinId', union_mode='left_to_right')
    nbcu_id: str | Any = Field(None, alias='nbcuId', union_mode='left_to_right')
    ott_certificate: str | Any = Field(None, alias='ottCertificate', union_mode='left_to_right')
    programme_uuid: UUID | Any = Field(None, alias='programmeUuid', union_mode='left_to_right')
    provider_id: str | Any = Field(None, alias='providerId', union_mode='left_to_right')
    provider_variant_id: UUID | Any = Field(None, alias='providerVariantId', union_mode='left_to_right')
    runtime: time | Any = Field(default=None, union_mode='left_to_right')
    synopsis_long: str | Any = Field(None, alias='synopsisLong', union_mode='left_to_right')
    synopsis_short: str | Any = Field(None, alias='synopsisShort', union_mode='left_to_right')
    target_audience: TargetAudience | Any = Field(None, alias='targetAudience', union_mode='left_to_right')
    title_long: str | Any = Field(None, alias='titleLong', union_mode='left_to_right')
    title_medium: str | Any = Field(None, alias='titleMedium', union_mode='left_to_right')
    alternative_date: list[AlternativeDateItem] | Any = Field(None, alias='alternativeDate', union_mode='left_to_right')
    uriid: str | Any = Field(default=None, union_mode='left_to_right')
    cast: list[str] | Any = Field(default=None, union_mode='left_to_right')
    cwm: str | Any = Field(default=None, union_mode='left_to_right')
    desc_long_seo: str | Any = Field(None, alias='descLongSeo', union_mode='left_to_right')
    editorial_warning_text: str | Any = Field(None, alias='editorialWarningText', union_mode='left_to_right')
    episode_name: str | Any = Field(None, alias='episodeName', union_mode='left_to_right')
    episode_name_long: str | Any = Field(None, alias='episodeNameLong', union_mode='left_to_right')
    episode_number: int | Any = Field(None, alias='episodeNumber', union_mode='left_to_right')
    genre_details: list[GenreDetail] | Any = Field(None, alias='genreDetails', union_mode='left_to_right')
    gracenote_id: str | Any = Field(None, alias='gracenoteId', union_mode='left_to_right')
    gracenote_series_id: str | Any = Field(None, alias='gracenoteSeriesId', union_mode='left_to_right')
    last_in_season: bool | Any = Field(None, alias='lastInSeason', union_mode='left_to_right')
    main_original_language: str | Any = Field(None, alias='mainOriginalLanguage', union_mode='left_to_right')
    merlin_alternate_id: str | Any = Field(None, alias='merlinAlternateId', union_mode='left_to_right')
    merlin_series_id: str | Any = Field(None, alias='merlinSeriesId', union_mode='left_to_right')
    nbcu_series_id: str | Any = Field(None, alias='nbcuSeriesId', union_mode='left_to_right')
    production_language: str | Any = Field(None, alias='productionLanguage', union_mode='left_to_right')
    provider_season_id: str | Any = Field(None, alias='providerSeasonId', union_mode='left_to_right')
    provider_series_id: str | Any = Field(None, alias='providerSeriesId', union_mode='left_to_right')
    season_id: UUID | Any = Field(None, alias='seasonId', union_mode='left_to_right')
    season_number: int | Any = Field(None, alias='seasonNumber', union_mode='left_to_right')
    series_id: UUID | Any = Field(None, alias='seriesId', union_mode='left_to_right')
    series_name: str | Any = Field(None, alias='seriesName', union_mode='left_to_right')
    series_native_id: str | Any = Field(None, alias='seriesNativeId', union_mode='left_to_right')
    sort_title: str | Any = Field(None, alias='sortTitle', union_mode='left_to_right')
    subtitled: bool | Any = Field(default=None, union_mode='left_to_right')
    synopsis: str | Any = Field(default=None, union_mode='left_to_right')
    synopsis_brief: str | Any = Field(None, alias='synopsisBrief', union_mode='left_to_right')
    title_seo: str | Any = Field(None, alias='titleSeo', union_mode='left_to_right')
    year: int | Any = Field(default=None, union_mode='left_to_right')
    advisory: list[AdvisoryItem2] | Any = Field(default=None, union_mode='left_to_right')

class ChildTypes8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    items: Items5 | Any = Field(default=None, union_mode='left_to_right')

class Attributes8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    alttext: str | Any = Field(default=None, union_mode='left_to_right')
    checksum: str | Any = Field(default=None, union_mode='left_to_right')
    child_node_types: list[str] | Any = Field(None, alias='childNodeTypes', union_mode='left_to_right')
    created_date: NaiveDatetime | Any = Field(None, alias='createdDate', union_mode='left_to_right')
    expiration_date: NaiveDatetime | Any = Field(None, alias='expirationDate', union_mode='left_to_right')
    filename: str | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')
    language: str | Any = Field(default=None, union_mode='left_to_right')
    modified_date: NaiveDatetime | Any = Field(None, alias='modifiedDate', union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    width: int | Any = Field(default=None, union_mode='left_to_right')

class Datum7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    links: Links | Any = Field(default=None, union_mode='left_to_right')
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    child_types: ChildTypes8 | Any = Field(None, alias='childTypes', union_mode='left_to_right')
    attributes: Attributes8 | Any = Field(default=None, union_mode='left_to_right')

class Images6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    data: list[Datum7] | Any = Field(default=None, union_mode='left_to_right')

class Relationships4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    images: Images6 | Any = Field(default=None, union_mode='left_to_right')

class Datum6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    links: Links | Any = Field(default=None, union_mode='left_to_right')
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    segment_id: str | Any = Field(None, alias='segmentId', union_mode='left_to_right')
    segment_name: str | Any = Field(None, alias='segmentName', union_mode='left_to_right')
    child_types: ChildTypes7 | Any = Field(None, alias='childTypes', union_mode='left_to_right')
    attributes: Attributes7 | Any = Field(default=None, union_mode='left_to_right')
    relationships: Relationships4 | Any = Field(default=None, union_mode='left_to_right')

class Items8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    data: list[Datum6] | Any = Field(default=None, union_mode='left_to_right')

class Relationships3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    items: Items8 | Any = Field(default=None, union_mode='left_to_right')

class Datum5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    links: Links | Any = Field(default=None, union_mode='left_to_right')
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    segment_id: str | Any = Field(None, alias='segmentId', union_mode='left_to_right')
    segment_name: str | Any = Field(None, alias='segmentName', union_mode='left_to_right')
    child_types: ChildTypes6 | Any = Field(None, alias='childTypes', union_mode='left_to_right')
    attributes: Attributes6 | Any = Field(default=None, union_mode='left_to_right')
    relationships: Relationships3 | Any = Field(default=None, union_mode='left_to_right')

class Items6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    data: list[Datum5] | Any = Field(default=None, union_mode='left_to_right')

class Relationships2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    items: Items6 | Any = Field(default=None, union_mode='left_to_right')

class Datum4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    links: Links | Any = Field(default=None, union_mode='left_to_right')
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    segment_id: str | Any = Field(None, alias='segmentId', union_mode='left_to_right')
    segment_name: str | Any = Field(None, alias='segmentName', union_mode='left_to_right')
    group_segment_id: str | Any = Field(None, alias='groupSegmentId', union_mode='left_to_right')
    group_segment_name: str | Any = Field(None, alias='groupSegmentName', union_mode='left_to_right')
    child_types: ChildTypes5 | Any = Field(None, alias='childTypes', union_mode='left_to_right')
    attributes: Attributes5 | Any = Field(default=None, union_mode='left_to_right')
    relationships: Relationships2 | Any = Field(default=None, union_mode='left_to_right')

class Collections2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    data: list[Datum4] | Any = Field(default=None, union_mode='left_to_right')

class Relationships(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    recs: Recs | Any = Field(default=None, union_mode='left_to_right')
    items: Items2 | Any = Field(default=None, union_mode='left_to_right')
    trailers: Trailers2 | Any = Field(default=None, union_mode='left_to_right')
    collections: Collections2 | Any = Field(default=None, union_mode='left_to_right')

class ShowModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    links: Links | Any = Field(default=None, union_mode='left_to_right')
    id: UUID | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    child_types: ChildTypes | Any = Field(None, alias='childTypes', union_mode='left_to_right')
    attributes: Attributes | Any = Field(default=None, union_mode='left_to_right')
    relationships: Relationships | Any = Field(default=None, union_mode='left_to_right')
    _raw_input: Any = PrivateAttr(default=None)

    @model_validator(mode='wrap')
    @classmethod
    def _capture_raw_input(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
        """Validate the model and keep the input it was built from."""
        model = handler(data)
        model._raw_input = data
        return model

    @property
    def raw_input(self) -> Any:
        """The input this model was validated from, as it was handed over."""
        return self._raw_input
