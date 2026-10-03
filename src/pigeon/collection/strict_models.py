from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from datetime import date, time
from typing import Any
from uuid import UUID
from pydantic import AwareDatetime, BaseModel, Field

class Links(BaseModel):
    model_config = ConfigDict(defer_build=True)
    self: str

class NextItems(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[str] = Field(..., alias='nodeTypes')
    count: int

class Items(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[str] = Field(..., alias='nodeTypes')
    count: int

class CurationConfig(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[str] = Field(..., alias='nodeTypes')
    count: int

class ChildTypes(BaseModel):
    model_config = ConfigDict(defer_build=True)
    next_items: NextItems | None = None
    items: Items
    curation_config: CurationConfig | None = Field(None, alias='curation-config')

class RenderHint(BaseModel):
    model_config = ConfigDict(defer_build=True)
    orientation: str
    sort: str | None = None
    image_template: str | None = Field(None, alias='imageTemplate')

class Attributes(BaseModel):
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
    render_hint: RenderHint = Field(..., alias='renderHint')
    section_navigation: str = Field(..., alias='sectionNavigation')
    slug: str
    sort_policy: str = Field(..., alias='sortPolicy')
    title: str
    collection_id: str | None = Field(None, alias='collectionId')
    seo_title: str | None = Field(None, alias='seoTitle')

class Images(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[str] = Field(..., alias='nodeTypes')
    count: int

class Shortforms(BaseModel):
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

class Clips(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[str] = Field(..., alias='nodeTypes')
    count: int

class Campaigns(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[str] = Field(..., alias='nodeTypes')
    count: int

class FirstEp(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[str] = Field(..., alias='nodeTypes')
    count: int

class FreeEpisodes(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[str] = Field(..., alias='nodeTypes')
    count: int

class Latest(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[str] = Field(..., alias='nodeTypes')
    count: int

class LinkedAssets(BaseModel):
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
    shortforms: Shortforms | None = None
    trailers: Trailers | None = None
    collections: Collections | None = None
    clips: Clips | None = None
    campaigns: Campaigns | None = None
    first_ep: FirstEp | None = None
    free_episodes: FreeEpisodes | None = None
    items: Items | None = None
    latest: Latest | None = None
    linked_assets: LinkedAssets | None = None
    next_clips: NextClips | None = None
    next_shortforms: NextShortforms | None = None

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

class RenderHint1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    template: str

class TuneInBadging(BaseModel):
    model_config = ConfigDict(defer_build=True)
    tune_in_badging_editorial_texts: TuneInBadgingEditorialTexts | None = Field(None, alias='tuneInBadgingEditorialTexts')
    message: str | None = None
    render_hint: RenderHint1 | None = Field(None, alias='renderHint')
    value: AwareDatetime | None = None

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
    streamable: bool | None = None
    downloadable: bool | None = None
    content_segment: str = Field(..., alias='contentSegment')
    video_format: str | None = Field(None, alias='videoFormat')
    video_format_variant: str | None = Field(None, alias='videoFormatVariant')
    colour_space: str | None = Field(None, alias='colourSpace')

class DeviceAvailability1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    available: bool

class AudioTracks(BaseModel):
    model_config = ConfigDict(defer_build=True)
    eng: list[str]
    spa: list[str] | None = None

class AvailableDevice(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    platform: str

class Restriction(BaseModel):
    model_config = ConfigDict(defer_build=True)
    usage: str
    type: str
    platform_capability: None = Field(..., alias='platformCapability')
    value: str
    parameters: list[None]

class Availability(BaseModel):
    model_config = ConfigDict(defer_build=True)
    available: bool
    media_type: str = Field(..., alias='mediaType')
    offer_stage: str = Field(..., alias='offerStage')
    offer_start_ts: int = Field(..., alias='offerStartTs')
    offer_end_ts: int = Field(..., alias='offerEndTs')
    streamable: bool | None = None
    downloadable: bool | None = None
    available_devices: list[AvailableDevice] = Field(..., alias='availableDevices')
    extended_offer_start_ts: int = Field(..., alias='extendedOfferStartTs')
    extended_offer_end_ts: int = Field(..., alias='extendedOfferEndTs')
    content_segment: str = Field(..., alias='contentSegment')
    video_format: str = Field(..., alias='videoFormat')
    video_format_variant: str = Field(..., alias='videoFormatVariant')
    colour_space: str = Field(..., alias='colourSpace')
    restrictions: list[Restriction] | None = None
    free_offer_end_ts: int | None = Field(None, alias='freeOfferEndTs')

class Markers(BaseModel):
    model_config = ConfigDict(defer_build=True)
    socr: int = Field(..., alias='SOCR')
    solc: int | None = Field(None, alias='SOLC')
    eolc: int | None = Field(None, alias='EOLC')
    soi: int | None = Field(None, alias='SOI')
    hsi: int | None = Field(None, alias='HSI')
    spi: int | None = Field(None, alias='SPI')

class Hd(BaseModel):
    model_config = ConfigDict(defer_build=True)
    audio_tracks: AudioTracks = Field(..., alias='audioTracks')
    chapter_markers: list[None] = Field(..., alias='chapterMarkers')
    event_stage: str = Field(..., alias='eventStage')
    content_id: str | None = Field(None, alias='contentId')
    availability: Availability
    start_of_credits: int = Field(..., alias='startOfCredits')
    markers: Markers | None = None

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

class TargetAudience(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str

class Term(BaseModel):
    model_config = ConfigDict(defer_build=True)
    description: str
    abbreviation: str | None = None

class AdvisoryItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    terms: list[Term]
    id: str
    group: int

class AlternativeDateItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    value: date
    date_type: str = Field(..., alias='dateType')
    territory: str

class FanCriticRatingItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    fan_score: int | None = Field(None, alias='fanScore')
    critic_score: int | None = Field(None, alias='criticScore')
    tags: list[str] | None = None

class PlacementTag(BaseModel):
    model_config = ConfigDict(defer_build=True)
    value: str
    primary: bool
    source: str | None = None

class MediaType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    media_type: str = Field(..., alias='mediaType')
    count: int
    latest: int

class Fact(BaseModel):
    model_config = ConfigDict(defer_build=True)
    fact_icon: str = Field(..., alias='factIcon')
    fact_text: str = Field(..., alias='factText')

class Attributes1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    free_wheel_content_id: str = Field(..., alias='FreeWheelContentID')
    audience_level: list[AudienceLevelItem] | None = Field(None, alias='audienceLevel')
    audio_described: bool = Field(..., alias='audioDescribed')
    badging: Badging
    cast: list[str] | None = None
    channel: Channel
    chapters_enabled: bool = Field(..., alias='chaptersEnabled')
    child_node_types: list[str] = Field(..., alias='childNodeTypes')
    classification: list[str]
    closed_captioned: bool | None = Field(None, alias='closedCaptioned')
    content_segments: list[str] = Field(..., alias='contentSegments')
    created_date: int = Field(..., alias='createdDate')
    desc_long_seo: str = Field(..., alias='descLongSeo')
    device_availabilities: list[DeviceAvailability] = Field(..., alias='deviceAvailabilities')
    device_availability: DeviceAvailability1 = Field(..., alias='deviceAvailability')
    duration_milliseconds: int | None = Field(None, alias='durationMilliseconds')
    duration_minutes: int | None = Field(None, alias='durationMinutes')
    duration_seconds: int | None = Field(None, alias='durationSeconds')
    editorial_warning_text: str | None = Field(None, alias='editorialWarningText')
    formats: Formats
    genre_details: list[GenreDetail] | None = Field(None, alias='genreDetails')
    genre_list: list[GenreListItem] = Field(..., alias='genreList')
    genres: list[str]
    gracenote_id: str | None = Field(None, alias='gracenoteId')
    images: list[Image]
    is_kids_content: bool | None = Field(None, alias='isKidsContent')
    main_original_language: str | None = Field(None, alias='mainOriginalLanguage')
    merlin_alternate_id: str | None = Field(None, alias='merlinAlternateId')
    merlin_id: str = Field(..., alias='merlinId')
    native_id: str | None = Field(None, alias='nativeId')
    nbcu_id: str = Field(..., alias='nbcuId')
    ott_certificate: str | None = Field(None, alias='ottCertificate')
    privacy_restrictions: list[str] | None = Field(None, alias='privacyRestrictions')
    production_language: str | None = Field(None, alias='productionLanguage')
    programme_uuid: UUID | None = Field(None, alias='programmeUuid')
    promoted_item: bool = Field(..., alias='promotedItem')
    provider_id: str | None = Field(None, alias='providerId')
    provider_variant_id: UUID | None = Field(None, alias='providerVariantId')
    runtime: time | None = None
    section_navigation: str = Field(..., alias='sectionNavigation')
    slug: str
    sort_title: str = Field(..., alias='sortTitle')
    subtitled: bool | None = None
    synopsis: str | None = None
    synopsis_brief: str | None = Field(None, alias='synopsisBrief')
    synopsis_long: str = Field(..., alias='synopsisLong')
    synopsis_short: str | None = Field(None, alias='synopsisShort')
    target_audience: TargetAudience | None = Field(None, alias='targetAudience')
    title: str
    title_long: str | None = Field(None, alias='titleLong')
    title_medium: str = Field(..., alias='titleMedium')
    title_seo: str = Field(..., alias='titleSeo')
    year: int | None = None
    director: list[str] | None = None
    advisory: list[AdvisoryItem] | None = None
    alternative_date: list[AlternativeDateItem] | None = Field(None, alias='alternativeDate')
    cwm: str | None = None
    fan_critic_rating: list[FanCriticRatingItem] | None = Field(None, alias='fanCriticRating')
    producer: list[str] | None = None
    rating: str | None = None
    rating_percentage: int | None = Field(None, alias='ratingPercentage')
    placement_tags: list[PlacementTag] | None = Field(None, alias='placementTags')
    available_episode_count: int | None = Field(None, alias='availableEpisodeCount')
    available_season_count: int | None = Field(None, alias='availableSeasonCount')
    brands: list[str] | None = None
    gracenote_series_id: str | None = Field(None, alias='gracenoteSeriesId')
    media_types: list[MediaType] | None = Field(None, alias='mediaTypes')
    merlin_series_id: str | None = Field(None, alias='merlinSeriesId')
    nbcu_series_id: str | None = Field(None, alias='nbcuSeriesId')
    provider_series_id: str | None = Field(None, alias='providerSeriesId')
    reverse_order: bool | None = Field(None, alias='reverseOrder')
    series_native_id: str | None = Field(None, alias='seriesNativeId')
    series_uuid: UUID | None = Field(None, alias='seriesUuid')
    smart_call_to_action: str | None = Field(None, alias='smartCallToAction')
    title_medium_seo: str | None = Field(None, alias='titleMediumSeo')
    desc_short_seo: str | None = Field(None, alias='descShortSeo')
    unlock_slug: bool | None = Field(None, alias='unlockSlug')
    facts: list[Fact] | None = None
    channel_logo_hide_value: str | None = Field(None, alias='channelLogoHideValue')

class Datum(BaseModel):
    model_config = ConfigDict(defer_build=True)
    links: Links
    id: UUID
    type: str
    child_types: ChildTypes1 = Field(..., alias='childTypes')
    attributes: Attributes1

class Items1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    data: list[Datum]

class Relationships(BaseModel):
    model_config = ConfigDict(defer_build=True)
    items: Items1

class CollectionModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    links: Links
    id: UUID
    type: str
    segment_id: str = Field(..., alias='segmentId')
    segment_name: str = Field(..., alias='segmentName')
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
