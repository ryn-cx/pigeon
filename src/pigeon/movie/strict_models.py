from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from datetime import date, time
from typing import Any
from uuid import UUID
from pydantic import BaseModel, Field


class Links(BaseModel):
    model_config = ConfigDict(defer_build=True)
    self: str


class Images(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[str] = Field(..., alias="nodeTypes")
    count: int


class Shortforms(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[str] = Field(..., alias="nodeTypes")
    count: int


class Trailers(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[str] = Field(..., alias="nodeTypes")
    count: int


class Clips(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[str] = Field(..., alias="nodeTypes")
    count: int


class LinkedAssets(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[str] = Field(..., alias="nodeTypes")
    count: int


class ChildTypes(BaseModel):
    model_config = ConfigDict(defer_build=True)
    images: Images
    shortforms: Shortforms
    trailers: Trailers
    clips: Clips | None = None
    linked_assets: LinkedAssets | None = None


class AudienceLevelItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    scheme_provider: str = Field(..., alias="schemeProvider")
    segment_code: str = Field(..., alias="segmentCode")
    target_segment: str = Field(..., alias="targetSegment")


class VideoFormat(BaseModel):
    model_config = ConfigDict(defer_build=True)
    video_format: str = Field(..., alias="videoFormat")
    colour_spaces: list[str] = Field(..., alias="colourSpaces")
    audio_tracks: list[str] = Field(..., alias="audioTracks")


class Badging(BaseModel):
    model_config = ConfigDict(defer_build=True)
    video_formats: list[VideoFormat] = Field(..., alias="videoFormats")
    audio_tracks: list[str] = Field(..., alias="audioTracks")


class Channel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    access_channel: str = Field(..., alias="accessChannel")
    name: str


class DeviceAvailability(BaseModel):
    model_config = ConfigDict(defer_build=True)
    format: str
    media_type: str = Field(..., alias="mediaType")
    offer_stage: str = Field(..., alias="offerStage")
    offer_start_ts: int = Field(..., alias="offerStartTs")
    offer_end_ts: int = Field(..., alias="offerEndTs")
    streamable: bool
    downloadable: bool
    content_segment: str = Field(..., alias="contentSegment")
    video_format: str = Field(..., alias="videoFormat")
    video_format_variant: str = Field(..., alias="videoFormatVariant")
    colour_space: str = Field(..., alias="colourSpace")


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


class Availability(BaseModel):
    model_config = ConfigDict(defer_build=True)
    available: bool
    media_type: str | None = Field(None, alias="mediaType")
    offer_stage: str | None = Field(None, alias="offerStage")
    offer_start_ts: int | None = Field(None, alias="offerStartTs")
    offer_end_ts: int | None = Field(None, alias="offerEndTs")
    streamable: bool | None = None
    downloadable: bool | None = None
    available_devices: list[AvailableDevice] = Field(..., alias="availableDevices")
    extended_offer_start_ts: int | None = Field(None, alias="extendedOfferStartTs")
    extended_offer_end_ts: int | None = Field(None, alias="extendedOfferEndTs")
    content_segment: str | None = Field(None, alias="contentSegment")
    video_format: str | None = Field(None, alias="videoFormat")
    video_format_variant: str | None = Field(None, alias="videoFormatVariant")
    colour_space: str | None = Field(None, alias="colourSpace")


class Markers(BaseModel):
    model_config = ConfigDict(defer_build=True)
    socr: int = Field(..., alias="SOCR")
    solc: int | None = Field(None, alias="SOLC")
    eolc: int | None = Field(None, alias="EOLC")


class Hd(BaseModel):
    model_config = ConfigDict(defer_build=True)
    audio_tracks: AudioTracks = Field(..., alias="audioTracks")
    chapter_markers: list[None] = Field(..., alias="chapterMarkers")
    event_stage: str | None = Field(None, alias="eventStage")
    content_id: str = Field(..., alias="contentId")
    availability: Availability
    start_of_credits: int = Field(..., alias="startOfCredits")
    markers: Markers


class Formats(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hd: Hd = Field(..., alias="HD")


class GenreDetail(BaseModel):
    model_config = ConfigDict(defer_build=True)
    primary: bool
    type: str
    term_id: str = Field(..., alias="termId")
    term_description: str = Field(..., alias="termDescription")
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


class AlternativeDateItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    value: date
    date_type: str = Field(..., alias="dateType")
    territory: str


class FanCriticRatingItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    fan_score: int = Field(..., alias="fanScore")
    critic_score: int = Field(..., alias="criticScore")
    tags: list[str]


class PlacementTag(BaseModel):
    model_config = ConfigDict(defer_build=True)
    value: str
    primary: bool
    source: str


class Attributes(BaseModel):
    model_config = ConfigDict(defer_build=True)
    free_wheel_content_id: str = Field(..., alias="FreeWheelContentID")
    audience_level: list[AudienceLevelItem] | None = Field(None, alias="audienceLevel")
    audio_described: bool = Field(..., alias="audioDescribed")
    badging: Badging
    cast: list[str]
    channel: Channel
    chapters_enabled: bool = Field(..., alias="chaptersEnabled")
    child_node_types: list[str] = Field(..., alias="childNodeTypes")
    classification: list[str]
    closed_captioned: bool = Field(..., alias="closedCaptioned")
    collection_pdp: str = Field(..., alias="collectionPdp")
    content_segments: list[str] = Field(..., alias="contentSegments")
    created_date: int = Field(..., alias="createdDate")
    desc_long_seo: str = Field(..., alias="descLongSeo")
    device_availabilities: list[DeviceAvailability] | None = Field(
        None, alias="deviceAvailabilities"
    )
    device_availability: DeviceAvailability1 = Field(..., alias="deviceAvailability")
    director: list[str]
    duration_milliseconds: int = Field(..., alias="durationMilliseconds")
    duration_minutes: int = Field(..., alias="durationMinutes")
    duration_seconds: int = Field(..., alias="durationSeconds")
    editorial_warning_text: str | None = Field(None, alias="editorialWarningText")
    formats: Formats
    genre_details: list[GenreDetail] | None = Field(None, alias="genreDetails")
    genre_list: list[GenreListItem] = Field(..., alias="genreList")
    genres: list[str]
    gracenote_id: str = Field(..., alias="gracenoteId")
    images: list[Image]
    main_original_language: str = Field(..., alias="mainOriginalLanguage")
    merlin_alternate_id: str | None = Field(None, alias="merlinAlternateId")
    merlin_id: str = Field(..., alias="merlinId")
    native_id: str = Field(..., alias="nativeId")
    nbcu_id: str = Field(..., alias="nbcuId")
    ott_certificate: str = Field(..., alias="ottCertificate")
    production_language: str = Field(..., alias="productionLanguage")
    programme_uuid: UUID = Field(..., alias="programmeUuid")
    provider_id: str = Field(..., alias="providerId")
    provider_variant_id: UUID = Field(..., alias="providerVariantId")
    runtime: time
    section_navigation: str = Field(..., alias="sectionNavigation")
    slug: str
    sort_title: str = Field(..., alias="sortTitle")
    subtitled: bool
    synopsis: str
    synopsis_brief: str = Field(..., alias="synopsisBrief")
    synopsis_long: str = Field(..., alias="synopsisLong")
    synopsis_short: str = Field(..., alias="synopsisShort")
    target_audience: TargetAudience = Field(..., alias="targetAudience")
    title: str
    title_long: str = Field(..., alias="titleLong")
    title_medium: str = Field(..., alias="titleMedium")
    title_seo: str = Field(..., alias="titleSeo")
    year: int
    alternative_date: list[AlternativeDateItem] | None = Field(
        None, alias="alternativeDate"
    )
    cwm: str | None = None
    fan_critic_rating: list[FanCriticRatingItem] | None = Field(
        None, alias="fanCriticRating"
    )
    is_kids_content: bool | None = Field(None, alias="isKidsContent")
    placement_tags: list[PlacementTag] | None = Field(None, alias="placementTags")
    producer: list[str] | None = None
    rating: str | None = None
    rating_percentage: int | None = Field(None, alias="ratingPercentage")


class FirstEp(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[str] = Field(..., alias="nodeTypes")
    count: int


class FreeEpisodes(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[None] = Field(..., alias="nodeTypes")
    count: int


class Items(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[str] = Field(..., alias="nodeTypes")
    count: int


class Collections(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_types: list[str] = Field(..., alias="nodeTypes")
    count: int


class ChildTypes1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    images: Images
    shortforms: Shortforms | None = None
    trailers: Trailers | None = None
    first_ep: FirstEp | None = None
    free_episodes: FreeEpisodes | None = None
    items: Items | None = None
    clips: Clips | None = None
    linked_assets: LinkedAssets | None = None
    collections: Collections | None = None


class Term(BaseModel):
    model_config = ConfigDict(defer_build=True)
    description: str
    abbreviation: str | None = None


class AdvisoryItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    terms: list[Term]
    id: str
    group: int


class Badging1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    video_formats: list[VideoFormat] = Field(..., alias="videoFormats")
    audio_tracks: list[str] = Field(..., alias="audioTracks")


class DeviceAvailability2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    format: str
    media_type: str = Field(..., alias="mediaType")
    offer_stage: str = Field(..., alias="offerStage")
    offer_start_ts: int = Field(..., alias="offerStartTs")
    offer_end_ts: int = Field(..., alias="offerEndTs")
    streamable: bool | None = None
    downloadable: bool | None = None
    content_segment: str = Field(..., alias="contentSegment")
    video_format: str = Field(..., alias="videoFormat")
    video_format_variant: str = Field(..., alias="videoFormatVariant")
    colour_space: str = Field(..., alias="colourSpace")


class DeviceAvailability3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    available: bool


class Restriction(BaseModel):
    model_config = ConfigDict(defer_build=True)
    usage: str
    type: str
    platform_capability: None = Field(..., alias="platformCapability")
    value: str
    parameters: list[None]


class Availability1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    available: bool
    media_type: str = Field(..., alias="mediaType")
    offer_stage: str = Field(..., alias="offerStage")
    offer_start_ts: int = Field(..., alias="offerStartTs")
    offer_end_ts: int = Field(..., alias="offerEndTs")
    streamable: bool | None = None
    downloadable: bool | None = None
    available_devices: list[AvailableDevice] = Field(..., alias="availableDevices")
    extended_offer_start_ts: int = Field(..., alias="extendedOfferStartTs")
    extended_offer_end_ts: int = Field(..., alias="extendedOfferEndTs")
    content_segment: str = Field(..., alias="contentSegment")
    video_format: str = Field(..., alias="videoFormat")
    video_format_variant: str = Field(..., alias="videoFormatVariant")
    colour_space: str = Field(..., alias="colourSpace")
    free_offer_end_ts: int | None = Field(None, alias="freeOfferEndTs")
    restrictions: list[Restriction] | None = None


class Hd1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    audio_tracks: AudioTracks = Field(..., alias="audioTracks")
    chapter_markers: list[None] = Field(..., alias="chapterMarkers")
    event_stage: str = Field(..., alias="eventStage")
    content_id: str | None = Field(None, alias="contentId")
    availability: Availability1
    start_of_credits: int = Field(..., alias="startOfCredits")
    markers: Markers | None = None


class Formats1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hd: Hd1 = Field(..., alias="HD")


class MediaType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    media_type: str = Field(..., alias="mediaType")
    count: int
    latest: int


class FanCriticRatingItem1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    fan_score: int = Field(..., alias="fanScore")
    critic_score: int = Field(..., alias="criticScore")
    tags: list[str] | None = None


class Attributes1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    free_wheel_content_id: str = Field(..., alias="FreeWheelContentID")
    advisory: list[AdvisoryItem] | None = None
    audience_level: list[AudienceLevelItem] | None = Field(None, alias="audienceLevel")
    audio_described: bool = Field(..., alias="audioDescribed")
    badging: Badging1
    cast: list[str] | None = None
    channel: Channel
    chapters_enabled: bool = Field(..., alias="chaptersEnabled")
    child_node_types: list[str] = Field(..., alias="childNodeTypes")
    classification: list[str]
    closed_captioned: bool | None = Field(None, alias="closedCaptioned")
    content_segments: list[str] = Field(..., alias="contentSegments")
    created_date: int = Field(..., alias="createdDate")
    desc_long_seo: str = Field(..., alias="descLongSeo")
    device_availabilities: list[DeviceAvailability2] = Field(
        ..., alias="deviceAvailabilities"
    )
    device_availability: DeviceAvailability3 = Field(..., alias="deviceAvailability")
    director: list[str] | None = None
    duration_milliseconds: int | None = Field(None, alias="durationMilliseconds")
    duration_minutes: int | None = Field(None, alias="durationMinutes")
    duration_seconds: int | None = Field(None, alias="durationSeconds")
    editorial_warning_text: str | None = Field(None, alias="editorialWarningText")
    formats: Formats1
    genre_details: list[GenreDetail] | None = Field(None, alias="genreDetails")
    genre_list: list[GenreListItem] = Field(..., alias="genreList")
    genres: list[str]
    gracenote_id: str = Field(..., alias="gracenoteId")
    images: list[Image]
    main_original_language: str | None = Field(None, alias="mainOriginalLanguage")
    merlin_alternate_id: str | None = Field(None, alias="merlinAlternateId")
    merlin_id: str = Field(..., alias="merlinId")
    native_id: str | None = Field(None, alias="nativeId")
    nbcu_id: str = Field(..., alias="nbcuId")
    ott_certificate: str = Field(..., alias="ottCertificate")
    producer: list[str] | None = None
    production_language: str | None = Field(None, alias="productionLanguage")
    programme_uuid: UUID | None = Field(None, alias="programmeUuid")
    provider_id: str | None = Field(None, alias="providerId")
    provider_variant_id: UUID | None = Field(None, alias="providerVariantId")
    runtime: time | None = None
    section_navigation: str = Field(..., alias="sectionNavigation")
    slug: str
    sort_title: str = Field(..., alias="sortTitle")
    subtitled: bool | None = None
    synopsis: str | None = None
    synopsis_brief: str | None = Field(None, alias="synopsisBrief")
    synopsis_long: str = Field(..., alias="synopsisLong")
    synopsis_short: str = Field(..., alias="synopsisShort")
    target_audience: TargetAudience = Field(..., alias="targetAudience")
    title: str
    title_long: str | None = Field(None, alias="titleLong")
    title_medium: str = Field(..., alias="titleMedium")
    title_seo: str = Field(..., alias="titleSeo")
    year: int | None = None
    available_episode_count: int | None = Field(None, alias="availableEpisodeCount")
    available_season_count: int | None = Field(None, alias="availableSeasonCount")
    brands: list[str] | None = None
    gracenote_series_id: str | None = Field(None, alias="gracenoteSeriesId")
    media_types: list[MediaType] | None = Field(None, alias="mediaTypes")
    merlin_series_id: str | None = Field(None, alias="merlinSeriesId")
    nbcu_series_id: str | None = Field(None, alias="nbcuSeriesId")
    provider_series_id: str | None = Field(None, alias="providerSeriesId")
    reverse_order: bool | None = Field(None, alias="reverseOrder")
    series_native_id: str | None = Field(None, alias="seriesNativeId")
    series_uuid: UUID | None = Field(None, alias="seriesUuid")
    smart_call_to_action: str | None = Field(None, alias="smartCallToAction")
    cwm: str | None = None
    alternative_date: list[AlternativeDateItem] | None = Field(
        None, alias="alternativeDate"
    )
    fan_critic_rating: list[FanCriticRatingItem1] | None = Field(
        None, alias="fanCriticRating"
    )
    is_kids_content: bool | None = Field(None, alias="isKidsContent")
    placement_tags: list[PlacementTag] | None = Field(None, alias="placementTags")
    rating: str | None = None
    rating_percentage: int | None = Field(None, alias="ratingPercentage")
    privacy_restrictions: list[str] | None = Field(None, alias="privacyRestrictions")


class Datum(BaseModel):
    model_config = ConfigDict(defer_build=True)
    links: Links
    id: UUID
    type: str
    child_types: ChildTypes1 = Field(..., alias="childTypes")
    attributes: Attributes1


class Recs(BaseModel):
    model_config = ConfigDict(defer_build=True)
    data: list[Datum]


class ChildTypes2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    images: Images


class Badging2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    video_formats: list[VideoFormat] = Field(..., alias="videoFormats")
    audio_tracks: list[str] = Field(..., alias="audioTracks")


class DeviceAvailability4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    format: str
    media_type: str = Field(..., alias="mediaType")
    offer_stage: str = Field(..., alias="offerStage")
    offer_start_ts: int = Field(..., alias="offerStartTs")
    offer_end_ts: int = Field(..., alias="offerEndTs")
    streamable: bool
    downloadable: bool
    content_segment: str = Field(..., alias="contentSegment")
    video_format: str = Field(..., alias="videoFormat")
    video_format_variant: str = Field(..., alias="videoFormatVariant")
    colour_space: str = Field(..., alias="colourSpace")


class DeviceAvailability5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    available: bool


class AudioTracks2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    eng: list[str]


class Availability2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    available: bool
    media_type: str = Field(..., alias="mediaType")
    offer_stage: str = Field(..., alias="offerStage")
    offer_start_ts: int = Field(..., alias="offerStartTs")
    offer_end_ts: int = Field(..., alias="offerEndTs")
    streamable: bool
    downloadable: bool
    available_devices: list[AvailableDevice] = Field(..., alias="availableDevices")
    extended_offer_start_ts: int = Field(..., alias="extendedOfferStartTs")
    extended_offer_end_ts: int = Field(..., alias="extendedOfferEndTs")
    content_segment: str = Field(..., alias="contentSegment")
    video_format: str = Field(..., alias="videoFormat")
    video_format_variant: str = Field(..., alias="videoFormatVariant")
    colour_space: str = Field(..., alias="colourSpace")
    restrictions: list[Restriction] | None = None


class Hd2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    audio_tracks: AudioTracks2 = Field(..., alias="audioTracks")
    chapter_markers: list[None] = Field(..., alias="chapterMarkers")
    event_stage: str = Field(..., alias="eventStage")
    content_id: str = Field(..., alias="contentId")
    availability: Availability2
    start_of_credits: int = Field(..., alias="startOfCredits")


class Formats2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hd: Hd2 = Field(..., alias="HD")


class Hd3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content_id: str = Field(..., alias="contentId")


class Uhdsdr(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content_id: str = Field(..., alias="contentId")


class Uhdhdr(BaseModel):
    model_config = ConfigDict(defer_build=True)
    content_id: str = Field(..., alias="contentId")


class Formats3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    hd: Hd3 = Field(..., alias="HD")
    uhdsdr: Uhdsdr | None = Field(None, alias="UHDSDR")
    uhdhdr: Uhdhdr | None = Field(None, alias="UHDHDR")


class MainTitleInfoItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    node_id: UUID = Field(..., alias="nodeId")
    type: str
    programme_uuid: UUID = Field(..., alias="programmeUuid")
    provider_variant_id: UUID = Field(..., alias="providerVariantId")
    formats: Formats3
    content_segments: list[str] = Field(..., alias="contentSegments")


class FanCriticRatingItem2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    fan_score: int = Field(..., alias="fanScore")
    critic_score: int = Field(..., alias="criticScore")
    tags: list[str]


class Attributes2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    free_wheel_content_id: str = Field(..., alias="FreeWheelContentID")
    audio_described: bool = Field(..., alias="audioDescribed")
    autoplay: bool
    badging: Badging2
    channel: Channel
    chapters_enabled: bool = Field(..., alias="chaptersEnabled")
    child_node_types: list[str] = Field(..., alias="childNodeTypes")
    classification: list[str]
    closed_captioned: bool = Field(..., alias="closedCaptioned")
    content_segments: list[str] = Field(..., alias="contentSegments")
    created_date: int = Field(..., alias="createdDate")
    device_availabilities: list[DeviceAvailability4] = Field(
        ..., alias="deviceAvailabilities"
    )
    device_availability: DeviceAvailability5 = Field(..., alias="deviceAvailability")
    duration_milliseconds: int = Field(..., alias="durationMilliseconds")
    duration_minutes: int = Field(..., alias="durationMinutes")
    duration_seconds: int = Field(..., alias="durationSeconds")
    formats: Formats2
    free_wheel_creative_id: str = Field(..., alias="freeWheelCreativeId")
    genre_list: list[GenreListItem] = Field(..., alias="genreList")
    genres: list[str]
    images: list[Image]
    main_title_info: list[MainTitleInfoItem] = Field(..., alias="mainTitleInfo")
    merlin_id: str = Field(..., alias="merlinId")
    nbcu_id: str = Field(..., alias="nbcuId")
    ott_certificate: str = Field(..., alias="ottCertificate")
    programme_uuid: UUID = Field(..., alias="programmeUuid")
    provider_id: str = Field(..., alias="providerId")
    provider_variant_id: UUID = Field(..., alias="providerVariantId")
    runtime: time
    slug: str
    synopsis_long: str = Field(..., alias="synopsisLong")
    synopsis_short: str = Field(..., alias="synopsisShort")
    target_audience: TargetAudience = Field(..., alias="targetAudience")
    title: str
    title_long: str = Field(..., alias="titleLong")
    title_medium: str = Field(..., alias="titleMedium")
    alternative_date: list[AlternativeDateItem] | None = Field(
        None, alias="alternativeDate"
    )
    cwm: str | None = None
    fan_critic_rating: list[FanCriticRatingItem2] | None = Field(
        None, alias="fanCriticRating"
    )
    is_kids_content: bool | None = Field(None, alias="isKidsContent")
    privacy_restrictions: list[str] | None = Field(None, alias="privacyRestrictions")
    subtitled: bool | None = None


class Datum1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    links: Links
    id: UUID
    type: str
    child_types: ChildTypes2 = Field(..., alias="childTypes")
    attributes: Attributes2


class Trailers2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    data: list[Datum1]


class Relationships(BaseModel):
    model_config = ConfigDict(defer_build=True)
    recs: Recs
    trailers: Trailers2


class MovieModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    links: Links
    id: UUID
    type: str
    child_types: ChildTypes = Field(..., alias="childTypes")
    attributes: Attributes
    relationships: Relationships
    _raw_input: Any = PrivateAttr(default=None)

    @model_validator(mode="wrap")
    @classmethod
    def _capture_raw_input(
        cls, data: Any, handler: ModelWrapValidatorHandler[Self]
    ) -> Self:
        """Validate the model and keep the input it was built from."""
        model = handler(data)
        model._raw_input = data
        return model

    @property
    def raw_input(self) -> Any:
        """The input this model was validated from, as it was handed over."""
        return self._raw_input
