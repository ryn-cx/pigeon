from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from datetime import date, time
from typing import Any
from uuid import UUID
from pydantic import BaseModel, Field, NaiveDatetime

class Links(BaseModel):
    model_config = ConfigDict(defer_build=True)
    self: str

class Images(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[str] = Field(..., alias='nodeTypes')
    count: int

class FirstEp(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[str] = Field(..., alias='nodeTypes')
    count: int

class Shortforms(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[str] = Field(..., alias='nodeTypes')
    count: int

class FreeEpisodes(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[None] = Field(..., alias='nodeTypes')
    count: int

class Clips(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[str] = Field(..., alias='nodeTypes')
    count: int

class LinkedAssets(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[str] = Field(..., alias='nodeTypes')
    count: int

class Items(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[str] = Field(..., alias='nodeTypes')
    count: int

class Trailers(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[str] = Field(..., alias='nodeTypes')
    count: int

class Collections(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[str] = Field(..., alias='nodeTypes')
    count: int

class Latest(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[str] = Field(..., alias='nodeTypes')
    count: int

class ChildTypes(BaseModel):
    model_config = ConfigDict(defer_build=True)
    images: Images
    first_ep: FirstEp
    shortforms: Shortforms
    free_episodes: FreeEpisodes
    clips: Clips
    linked_assets: LinkedAssets | None = None
    items: Items
    trailers: Trailers | None = None
    collections: Collections | None = None
    latest: Latest | None = None

class AudienceLevelItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    scheme_provider: str = Field(..., alias='schemeProvider')
    segment_code: str = Field(..., alias='segmentCode')
    target_segment: str = Field(..., alias='targetSegment')

class VideoFormat(BaseModel):
    model_config = ConfigDict(defer_build=True)
    video_format: str = Field(..., alias='videoFormat')
    colour_spaces: list[str] = Field(..., alias='colourSpaces')
    audio_tracks: list[str] = Field(..., alias='audioTracks')

class TuneInBadgingEditorialTexts(BaseModel):
    model_config = ConfigDict(defer_build=True)
    short: str
    long: str

class TuneInBadging(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tune_in_badging_editorial_texts: TuneInBadgingEditorialTexts = Field(..., alias='tuneInBadgingEditorialTexts')

class Badging(BaseModel):
    model_config = ConfigDict(defer_build=True)
    video_formats: list[VideoFormat] = Field(..., alias='videoFormats')
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    tune_in_badging: TuneInBadging | None = Field(None, alias='tuneInBadging')

class LogoItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    key: str
    template: str

class Channel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    access_channel: str = Field(..., alias='accessChannel')
    name: str
    logo_style: str | None = Field(None, alias='logoStyle')
    provider_id: str | None = Field(None, alias='providerId')
    logo: list[LogoItem] | None = None
    sections: list[str] | None = None
    logo_height_percentage: int | None = Field(None, alias='logoHeightPercentage')

class DeviceAvailability(BaseModel):
    model_config = ConfigDict(defer_build=True)
    format: str
    media_type: str = Field(..., alias='mediaType')
    offer_stage: str = Field(..., alias='offerStage')
    offer_start_ts: int = Field(..., alias='offerStartTs')
    offer_end_ts: int = Field(..., alias='offerEndTs')
    content_segment: str = Field(..., alias='contentSegment')
    video_format: str = Field(..., alias='videoFormat')
    video_format_variant: str = Field(..., alias='videoFormatVariant')
    colour_space: str = Field(..., alias='colourSpace')

class DeviceAvailability1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    available: bool

class FanCriticRatingItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    fan_score: int = Field(..., alias='fanScore')
    critic_score: int = Field(..., alias='criticScore')

class AudioTracks(BaseModel):
    model_config = ConfigDict(defer_build=True)
    spa: list[str]
    eng: list[str]

class AvailableDevice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    platform: str

class Availability(BaseModel):
    model_config = ConfigDict(defer_build=True)
    available: bool
    media_type: str = Field(..., alias='mediaType')
    offer_stage: str = Field(..., alias='offerStage')
    offer_start_ts: int = Field(..., alias='offerStartTs')
    offer_end_ts: int = Field(..., alias='offerEndTs')
    available_devices: list[AvailableDevice] = Field(..., alias='availableDevices')
    extended_offer_start_ts: int = Field(..., alias='extendedOfferStartTs')
    extended_offer_end_ts: int = Field(..., alias='extendedOfferEndTs')
    content_segment: str = Field(..., alias='contentSegment')
    video_format: str = Field(..., alias='videoFormat')
    video_format_variant: str = Field(..., alias='videoFormatVariant')
    colour_space: str = Field(..., alias='colourSpace')

class Hd(BaseModel):
    model_config = ConfigDict(defer_build=True)
    audio_tracks: AudioTracks = Field(..., alias='audioTracks')
    chapter_markers: list[None] = Field(..., alias='chapterMarkers')
    event_stage: str = Field(..., alias='eventStage')
    availability: Availability
    start_of_credits: int = Field(..., alias='startOfCredits')

class Formats(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hd: Hd = Field(..., alias='HD')

class GenreDetail(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary: bool
    type: str
    term_id: str = Field(..., alias='termId')
    term_description: str = Field(..., alias='termDescription')
    code: str

class GenreListItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    subgenre: list[str]
    genre: list[str]

class Image(BaseModel):
    model_config = ConfigDict(defer_build=True)
    url: str
    type: str

class MediaType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    media_type: str = Field(..., alias='mediaType')
    count: int
    latest: int

class TargetAudience(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str

class Attributes(BaseModel):
    model_config = ConfigDict(defer_build=True)
    free_wheel_content_id: str = Field(..., alias='FreeWheelContentID')
    audience_level: list[AudienceLevelItem] = Field(..., alias='audienceLevel')
    audio_described: bool = Field(..., alias='audioDescribed')
    available_episode_count: int = Field(..., alias='availableEpisodeCount')
    available_season_count: int = Field(..., alias='availableSeasonCount')
    badging: Badging
    brands: list[str]
    cast: list[str]
    channel: Channel
    chapters_enabled: bool = Field(..., alias='chaptersEnabled')
    child_node_types: list[str] = Field(..., alias='childNodeTypes')
    classification: list[str]
    collection_pdp: str = Field(..., alias='collectionPdp')
    content_segments: list[str] = Field(..., alias='contentSegments')
    created_date: int = Field(..., alias='createdDate')
    desc_long_seo: str = Field(..., alias='descLongSeo')
    device_availabilities: list[DeviceAvailability] = Field(..., alias='deviceAvailabilities')
    device_availability: DeviceAvailability1 = Field(..., alias='deviceAvailability')
    fan_critic_rating: list[FanCriticRatingItem] = Field(..., alias='fanCriticRating')
    formats: Formats
    genre_details: list[GenreDetail] = Field(..., alias='genreDetails')
    genre_list: list[GenreListItem] = Field(..., alias='genreList')
    genres: list[str]
    gracenote_id: str = Field(..., alias='gracenoteId')
    gracenote_series_id: str = Field(..., alias='gracenoteSeriesId')
    images: list[Image]
    media_types: list[MediaType] = Field(..., alias='mediaTypes')
    merlin_id: str = Field(..., alias='merlinId')
    merlin_series_id: str = Field(..., alias='merlinSeriesId')
    nbcu_id: str = Field(..., alias='nbcuId')
    nbcu_series_id: str = Field(..., alias='nbcuSeriesId')
    ott_certificate: str = Field(..., alias='ottCertificate')
    provider_series_id: str = Field(..., alias='providerSeriesId')
    reverse_order: bool = Field(..., alias='reverseOrder')
    section_navigation: str = Field(..., alias='sectionNavigation')
    series_native_id: str = Field(..., alias='seriesNativeId')
    series_uuid: UUID = Field(..., alias='seriesUuid')
    slug: str
    smart_call_to_action: str = Field(..., alias='smartCallToAction')
    sort_title: str = Field(..., alias='sortTitle')
    synopsis_long: str = Field(..., alias='synopsisLong')
    target_audience: TargetAudience = Field(..., alias='targetAudience')
    title: str
    title_medium: str = Field(..., alias='titleMedium')
    title_seo: str = Field(..., alias='titleSeo')
    synopsis: str | None = None
    synopsis_short: str | None = Field(None, alias='synopsisShort')
    title_medium_seo: str | None = Field(None, alias='titleMediumSeo')

class FreeEpisodes1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[str] = Field(..., alias='nodeTypes')
    count: int

class NextClips(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[str] = Field(..., alias='nodeTypes')
    count: int

class NextShortforms(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[str] = Field(..., alias='nodeTypes')
    count: int

class ChildTypes1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    images: Images
    first_ep: FirstEp | None = None
    shortforms: Shortforms | None = None
    free_episodes: FreeEpisodes1 | None = None
    clips: Clips | None = None
    items: Items | None = None
    latest: Latest | None = None
    trailers: Trailers | None = None
    collections: Collections | None = None
    next_clips: NextClips | None = None
    next_shortforms: NextShortforms | None = None
    linked_assets: LinkedAssets | None = None

class TuneInBadging1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tune_in_badging_editorial_texts: TuneInBadgingEditorialTexts = Field(..., alias='tuneInBadgingEditorialTexts')

class Badging1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    video_formats: list[VideoFormat] = Field(..., alias='videoFormats')
    audio_tracks: list[str] = Field(..., alias='audioTracks')
    tune_in_badging: TuneInBadging1 | None = Field(None, alias='tuneInBadging')

class Channel1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    logo_style: str | None = Field(None, alias='logoStyle')
    access_channel: str = Field(..., alias='accessChannel')
    provider_id: str | None = Field(None, alias='providerId')
    name: str
    logo: list[LogoItem] | None = None
    sections: list[str] | None = None
    logo_height_percentage: int | None = Field(None, alias='logoHeightPercentage')

class DeviceAvailability2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    format: str
    media_type: str = Field(..., alias='mediaType')
    offer_stage: str = Field(..., alias='offerStage')
    offer_start_ts: int = Field(..., alias='offerStartTs')
    offer_end_ts: int = Field(..., alias='offerEndTs')
    content_segment: str = Field(..., alias='contentSegment')
    video_format: str = Field(..., alias='videoFormat')
    video_format_variant: str = Field(..., alias='videoFormatVariant')
    colour_space: str = Field(..., alias='colourSpace')
    streamable: bool | None = None
    downloadable: bool | None = None

class DeviceAvailability3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    available: bool

class FanCriticRatingItem1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    critic_score: int | None = Field(None, alias='criticScore')
    fan_score: int | None = Field(None, alias='fanScore')
    tags: list[str] | None = None

class AudioTracks1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    eng: list[str]
    spa: list[str] | None = None

class Availability1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    available: bool
    media_type: str = Field(..., alias='mediaType')
    offer_stage: str = Field(..., alias='offerStage')
    offer_start_ts: int = Field(..., alias='offerStartTs')
    offer_end_ts: int = Field(..., alias='offerEndTs')
    available_devices: list[AvailableDevice] = Field(..., alias='availableDevices')
    extended_offer_start_ts: int = Field(..., alias='extendedOfferStartTs')
    extended_offer_end_ts: int = Field(..., alias='extendedOfferEndTs')
    content_segment: str = Field(..., alias='contentSegment')
    video_format: str = Field(..., alias='videoFormat')
    video_format_variant: str = Field(..., alias='videoFormatVariant')
    colour_space: str = Field(..., alias='colourSpace')
    free_offer_end_ts: int | None = Field(None, alias='freeOfferEndTs')
    streamable: bool | None = None
    downloadable: bool | None = None

class Markers(BaseModel):
    model_config = ConfigDict(defer_build=True)
    socr: int = Field(..., alias='SOCR')
    solc: int = Field(..., alias='SOLC')
    eolc: int = Field(..., alias='EOLC')

class Hd1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    audio_tracks: AudioTracks1 = Field(..., alias='audioTracks')
    chapter_markers: list[None] = Field(..., alias='chapterMarkers')
    event_stage: str = Field(..., alias='eventStage')
    availability: Availability1
    start_of_credits: int = Field(..., alias='startOfCredits')
    content_id: str | None = Field(None, alias='contentId')
    markers: Markers | None = None

class Formats1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hd: Hd1 = Field(..., alias='HD')

class Fact(BaseModel):
    model_config = ConfigDict(defer_build=True)
    fact_icon: str = Field(..., alias='factIcon')
    fact_text: str = Field(..., alias='factText')

class AlternativeDateItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    value: date
    date_type: str = Field(..., alias='dateType')
    territory: str

class Attributes1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    free_wheel_content_id: str = Field(..., alias='FreeWheelContentID')
    audience_level: list[AudienceLevelItem] | None = Field(None, alias='audienceLevel')
    audio_described: bool = Field(..., alias='audioDescribed')
    available_episode_count: int | None = Field(None, alias='availableEpisodeCount')
    available_season_count: int | None = Field(None, alias='availableSeasonCount')
    badging: Badging1
    brands: list[str] | None = None
    cast: list[str] | None = None
    channel: Channel1
    chapters_enabled: bool = Field(..., alias='chaptersEnabled')
    child_node_types: list[str] = Field(..., alias='childNodeTypes')
    classification: list[str]
    content_segments: list[str] = Field(..., alias='contentSegments')
    created_date: int = Field(..., alias='createdDate')
    desc_long_seo: str = Field(..., alias='descLongSeo')
    device_availabilities: list[DeviceAvailability2] = Field(..., alias='deviceAvailabilities')
    device_availability: DeviceAvailability3 = Field(..., alias='deviceAvailability')
    fan_critic_rating: list[FanCriticRatingItem1] | None = Field(None, alias='fanCriticRating')
    formats: Formats1
    genre_details: list[GenreDetail] | None = Field(None, alias='genreDetails')
    genre_list: list[GenreListItem] = Field(..., alias='genreList')
    genres: list[str]
    gracenote_id: str = Field(..., alias='gracenoteId')
    gracenote_series_id: str | None = Field(None, alias='gracenoteSeriesId')
    images: list[Image]
    media_types: list[MediaType] | None = Field(None, alias='mediaTypes')
    merlin_id: str = Field(..., alias='merlinId')
    merlin_series_id: str | None = Field(None, alias='merlinSeriesId')
    nbcu_id: str = Field(..., alias='nbcuId')
    nbcu_series_id: str | None = Field(None, alias='nbcuSeriesId')
    ott_certificate: str = Field(..., alias='ottCertificate')
    provider_series_id: str | None = Field(None, alias='providerSeriesId')
    reverse_order: bool | None = Field(None, alias='reverseOrder')
    section_navigation: str = Field(..., alias='sectionNavigation')
    series_native_id: str | None = Field(None, alias='seriesNativeId')
    series_uuid: UUID | None = Field(None, alias='seriesUuid')
    slug: str
    smart_call_to_action: str | None = Field(None, alias='smartCallToAction')
    sort_title: str = Field(..., alias='sortTitle')
    synopsis_long: str = Field(..., alias='synopsisLong')
    synopsis_short: str | None = Field(None, alias='synopsisShort')
    target_audience: TargetAudience = Field(..., alias='targetAudience')
    title: str
    title_medium: str = Field(..., alias='titleMedium')
    title_seo: str = Field(..., alias='titleSeo')
    synopsis: str | None = None
    facts: list[Fact] | None = None
    title_medium_seo: str | None = Field(None, alias='titleMediumSeo')
    director: list[str] | None = None
    alternative_date: list[AlternativeDateItem] | None = Field(None, alias='alternativeDate')
    closed_captioned: bool | None = Field(None, alias='closedCaptioned')
    cwm: str | None = None
    duration_milliseconds: int | None = Field(None, alias='durationMilliseconds')
    duration_minutes: int | None = Field(None, alias='durationMinutes')
    duration_seconds: int | None = Field(None, alias='durationSeconds')
    main_original_language: str | None = Field(None, alias='mainOriginalLanguage')
    native_id: str | None = Field(None, alias='nativeId')
    producer: list[str] | None = None
    production_language: str | None = Field(None, alias='productionLanguage')
    programme_uuid: UUID | None = Field(None, alias='programmeUuid')
    provider_id: str | None = Field(None, alias='providerId')
    provider_variant_id: UUID | None = Field(None, alias='providerVariantId')
    rating: str | None = None
    rating_percentage: int | None = Field(None, alias='ratingPercentage')
    runtime: time | None = None
    subtitled: bool | None = None
    synopsis_brief: str | None = Field(None, alias='synopsisBrief')
    title_long: str | None = Field(None, alias='titleLong')
    year: int | None = None
    desc_short_seo: str | None = Field(None, alias='descShortSeo')

class Datum(BaseModel):
    model_config = ConfigDict(defer_build=True)
    links: Links
    id: UUID
    type: str
    child_types: ChildTypes1 = Field(..., alias='childTypes')
    attributes: Attributes1

class Recs(BaseModel):
    model_config = ConfigDict(defer_build=True)
    data: list[Datum]

class ChildTypes2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    images: Images
    items: Items

class Badging2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    video_formats: list[VideoFormat] = Field(..., alias='videoFormats')
    audio_tracks: list[str] = Field(..., alias='audioTracks')

class Channel2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    access_channel: str = Field(..., alias='accessChannel')
    name: str
    logo_style: str | None = Field(None, alias='logoStyle')
    provider_id: str | None = Field(None, alias='providerId')
    logo: list[LogoItem] | None = None
    sections: list[str] | None = None
    logo_height_percentage: int | None = Field(None, alias='logoHeightPercentage')

class DeviceAvailability4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    format: str
    media_type: str = Field(..., alias='mediaType')
    offer_stage: str = Field(..., alias='offerStage')
    offer_start_ts: int = Field(..., alias='offerStartTs')
    offer_end_ts: int = Field(..., alias='offerEndTs')
    content_segment: str = Field(..., alias='contentSegment')
    video_format: str = Field(..., alias='videoFormat')
    video_format_variant: str = Field(..., alias='videoFormatVariant')
    colour_space: str = Field(..., alias='colourSpace')

class DeviceAvailability5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    available: bool

class FanCriticRatingItem2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    fan_score: int = Field(..., alias='fanScore')
    critic_score: int = Field(..., alias='criticScore')

class AudioTracks2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    spa: list[str]
    eng: list[str]

class Availability2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    available: bool
    media_type: str = Field(..., alias='mediaType')
    offer_stage: str = Field(..., alias='offerStage')
    offer_start_ts: int = Field(..., alias='offerStartTs')
    offer_end_ts: int = Field(..., alias='offerEndTs')
    available_devices: list[AvailableDevice] = Field(..., alias='availableDevices')
    extended_offer_start_ts: int = Field(..., alias='extendedOfferStartTs')
    extended_offer_end_ts: int = Field(..., alias='extendedOfferEndTs')
    content_segment: str = Field(..., alias='contentSegment')
    video_format: str = Field(..., alias='videoFormat')
    video_format_variant: str = Field(..., alias='videoFormatVariant')
    colour_space: str = Field(..., alias='colourSpace')

class Hd2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    audio_tracks: AudioTracks2 = Field(..., alias='audioTracks')
    chapter_markers: list[None] = Field(..., alias='chapterMarkers')
    event_stage: str = Field(..., alias='eventStage')
    availability: Availability2
    start_of_credits: int = Field(..., alias='startOfCredits')

class Formats2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hd: Hd2 = Field(..., alias='HD')

class Attributes2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    free_wheel_content_id: str = Field(..., alias='FreeWheelContentID')
    audio_described: bool = Field(..., alias='audioDescribed')
    badging: Badging2
    channel: Channel2
    chapters_enabled: bool = Field(..., alias='chaptersEnabled')
    child_node_types: list[str] = Field(..., alias='childNodeTypes')
    classification: list[str]
    content_segments: list[str] = Field(..., alias='contentSegments')
    created_date: int = Field(..., alias='createdDate')
    desc_long_seo: str = Field(..., alias='descLongSeo')
    device_availabilities: list[DeviceAvailability4] = Field(..., alias='deviceAvailabilities')
    device_availability: DeviceAvailability5 = Field(..., alias='deviceAvailability')
    fan_critic_rating: list[FanCriticRatingItem2] = Field(..., alias='fanCriticRating')
    formats: Formats2
    genre_list: list[GenreListItem] = Field(..., alias='genreList')
    genres: list[str]
    gracenote_id: str = Field(..., alias='gracenoteId')
    gracenote_series_id: str = Field(..., alias='gracenoteSeriesId')
    images: list[Image]
    merlin_id: str = Field(..., alias='merlinId')
    merlin_series_id: str = Field(..., alias='merlinSeriesId')
    nbcu_id: str = Field(..., alias='nbcuId')
    nbcu_series_id: str = Field(..., alias='nbcuSeriesId')
    provider_season_id: str = Field(..., alias='providerSeasonId')
    provider_series_id: str = Field(..., alias='providerSeriesId')
    season_number: int = Field(..., alias='seasonNumber')
    season_uuid: UUID = Field(..., alias='seasonUuid')
    section_navigation: str = Field(..., alias='sectionNavigation')
    series_id: UUID = Field(..., alias='seriesId')
    series_name: str = Field(..., alias='seriesName')
    series_native_id: str = Field(..., alias='seriesNativeId')
    slug: str
    sort_title: str = Field(..., alias='sortTitle')
    synopsis_long: str | None = Field(None, alias='synopsisLong')
    title: str
    title_medium: str = Field(..., alias='titleMedium')
    title_seo: str = Field(..., alias='titleSeo')
    genre_details: list[GenreDetail] | None = Field(None, alias='genreDetails')
    synopsis_short: str | None = Field(None, alias='synopsisShort')
    title_medium_seo: str | None = Field(None, alias='titleMediumSeo')

class ChildTypes3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    images: Images

class Term(BaseModel):
    model_config = ConfigDict(defer_build=True)
    description: str
    abbreviation: str | None = None

class AdvisoryItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    terms: list[Term]
    id: str
    group: int

class Badging3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    video_formats: list[VideoFormat] = Field(..., alias='videoFormats')
    audio_tracks: list[str] = Field(..., alias='audioTracks')

class Channel3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    access_channel: str = Field(..., alias='accessChannel')
    name: str
    logo_style: str | None = Field(None, alias='logoStyle')
    provider_id: str | None = Field(None, alias='providerId')
    logo: list[LogoItem] | None = None
    sections: list[str] | None = None
    logo_height_percentage: int | None = Field(None, alias='logoHeightPercentage')

class DeviceAvailability6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    format: str
    media_type: str = Field(..., alias='mediaType')
    offer_stage: str = Field(..., alias='offerStage')
    offer_start_ts: int = Field(..., alias='offerStartTs')
    offer_end_ts: int = Field(..., alias='offerEndTs')
    streamable: bool
    downloadable: bool
    content_segment: str = Field(..., alias='contentSegment')
    video_format: str = Field(..., alias='videoFormat')
    video_format_variant: str = Field(..., alias='videoFormatVariant')
    colour_space: str = Field(..., alias='colourSpace')

class DeviceAvailability7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    available: bool

class AudioTracks3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    spa: list[str] | None = None
    eng: list[str]

class Availability3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    available: bool
    media_type: str = Field(..., alias='mediaType')
    offer_stage: str = Field(..., alias='offerStage')
    offer_start_ts: int = Field(..., alias='offerStartTs')
    offer_end_ts: int = Field(..., alias='offerEndTs')
    streamable: bool
    downloadable: bool
    available_devices: list[AvailableDevice] = Field(..., alias='availableDevices')
    extended_offer_start_ts: int = Field(..., alias='extendedOfferStartTs')
    extended_offer_end_ts: int = Field(..., alias='extendedOfferEndTs')
    content_segment: str = Field(..., alias='contentSegment')
    video_format: str = Field(..., alias='videoFormat')
    video_format_variant: str = Field(..., alias='videoFormatVariant')
    colour_space: str = Field(..., alias='colourSpace')

class Markers1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    socr: int = Field(..., alias='SOCR')
    soi: int | None = Field(None, alias='SOI')
    hsi: int | None = Field(None, alias='HSI')
    spi: int | None = Field(None, alias='SPI')
    solc: int | None = Field(None, alias='SOLC')
    eolc: int | None = Field(None, alias='EOLC')
    sor: int | None = Field(None, alias='SOR')
    hsr: int | None = Field(None, alias='HSR')
    spr: int | None = Field(None, alias='SPR')

class Hd3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    audio_tracks: AudioTracks3 = Field(..., alias='audioTracks')
    chapter_markers: list[None] = Field(..., alias='chapterMarkers')
    event_stage: str = Field(..., alias='eventStage')
    content_id: str = Field(..., alias='contentId')
    availability: Availability3
    start_of_credits: int = Field(..., alias='startOfCredits')
    markers: Markers1

class Formats3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hd: Hd3 = Field(..., alias='HD')

class Attributes3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    free_wheel_content_id: str = Field(..., alias='FreeWheelContentID')
    advisory: list[AdvisoryItem] | None = None
    audio_described: bool = Field(..., alias='audioDescribed')
    badging: Badging3
    channel: Channel3
    chapters_enabled: bool = Field(..., alias='chaptersEnabled')
    child_node_types: list[str] = Field(..., alias='childNodeTypes')
    classification: list[str]
    closed_captioned: bool = Field(..., alias='closedCaptioned')
    content_segments: list[str] = Field(..., alias='contentSegments')
    created_date: int = Field(..., alias='createdDate')
    cwm: str
    desc_long_seo: str = Field(..., alias='descLongSeo')
    device_availabilities: list[DeviceAvailability6] = Field(..., alias='deviceAvailabilities')
    device_availability: DeviceAvailability7 = Field(..., alias='deviceAvailability')
    duration_milliseconds: int = Field(..., alias='durationMilliseconds')
    duration_minutes: int = Field(..., alias='durationMinutes')
    duration_seconds: int = Field(..., alias='durationSeconds')
    episode_name: str = Field(..., alias='episodeName')
    episode_name_long: str = Field(..., alias='episodeNameLong')
    episode_number: int = Field(..., alias='episodeNumber')
    formats: Formats3
    genre_list: list[GenreListItem] = Field(..., alias='genreList')
    genres: list[str]
    gracenote_id: str = Field(..., alias='gracenoteId')
    gracenote_series_id: str = Field(..., alias='gracenoteSeriesId')
    images: list[Image]
    last_in_season: bool = Field(..., alias='lastInSeason')
    main_original_language: str = Field(..., alias='mainOriginalLanguage')
    merlin_id: str = Field(..., alias='merlinId')
    merlin_series_id: str = Field(..., alias='merlinSeriesId')
    nbcu_id: str = Field(..., alias='nbcuId')
    nbcu_series_id: str = Field(..., alias='nbcuSeriesId')
    ott_certificate: str = Field(..., alias='ottCertificate')
    production_language: str = Field(..., alias='productionLanguage')
    programme_uuid: UUID = Field(..., alias='programmeUuid')
    provider_id: str = Field(..., alias='providerId')
    provider_season_id: str = Field(..., alias='providerSeasonId')
    provider_series_id: str = Field(..., alias='providerSeriesId')
    provider_variant_id: UUID = Field(..., alias='providerVariantId')
    runtime: time
    season_id: UUID = Field(..., alias='seasonId')
    season_number: int = Field(..., alias='seasonNumber')
    section_navigation: str = Field(..., alias='sectionNavigation')
    series_id: UUID = Field(..., alias='seriesId')
    series_name: str = Field(..., alias='seriesName')
    series_native_id: str = Field(..., alias='seriesNativeId')
    slug: str
    sort_title: str = Field(..., alias='sortTitle')
    subtitled: bool
    synopsis: str
    synopsis_brief: str = Field(..., alias='synopsisBrief')
    synopsis_long: str = Field(..., alias='synopsisLong')
    synopsis_short: str = Field(..., alias='synopsisShort')
    target_audience: TargetAudience = Field(..., alias='targetAudience')
    title: str
    title_long: str = Field(..., alias='titleLong')
    title_medium: str = Field(..., alias='titleMedium')
    title_seo: str = Field(..., alias='titleSeo')
    year: int
    cast: list[str] | None = None
    editorial_warning_text: str | None = Field(None, alias='editorialWarningText')
    genre_details: list[GenreDetail] | None = Field(None, alias='genreDetails')
    merlin_alternate_id: str | None = Field(None, alias='merlinAlternateId')

class Datum2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    links: Links
    id: UUID
    type: str
    child_types: ChildTypes3 = Field(..., alias='childTypes')
    attributes: Attributes3

class Items4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    data: list[Datum2]

class Relationships1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    items: Items4

class Datum1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    links: Links
    id: UUID
    type: str
    child_types: ChildTypes2 = Field(..., alias='childTypes')
    attributes: Attributes2
    relationships: Relationships1

class Items2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    data: list[Datum1]

class ChildTypes4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    images: Images

class Term1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    description: str
    abbreviation: str

class AdvisoryItem1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    terms: list[Term1]
    id: str
    group: int

class Badging4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    video_formats: list[VideoFormat] = Field(..., alias='videoFormats')
    audio_tracks: list[str] = Field(..., alias='audioTracks')

class Channel4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    access_channel: str = Field(..., alias='accessChannel')
    name: str

class DeviceAvailability8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    format: str
    media_type: str = Field(..., alias='mediaType')
    offer_stage: str = Field(..., alias='offerStage')
    offer_start_ts: int = Field(..., alias='offerStartTs')
    offer_end_ts: int = Field(..., alias='offerEndTs')
    streamable: bool
    downloadable: bool
    content_segment: str = Field(..., alias='contentSegment')
    video_format: str = Field(..., alias='videoFormat')
    video_format_variant: str = Field(..., alias='videoFormatVariant')
    colour_space: str = Field(..., alias='colourSpace')

class DeviceAvailability9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    available: bool

class AudioTracks4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    eng: list[str]

class Availability4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    available: bool
    media_type: str = Field(..., alias='mediaType')
    offer_stage: str = Field(..., alias='offerStage')
    offer_start_ts: int = Field(..., alias='offerStartTs')
    offer_end_ts: int = Field(..., alias='offerEndTs')
    streamable: bool
    downloadable: bool
    available_devices: list[AvailableDevice] = Field(..., alias='availableDevices')
    extended_offer_start_ts: int = Field(..., alias='extendedOfferStartTs')
    extended_offer_end_ts: int = Field(..., alias='extendedOfferEndTs')
    content_segment: str = Field(..., alias='contentSegment')
    video_format: str = Field(..., alias='videoFormat')
    video_format_variant: str = Field(..., alias='videoFormatVariant')
    colour_space: str = Field(..., alias='colourSpace')

class Hd4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    audio_tracks: AudioTracks4 = Field(..., alias='audioTracks')
    chapter_markers: list[None] = Field(..., alias='chapterMarkers')
    event_stage: str = Field(..., alias='eventStage')
    content_id: str = Field(..., alias='contentId')
    availability: Availability4
    start_of_credits: int = Field(..., alias='startOfCredits')

class Formats4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hd: Hd4 = Field(..., alias='HD')

class LinkedEpisode(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_id: UUID = Field(..., alias='nodeId')
    content_id: str = Field(..., alias='contentId')
    provider_variant_id: UUID = Field(..., alias='providerVariantId')
    format: str

class MainTitleInfoItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_id: UUID = Field(..., alias='nodeId')
    type: str
    series_uuid: UUID = Field(..., alias='seriesUuid')
    provider_series_id: str = Field(..., alias='providerSeriesId')
    linked_episodes: list[LinkedEpisode] = Field(..., alias='linkedEpisodes')
    content_segments: list[str] = Field(..., alias='contentSegments')

class Attributes4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    free_wheel_content_id: str = Field(..., alias='FreeWheelContentID')
    advisory: list[AdvisoryItem1] | None = None
    audio_described: bool = Field(..., alias='audioDescribed')
    autoplay: bool
    badging: Badging4
    channel: Channel4
    chapters_enabled: bool = Field(..., alias='chaptersEnabled')
    child_node_types: list[str] = Field(..., alias='childNodeTypes')
    classification: list[str]
    closed_captioned: bool = Field(..., alias='closedCaptioned')
    content_segments: list[str] = Field(..., alias='contentSegments')
    created_date: int = Field(..., alias='createdDate')
    cwm: str
    device_availabilities: list[DeviceAvailability8] = Field(..., alias='deviceAvailabilities')
    device_availability: DeviceAvailability9 = Field(..., alias='deviceAvailability')
    duration_milliseconds: int = Field(..., alias='durationMilliseconds')
    duration_minutes: int = Field(..., alias='durationMinutes')
    duration_seconds: int = Field(..., alias='durationSeconds')
    formats: Formats4
    free_wheel_creative_id: str = Field(..., alias='freeWheelCreativeId')
    genre_list: list[GenreListItem] = Field(..., alias='genreList')
    genres: list[str]
    images: list[Image]
    main_title_info: list[MainTitleInfoItem] = Field(..., alias='mainTitleInfo')
    merlin_id: str = Field(..., alias='merlinId')
    nbcu_id: str = Field(..., alias='nbcuId')
    ott_certificate: str = Field(..., alias='ottCertificate')
    provider_id: str = Field(..., alias='providerId')
    provider_variant_id: UUID = Field(..., alias='providerVariantId')
    runtime: time
    series_uuid: UUID = Field(..., alias='seriesUuid')
    slug: str
    synopsis_long: str = Field(..., alias='synopsisLong')
    synopsis_short: str = Field(..., alias='synopsisShort')
    target_audience: TargetAudience = Field(..., alias='targetAudience')
    title: str
    title_long: str = Field(..., alias='titleLong')
    title_medium: str = Field(..., alias='titleMedium')

class Datum3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    links: Links
    id: UUID
    type: str
    child_types: ChildTypes4 = Field(..., alias='childTypes')
    attributes: Attributes4

class Trailers2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    data: list[Datum3]

class Items5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[str] = Field(..., alias='nodeTypes')
    count: int

class ChildTypes5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    items: Items5

class RenderHint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    group_template: str = Field(..., alias='groupTemplate')

class Attributes5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    alias: str
    child_node_types: list[str] = Field(..., alias='childNodeTypes')
    created_date: int = Field(..., alias='createdDate')
    render_hint: RenderHint = Field(..., alias='renderHint')
    section_navigation: str = Field(..., alias='sectionNavigation')
    slug: str
    title: str

class CurationConfig(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[str] = Field(..., alias='nodeTypes')
    count: int

class ChildTypes6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    items: Items5
    curation_config: CurationConfig | None = Field(None, alias='curation-config')

class RenderHint1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    orientation: str
    sort: str
    view_all: str | None = Field(None, alias='viewAll')
    image_template: str = Field(..., alias='imageTemplate')

class Attributes6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    child_node_types: list[str] = Field(..., alias='childNodeTypes')
    collection_type: str = Field(..., alias='collectionType')
    content_level: str = Field(..., alias='contentLevel')
    created_date: int = Field(..., alias='createdDate')
    items_count: int = Field(..., alias='itemsCount')
    keep_if_empty: bool = Field(..., alias='keepIfEmpty')
    orientation: str
    rail_title_type: str = Field(..., alias='railTitleType')
    refresh_policy: str = Field(..., alias='refreshPolicy')
    render_hint: RenderHint1 = Field(..., alias='renderHint')
    section_navigation: str = Field(..., alias='sectionNavigation')
    slug: str
    sort_policy: str = Field(..., alias='sortPolicy')
    title: str

class ChildTypes7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    images: Images
    items: Items5 | None = None
    curation_config: CurationConfig | None = Field(None, alias='curation-config')

class Image5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    width: int | None = None
    height: int | None = None
    url: str
    type: str

class RenderHint2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    orientation: str
    autoplay: str
    sort: str | None = None
    image_template: str | None = Field(None, alias='imageTemplate')

class Badging5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    video_formats: list[VideoFormat] = Field(..., alias='videoFormats')
    audio_tracks: list[str] = Field(..., alias='audioTracks')

class Channel5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    access_channel: str = Field(..., alias='accessChannel')
    name: str
    logo_style: str | None = Field(None, alias='logoStyle')
    provider_id: str | None = Field(None, alias='providerId')
    logo: list[LogoItem] | None = None
    sections: list[str] | None = None
    logo_height_percentage: int | None = Field(None, alias='logoHeightPercentage')

class DeviceAvailability10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    format: str
    media_type: str = Field(..., alias='mediaType')
    offer_stage: str = Field(..., alias='offerStage')
    offer_start_ts: int = Field(..., alias='offerStartTs')
    offer_end_ts: int = Field(..., alias='offerEndTs')
    streamable: bool
    downloadable: bool
    content_segment: str = Field(..., alias='contentSegment')
    video_format: str = Field(..., alias='videoFormat')
    video_format_variant: str = Field(..., alias='videoFormatVariant')
    colour_space: str = Field(..., alias='colourSpace')

class DeviceAvailability11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    available: bool

class AudioTracks5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    eng: list[str]
    spa: list[str] | None = None

class Availability5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    available: bool
    media_type: str = Field(..., alias='mediaType')
    offer_stage: str = Field(..., alias='offerStage')
    offer_start_ts: int = Field(..., alias='offerStartTs')
    offer_end_ts: int = Field(..., alias='offerEndTs')
    streamable: bool
    downloadable: bool
    available_devices: list[AvailableDevice] = Field(..., alias='availableDevices')
    extended_offer_start_ts: int = Field(..., alias='extendedOfferStartTs')
    extended_offer_end_ts: int = Field(..., alias='extendedOfferEndTs')
    content_segment: str = Field(..., alias='contentSegment')
    video_format: str = Field(..., alias='videoFormat')
    video_format_variant: str = Field(..., alias='videoFormatVariant')
    colour_space: str = Field(..., alias='colourSpace')

class Markers2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    socr: int = Field(..., alias='SOCR')
    soi: int | None = Field(None, alias='SOI')
    hsi: int | None = Field(None, alias='HSI')
    spi: int | None = Field(None, alias='SPI')

class Hd5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    audio_tracks: AudioTracks5 = Field(..., alias='audioTracks')
    chapter_markers: list[None] = Field(..., alias='chapterMarkers')
    event_stage: str = Field(..., alias='eventStage')
    content_id: str = Field(..., alias='contentId')
    availability: Availability5
    start_of_credits: int = Field(..., alias='startOfCredits')
    markers: Markers2 | None = None

class Formats5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hd: Hd5 = Field(..., alias='HD')

class AdvisoryItem2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    terms: list[Term1]
    id: str
    group: int

class Attributes7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    child_node_types: list[str] = Field(..., alias='childNodeTypes')
    collection_type: str | None = Field(None, alias='collectionType')
    content_level: str | None = Field(None, alias='contentLevel')
    created_date: int = Field(..., alias='createdDate')
    image_url: str | None = Field(None, alias='imageUrl')
    images: list[Image5]
    items_count: int | None = Field(None, alias='itemsCount')
    keep_if_empty: bool | None = Field(None, alias='keepIfEmpty')
    orientation: str | None = None
    promoted_item: bool = Field(..., alias='promotedItem')
    rail_title_type: str | None = Field(None, alias='railTitleType')
    refresh_policy: str | None = Field(None, alias='refreshPolicy')
    render_hint: RenderHint2 | None = Field(None, alias='renderHint')
    section_navigation: str | None = Field(None, alias='sectionNavigation')
    slug: str
    sort_policy: str | None = Field(None, alias='sortPolicy')
    title: str
    free_wheel_content_id: str | None = Field(None, alias='FreeWheelContentID')
    audio_described: bool | None = Field(None, alias='audioDescribed')
    badging: Badging5 | None = None
    channel: Channel5 | None = None
    chapters_enabled: bool | None = Field(None, alias='chaptersEnabled')
    classification: list[str] | None = None
    closed_captioned: bool | None = Field(None, alias='closedCaptioned')
    content_segments: list[str] | None = Field(None, alias='contentSegments')
    device_availabilities: list[DeviceAvailability10] | None = Field(None, alias='deviceAvailabilities')
    device_availability: DeviceAvailability11 | None = Field(None, alias='deviceAvailability')
    duration_milliseconds: int | None = Field(None, alias='durationMilliseconds')
    duration_minutes: int | None = Field(None, alias='durationMinutes')
    duration_seconds: int | None = Field(None, alias='durationSeconds')
    formats: Formats5 | None = None
    free_wheel_creative_id: str | None = Field(None, alias='freeWheelCreativeId')
    genre_list: list[GenreListItem] | None = Field(None, alias='genreList')
    genres: list[str] | None = None
    merlin_id: str | None = Field(None, alias='merlinId')
    nbcu_id: str | None = Field(None, alias='nbcuId')
    ott_certificate: str | None = Field(None, alias='ottCertificate')
    programme_uuid: UUID | None = Field(None, alias='programmeUuid')
    provider_id: str | None = Field(None, alias='providerId')
    provider_variant_id: UUID | None = Field(None, alias='providerVariantId')
    runtime: time | None = None
    synopsis_long: str | None = Field(None, alias='synopsisLong')
    synopsis_short: str | None = Field(None, alias='synopsisShort')
    target_audience: TargetAudience | None = Field(None, alias='targetAudience')
    title_long: str | None = Field(None, alias='titleLong')
    title_medium: str | None = Field(None, alias='titleMedium')
    alternative_date: list[AlternativeDateItem] | None = Field(None, alias='alternativeDate')
    uriid: str | None = None
    cast: list[str] | None = None
    cwm: str | None = None
    desc_long_seo: str | None = Field(None, alias='descLongSeo')
    editorial_warning_text: str | None = Field(None, alias='editorialWarningText')
    episode_name: str | None = Field(None, alias='episodeName')
    episode_name_long: str | None = Field(None, alias='episodeNameLong')
    episode_number: int | None = Field(None, alias='episodeNumber')
    genre_details: list[GenreDetail] | None = Field(None, alias='genreDetails')
    gracenote_id: str | None = Field(None, alias='gracenoteId')
    gracenote_series_id: str | None = Field(None, alias='gracenoteSeriesId')
    last_in_season: bool | None = Field(None, alias='lastInSeason')
    main_original_language: str | None = Field(None, alias='mainOriginalLanguage')
    merlin_alternate_id: str | None = Field(None, alias='merlinAlternateId')
    merlin_series_id: str | None = Field(None, alias='merlinSeriesId')
    nbcu_series_id: str | None = Field(None, alias='nbcuSeriesId')
    production_language: str | None = Field(None, alias='productionLanguage')
    provider_season_id: str | None = Field(None, alias='providerSeasonId')
    provider_series_id: str | None = Field(None, alias='providerSeriesId')
    season_id: UUID | None = Field(None, alias='seasonId')
    season_number: int | None = Field(None, alias='seasonNumber')
    series_id: UUID | None = Field(None, alias='seriesId')
    series_name: str | None = Field(None, alias='seriesName')
    series_native_id: str | None = Field(None, alias='seriesNativeId')
    sort_title: str | None = Field(None, alias='sortTitle')
    subtitled: bool | None = None
    synopsis: str | None = None
    synopsis_brief: str | None = Field(None, alias='synopsisBrief')
    title_seo: str | None = Field(None, alias='titleSeo')
    year: int | None = None
    advisory: list[AdvisoryItem2] | None = None

class ChildTypes8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    items: Items5

class Attributes8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    alttext: str
    checksum: str
    child_node_types: list[str] = Field(..., alias='childNodeTypes')
    created_date: NaiveDatetime = Field(..., alias='createdDate')
    expiration_date: NaiveDatetime = Field(..., alias='expirationDate')
    filename: str
    height: int
    language: str
    modified_date: NaiveDatetime = Field(..., alias='modifiedDate')
    title: str
    type: str
    url: str
    width: int

class Datum7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    links: Links
    id: UUID
    type: str
    child_types: ChildTypes8 = Field(..., alias='childTypes')
    attributes: Attributes8

class Images6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    data: list[Datum7]

class Relationships4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    images: Images6

class Datum6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    links: Links
    id: UUID
    type: str
    segment_id: str | None = Field(None, alias='segmentId')
    segment_name: str | None = Field(None, alias='segmentName')
    child_types: ChildTypes7 = Field(..., alias='childTypes')
    attributes: Attributes7
    relationships: Relationships4 | None = None

class Items8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    data: list[Datum6]

class Relationships3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    items: Items8

class Datum5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    links: Links
    id: UUID
    type: str
    segment_id: str = Field(..., alias='segmentId')
    segment_name: str = Field(..., alias='segmentName')
    child_types: ChildTypes6 = Field(..., alias='childTypes')
    attributes: Attributes6
    relationships: Relationships3

class Items6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    data: list[Datum5]

class Relationships2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    items: Items6

class Datum4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    links: Links
    id: UUID
    type: str
    segment_id: str = Field(..., alias='segmentId')
    segment_name: str = Field(..., alias='segmentName')
    group_segment_id: str = Field(..., alias='groupSegmentId')
    group_segment_name: str = Field(..., alias='groupSegmentName')
    child_types: ChildTypes5 = Field(..., alias='childTypes')
    attributes: Attributes5
    relationships: Relationships2

class Collections2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    data: list[Datum4]

class Relationships(BaseModel):
    model_config = ConfigDict(defer_build=True)
    recs: Recs
    items: Items2
    trailers: Trailers2
    collections: Collections2 | None = None

class ShowModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    links: Links
    id: UUID
    type: str
    child_types: ChildTypes = Field(..., alias='childTypes')
    attributes: Attributes
    relationships: Relationships
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
