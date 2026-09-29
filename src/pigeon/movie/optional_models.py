from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from datetime import date, time
from typing import Any
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field


class Links(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    self: str | Any = Field(default=None, union_mode="left_to_right")


class Images(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    node_types: list[str] | Any = Field(
        None, alias="nodeTypes", union_mode="left_to_right"
    )
    count: int | Any = Field(default=None, union_mode="left_to_right")


class Shortforms(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    node_types: list[str] | Any = Field(
        None, alias="nodeTypes", union_mode="left_to_right"
    )
    count: int | Any = Field(default=None, union_mode="left_to_right")


class Trailers(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    node_types: list[str] | Any = Field(
        None, alias="nodeTypes", union_mode="left_to_right"
    )
    count: int | Any = Field(default=None, union_mode="left_to_right")


class Clips(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    node_types: list[str] | Any = Field(
        None, alias="nodeTypes", union_mode="left_to_right"
    )
    count: int | Any = Field(default=None, union_mode="left_to_right")


class LinkedAssets(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    node_types: list[str] | Any = Field(
        None, alias="nodeTypes", union_mode="left_to_right"
    )
    count: int | Any = Field(default=None, union_mode="left_to_right")


class ChildTypes(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    images: Images | Any = Field(default=None, union_mode="left_to_right")
    shortforms: Shortforms | Any = Field(default=None, union_mode="left_to_right")
    trailers: Trailers | Any = Field(default=None, union_mode="left_to_right")
    clips: Clips | Any = Field(default=None, union_mode="left_to_right")
    linked_assets: LinkedAssets | Any = Field(default=None, union_mode="left_to_right")


class AudienceLevelItem(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    scheme_provider: str | Any = Field(
        None, alias="schemeProvider", union_mode="left_to_right"
    )
    segment_code: str | Any = Field(
        None, alias="segmentCode", union_mode="left_to_right"
    )
    target_segment: str | Any = Field(
        None, alias="targetSegment", union_mode="left_to_right"
    )


class VideoFormat(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    video_format: str | Any = Field(
        None, alias="videoFormat", union_mode="left_to_right"
    )
    colour_spaces: list[str] | Any = Field(
        None, alias="colourSpaces", union_mode="left_to_right"
    )
    audio_tracks: list[str] | Any = Field(
        None, alias="audioTracks", union_mode="left_to_right"
    )


class Badging(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    video_formats: list[VideoFormat] | Any = Field(
        None, alias="videoFormats", union_mode="left_to_right"
    )
    audio_tracks: list[str] | Any = Field(
        None, alias="audioTracks", union_mode="left_to_right"
    )


class Channel(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    access_channel: str | Any = Field(
        None, alias="accessChannel", union_mode="left_to_right"
    )
    name: str | Any = Field(default=None, union_mode="left_to_right")


class DeviceAvailability(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    format: str | Any = Field(default=None, union_mode="left_to_right")
    media_type: str | Any = Field(None, alias="mediaType", union_mode="left_to_right")
    offer_stage: str | Any = Field(None, alias="offerStage", union_mode="left_to_right")
    offer_start_ts: int | Any = Field(
        None, alias="offerStartTs", union_mode="left_to_right"
    )
    offer_end_ts: int | Any = Field(
        None, alias="offerEndTs", union_mode="left_to_right"
    )
    streamable: bool | Any = Field(default=None, union_mode="left_to_right")
    downloadable: bool | Any = Field(default=None, union_mode="left_to_right")
    content_segment: str | Any = Field(
        None, alias="contentSegment", union_mode="left_to_right"
    )
    video_format: str | Any = Field(
        None, alias="videoFormat", union_mode="left_to_right"
    )
    video_format_variant: str | Any = Field(
        None, alias="videoFormatVariant", union_mode="left_to_right"
    )
    colour_space: str | Any = Field(
        None, alias="colourSpace", union_mode="left_to_right"
    )


class DeviceAvailability1(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    available: bool | Any = Field(default=None, union_mode="left_to_right")


class AudioTracks(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    eng: list[str] | Any = Field(default=None, union_mode="left_to_right")
    spa: list[str] | Any = Field(default=None, union_mode="left_to_right")


class AvailableDevice(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    type: str | Any = Field(default=None, union_mode="left_to_right")
    platform: str | Any = Field(default=None, union_mode="left_to_right")


class Availability(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    available: bool | Any = Field(default=None, union_mode="left_to_right")
    media_type: str | Any = Field(None, alias="mediaType", union_mode="left_to_right")
    offer_stage: str | Any = Field(None, alias="offerStage", union_mode="left_to_right")
    offer_start_ts: int | Any = Field(
        None, alias="offerStartTs", union_mode="left_to_right"
    )
    offer_end_ts: int | Any = Field(
        None, alias="offerEndTs", union_mode="left_to_right"
    )
    streamable: bool | Any = Field(default=None, union_mode="left_to_right")
    downloadable: bool | Any = Field(default=None, union_mode="left_to_right")
    available_devices: list[AvailableDevice] | Any = Field(
        None, alias="availableDevices", union_mode="left_to_right"
    )
    extended_offer_start_ts: int | Any = Field(
        None, alias="extendedOfferStartTs", union_mode="left_to_right"
    )
    extended_offer_end_ts: int | Any = Field(
        None, alias="extendedOfferEndTs", union_mode="left_to_right"
    )
    content_segment: str | Any = Field(
        None, alias="contentSegment", union_mode="left_to_right"
    )
    video_format: str | Any = Field(
        None, alias="videoFormat", union_mode="left_to_right"
    )
    video_format_variant: str | Any = Field(
        None, alias="videoFormatVariant", union_mode="left_to_right"
    )
    colour_space: str | Any = Field(
        None, alias="colourSpace", union_mode="left_to_right"
    )


class Markers(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    socr: int | Any = Field(None, alias="SOCR", union_mode="left_to_right")


class Hd(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    audio_tracks: AudioTracks | Any = Field(
        None, alias="audioTracks", union_mode="left_to_right"
    )
    chapter_markers: list[Any] | Any = Field(
        None, alias="chapterMarkers", union_mode="left_to_right"
    )
    event_stage: str | Any = Field(None, alias="eventStage", union_mode="left_to_right")
    content_id: str | Any = Field(None, alias="contentId", union_mode="left_to_right")
    availability: Availability | Any = Field(default=None, union_mode="left_to_right")
    start_of_credits: int | Any = Field(
        None, alias="startOfCredits", union_mode="left_to_right"
    )
    markers: Markers | Any = Field(default=None, union_mode="left_to_right")


class Formats(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    hd: Hd | Any = Field(None, alias="HD", union_mode="left_to_right")


class GenreDetail(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    primary: bool | Any = Field(default=None, union_mode="left_to_right")
    type: str | Any = Field(default=None, union_mode="left_to_right")
    term_id: str | Any = Field(None, alias="termId", union_mode="left_to_right")
    term_description: str | Any = Field(
        None, alias="termDescription", union_mode="left_to_right"
    )
    code: str | Any = Field(default=None, union_mode="left_to_right")


class GenreListItem(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    subgenre: list[str] | Any = Field(default=None, union_mode="left_to_right")
    genre: list[str] | Any = Field(default=None, union_mode="left_to_right")


class Image(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    url: str | Any = Field(default=None, union_mode="left_to_right")
    type: str | Any = Field(default=None, union_mode="left_to_right")


class TargetAudience(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    id: str | Any = Field(default=None, union_mode="left_to_right")


class AlternativeDateItem(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    type: str | Any = Field(default=None, union_mode="left_to_right")
    value: date | Any = Field(default=None, union_mode="left_to_right")
    date_type: str | Any = Field(None, alias="dateType", union_mode="left_to_right")
    territory: str | Any = Field(default=None, union_mode="left_to_right")


class FanCriticRatingItem(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    source: str | Any = Field(default=None, union_mode="left_to_right")
    fan_score: int | Any = Field(None, alias="fanScore", union_mode="left_to_right")
    critic_score: int | Any = Field(
        None, alias="criticScore", union_mode="left_to_right"
    )
    tags: list[str] | Any = Field(default=None, union_mode="left_to_right")


class PlacementTag(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    value: str | Any = Field(default=None, union_mode="left_to_right")
    primary: bool | Any = Field(default=None, union_mode="left_to_right")
    source: str | Any = Field(default=None, union_mode="left_to_right")


class Attributes(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    free_wheel_content_id: str | Any = Field(
        None, alias="FreeWheelContentID", union_mode="left_to_right"
    )
    audience_level: list[AudienceLevelItem] | Any = Field(
        None, alias="audienceLevel", union_mode="left_to_right"
    )
    audio_described: bool | Any = Field(
        None, alias="audioDescribed", union_mode="left_to_right"
    )
    badging: Badging | Any = Field(default=None, union_mode="left_to_right")
    cast: list[str] | Any = Field(default=None, union_mode="left_to_right")
    channel: Channel | Any = Field(default=None, union_mode="left_to_right")
    chapters_enabled: bool | Any = Field(
        None, alias="chaptersEnabled", union_mode="left_to_right"
    )
    child_node_types: list[str] | Any = Field(
        None, alias="childNodeTypes", union_mode="left_to_right"
    )
    classification: list[str] | Any = Field(default=None, union_mode="left_to_right")
    closed_captioned: bool | Any = Field(
        None, alias="closedCaptioned", union_mode="left_to_right"
    )
    collection_pdp: str | Any = Field(
        None, alias="collectionPdp", union_mode="left_to_right"
    )
    content_segments: list[str] | Any = Field(
        None, alias="contentSegments", union_mode="left_to_right"
    )
    created_date: int | Any = Field(
        None, alias="createdDate", union_mode="left_to_right"
    )
    desc_long_seo: str | Any = Field(
        None, alias="descLongSeo", union_mode="left_to_right"
    )
    device_availabilities: list[DeviceAvailability] | Any = Field(
        None, alias="deviceAvailabilities", union_mode="left_to_right"
    )
    device_availability: DeviceAvailability1 | Any = Field(
        None, alias="deviceAvailability", union_mode="left_to_right"
    )
    director: list[str] | Any = Field(default=None, union_mode="left_to_right")
    duration_milliseconds: int | Any = Field(
        None, alias="durationMilliseconds", union_mode="left_to_right"
    )
    duration_minutes: int | Any = Field(
        None, alias="durationMinutes", union_mode="left_to_right"
    )
    duration_seconds: int | Any = Field(
        None, alias="durationSeconds", union_mode="left_to_right"
    )
    editorial_warning_text: str | Any = Field(
        None, alias="editorialWarningText", union_mode="left_to_right"
    )
    formats: Formats | Any = Field(default=None, union_mode="left_to_right")
    genre_details: list[GenreDetail] | Any = Field(
        None, alias="genreDetails", union_mode="left_to_right"
    )
    genre_list: list[GenreListItem] | Any = Field(
        None, alias="genreList", union_mode="left_to_right"
    )
    genres: list[str] | Any = Field(default=None, union_mode="left_to_right")
    gracenote_id: str | Any = Field(
        None, alias="gracenoteId", union_mode="left_to_right"
    )
    images: list[Image] | Any = Field(default=None, union_mode="left_to_right")
    main_original_language: str | Any = Field(
        None, alias="mainOriginalLanguage", union_mode="left_to_right"
    )
    merlin_alternate_id: str | Any = Field(
        None, alias="merlinAlternateId", union_mode="left_to_right"
    )
    merlin_id: str | Any = Field(None, alias="merlinId", union_mode="left_to_right")
    native_id: str | Any = Field(None, alias="nativeId", union_mode="left_to_right")
    nbcu_id: str | Any = Field(None, alias="nbcuId", union_mode="left_to_right")
    ott_certificate: str | Any = Field(
        None, alias="ottCertificate", union_mode="left_to_right"
    )
    production_language: str | Any = Field(
        None, alias="productionLanguage", union_mode="left_to_right"
    )
    programme_uuid: UUID | Any = Field(
        None, alias="programmeUuid", union_mode="left_to_right"
    )
    provider_id: str | Any = Field(None, alias="providerId", union_mode="left_to_right")
    provider_variant_id: UUID | Any = Field(
        None, alias="providerVariantId", union_mode="left_to_right"
    )
    runtime: time | Any = Field(default=None, union_mode="left_to_right")
    section_navigation: str | Any = Field(
        None, alias="sectionNavigation", union_mode="left_to_right"
    )
    slug: str | Any = Field(default=None, union_mode="left_to_right")
    sort_title: str | Any = Field(None, alias="sortTitle", union_mode="left_to_right")
    subtitled: bool | Any = Field(default=None, union_mode="left_to_right")
    synopsis: str | Any = Field(default=None, union_mode="left_to_right")
    synopsis_brief: str | Any = Field(
        None, alias="synopsisBrief", union_mode="left_to_right"
    )
    synopsis_long: str | Any = Field(
        None, alias="synopsisLong", union_mode="left_to_right"
    )
    synopsis_short: str | Any = Field(
        None, alias="synopsisShort", union_mode="left_to_right"
    )
    target_audience: TargetAudience | Any = Field(
        None, alias="targetAudience", union_mode="left_to_right"
    )
    title: str | Any = Field(default=None, union_mode="left_to_right")
    title_long: str | Any = Field(None, alias="titleLong", union_mode="left_to_right")
    title_medium: str | Any = Field(
        None, alias="titleMedium", union_mode="left_to_right"
    )
    title_seo: str | Any = Field(None, alias="titleSeo", union_mode="left_to_right")
    year: int | Any = Field(default=None, union_mode="left_to_right")
    alternative_date: list[AlternativeDateItem] | Any = Field(
        None, alias="alternativeDate", union_mode="left_to_right"
    )
    cwm: str | Any = Field(default=None, union_mode="left_to_right")
    fan_critic_rating: list[FanCriticRatingItem] | Any = Field(
        None, alias="fanCriticRating", union_mode="left_to_right"
    )
    is_kids_content: bool | Any = Field(
        None, alias="isKidsContent", union_mode="left_to_right"
    )
    placement_tags: list[PlacementTag] | Any = Field(
        None, alias="placementTags", union_mode="left_to_right"
    )
    producer: list[str] | Any = Field(default=None, union_mode="left_to_right")
    rating: str | Any = Field(default=None, union_mode="left_to_right")
    rating_percentage: int | Any = Field(
        None, alias="ratingPercentage", union_mode="left_to_right"
    )


class FirstEp(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    node_types: list[str] | Any = Field(
        None, alias="nodeTypes", union_mode="left_to_right"
    )
    count: int | Any = Field(default=None, union_mode="left_to_right")


class FreeEpisodes(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    node_types: list[Any] | Any = Field(
        None, alias="nodeTypes", union_mode="left_to_right"
    )
    count: int | Any = Field(default=None, union_mode="left_to_right")


class Items(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    node_types: list[str] | Any = Field(
        None, alias="nodeTypes", union_mode="left_to_right"
    )
    count: int | Any = Field(default=None, union_mode="left_to_right")


class Collections(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    node_types: list[str] | Any = Field(
        None, alias="nodeTypes", union_mode="left_to_right"
    )
    count: int | Any = Field(default=None, union_mode="left_to_right")


class ChildTypes1(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    images: Images | Any = Field(default=None, union_mode="left_to_right")
    shortforms: Shortforms | Any = Field(default=None, union_mode="left_to_right")
    trailers: Trailers | Any = Field(default=None, union_mode="left_to_right")
    first_ep: FirstEp | Any = Field(default=None, union_mode="left_to_right")
    free_episodes: FreeEpisodes | Any = Field(default=None, union_mode="left_to_right")
    items: Items | Any = Field(default=None, union_mode="left_to_right")
    clips: Clips | Any = Field(default=None, union_mode="left_to_right")
    linked_assets: LinkedAssets | Any = Field(default=None, union_mode="left_to_right")
    collections: Collections | Any = Field(default=None, union_mode="left_to_right")


class Term(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    description: str | Any = Field(default=None, union_mode="left_to_right")
    abbreviation: str | Any = Field(default=None, union_mode="left_to_right")


class AdvisoryItem(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    terms: list[Term] | Any = Field(default=None, union_mode="left_to_right")
    id: str | Any = Field(default=None, union_mode="left_to_right")
    group: int | Any = Field(default=None, union_mode="left_to_right")


class Badging1(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    video_formats: list[VideoFormat] | Any = Field(
        None, alias="videoFormats", union_mode="left_to_right"
    )
    audio_tracks: list[str] | Any = Field(
        None, alias="audioTracks", union_mode="left_to_right"
    )


class DeviceAvailability2(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    format: str | Any = Field(default=None, union_mode="left_to_right")
    media_type: str | Any = Field(None, alias="mediaType", union_mode="left_to_right")
    offer_stage: str | Any = Field(None, alias="offerStage", union_mode="left_to_right")
    offer_start_ts: int | Any = Field(
        None, alias="offerStartTs", union_mode="left_to_right"
    )
    offer_end_ts: int | Any = Field(
        None, alias="offerEndTs", union_mode="left_to_right"
    )
    streamable: bool | Any = Field(default=None, union_mode="left_to_right")
    downloadable: bool | Any = Field(default=None, union_mode="left_to_right")
    content_segment: str | Any = Field(
        None, alias="contentSegment", union_mode="left_to_right"
    )
    video_format: str | Any = Field(
        None, alias="videoFormat", union_mode="left_to_right"
    )
    video_format_variant: str | Any = Field(
        None, alias="videoFormatVariant", union_mode="left_to_right"
    )
    colour_space: str | Any = Field(
        None, alias="colourSpace", union_mode="left_to_right"
    )


class DeviceAvailability3(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    available: bool | Any = Field(default=None, union_mode="left_to_right")


class Restriction(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    usage: str | Any = Field(default=None, union_mode="left_to_right")
    type: str | Any = Field(default=None, union_mode="left_to_right")
    platform_capability: Any | None = Field(None, alias="platformCapability")
    value: str | Any = Field(default=None, union_mode="left_to_right")
    parameters: list[Any] | Any = Field(default=None, union_mode="left_to_right")


class Availability1(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    available: bool | Any = Field(default=None, union_mode="left_to_right")
    media_type: str | Any = Field(None, alias="mediaType", union_mode="left_to_right")
    offer_stage: str | Any = Field(None, alias="offerStage", union_mode="left_to_right")
    offer_start_ts: int | Any = Field(
        None, alias="offerStartTs", union_mode="left_to_right"
    )
    offer_end_ts: int | Any = Field(
        None, alias="offerEndTs", union_mode="left_to_right"
    )
    streamable: bool | Any = Field(default=None, union_mode="left_to_right")
    downloadable: bool | Any = Field(default=None, union_mode="left_to_right")
    available_devices: list[AvailableDevice] | Any = Field(
        None, alias="availableDevices", union_mode="left_to_right"
    )
    extended_offer_start_ts: int | Any = Field(
        None, alias="extendedOfferStartTs", union_mode="left_to_right"
    )
    extended_offer_end_ts: int | Any = Field(
        None, alias="extendedOfferEndTs", union_mode="left_to_right"
    )
    content_segment: str | Any = Field(
        None, alias="contentSegment", union_mode="left_to_right"
    )
    video_format: str | Any = Field(
        None, alias="videoFormat", union_mode="left_to_right"
    )
    video_format_variant: str | Any = Field(
        None, alias="videoFormatVariant", union_mode="left_to_right"
    )
    colour_space: str | Any = Field(
        None, alias="colourSpace", union_mode="left_to_right"
    )
    free_offer_end_ts: int | Any = Field(
        None, alias="freeOfferEndTs", union_mode="left_to_right"
    )
    restrictions: list[Restriction] | Any = Field(
        default=None, union_mode="left_to_right"
    )


class Markers1(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    socr: int | Any = Field(None, alias="SOCR", union_mode="left_to_right")
    solc: int | Any = Field(None, alias="SOLC", union_mode="left_to_right")
    eolc: int | Any = Field(None, alias="EOLC", union_mode="left_to_right")


class Hd1(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    audio_tracks: AudioTracks | Any = Field(
        None, alias="audioTracks", union_mode="left_to_right"
    )
    chapter_markers: list[Any] | Any = Field(
        None, alias="chapterMarkers", union_mode="left_to_right"
    )
    event_stage: str | Any = Field(None, alias="eventStage", union_mode="left_to_right")
    content_id: str | Any = Field(None, alias="contentId", union_mode="left_to_right")
    availability: Availability1 | Any = Field(default=None, union_mode="left_to_right")
    start_of_credits: int | Any = Field(
        None, alias="startOfCredits", union_mode="left_to_right"
    )
    markers: Markers1 | Any = Field(default=None, union_mode="left_to_right")


class Formats1(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    hd: Hd1 | Any = Field(None, alias="HD", union_mode="left_to_right")


class MediaType(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    media_type: str | Any = Field(None, alias="mediaType", union_mode="left_to_right")
    count: int | Any = Field(default=None, union_mode="left_to_right")
    latest: int | Any = Field(default=None, union_mode="left_to_right")


class Attributes1(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    free_wheel_content_id: str | Any = Field(
        None, alias="FreeWheelContentID", union_mode="left_to_right"
    )
    advisory: list[AdvisoryItem] | Any = Field(default=None, union_mode="left_to_right")
    audience_level: list[AudienceLevelItem] | Any = Field(
        None, alias="audienceLevel", union_mode="left_to_right"
    )
    audio_described: bool | Any = Field(
        None, alias="audioDescribed", union_mode="left_to_right"
    )
    badging: Badging1 | Any = Field(default=None, union_mode="left_to_right")
    cast: list[str] | Any = Field(default=None, union_mode="left_to_right")
    channel: Channel | Any = Field(default=None, union_mode="left_to_right")
    chapters_enabled: bool | Any = Field(
        None, alias="chaptersEnabled", union_mode="left_to_right"
    )
    child_node_types: list[str] | Any = Field(
        None, alias="childNodeTypes", union_mode="left_to_right"
    )
    classification: list[str] | Any = Field(default=None, union_mode="left_to_right")
    closed_captioned: bool | Any = Field(
        None, alias="closedCaptioned", union_mode="left_to_right"
    )
    content_segments: list[str] | Any = Field(
        None, alias="contentSegments", union_mode="left_to_right"
    )
    created_date: int | Any = Field(
        None, alias="createdDate", union_mode="left_to_right"
    )
    desc_long_seo: str | Any = Field(
        None, alias="descLongSeo", union_mode="left_to_right"
    )
    device_availabilities: list[DeviceAvailability2] | Any = Field(
        None, alias="deviceAvailabilities", union_mode="left_to_right"
    )
    device_availability: DeviceAvailability3 | Any = Field(
        None, alias="deviceAvailability", union_mode="left_to_right"
    )
    director: list[str] | Any = Field(default=None, union_mode="left_to_right")
    duration_milliseconds: int | Any = Field(
        None, alias="durationMilliseconds", union_mode="left_to_right"
    )
    duration_minutes: int | Any = Field(
        None, alias="durationMinutes", union_mode="left_to_right"
    )
    duration_seconds: int | Any = Field(
        None, alias="durationSeconds", union_mode="left_to_right"
    )
    editorial_warning_text: str | Any = Field(
        None, alias="editorialWarningText", union_mode="left_to_right"
    )
    formats: Formats1 | Any = Field(default=None, union_mode="left_to_right")
    genre_details: list[GenreDetail] | Any = Field(
        None, alias="genreDetails", union_mode="left_to_right"
    )
    genre_list: list[GenreListItem] | Any = Field(
        None, alias="genreList", union_mode="left_to_right"
    )
    genres: list[str] | Any = Field(default=None, union_mode="left_to_right")
    gracenote_id: str | Any = Field(
        None, alias="gracenoteId", union_mode="left_to_right"
    )
    images: list[Image] | Any = Field(default=None, union_mode="left_to_right")
    main_original_language: str | Any = Field(
        None, alias="mainOriginalLanguage", union_mode="left_to_right"
    )
    merlin_alternate_id: str | Any = Field(
        None, alias="merlinAlternateId", union_mode="left_to_right"
    )
    merlin_id: str | Any = Field(None, alias="merlinId", union_mode="left_to_right")
    native_id: str | Any = Field(None, alias="nativeId", union_mode="left_to_right")
    nbcu_id: str | Any = Field(None, alias="nbcuId", union_mode="left_to_right")
    ott_certificate: str | Any = Field(
        None, alias="ottCertificate", union_mode="left_to_right"
    )
    producer: list[str] | Any = Field(default=None, union_mode="left_to_right")
    production_language: str | Any = Field(
        None, alias="productionLanguage", union_mode="left_to_right"
    )
    programme_uuid: UUID | Any = Field(
        None, alias="programmeUuid", union_mode="left_to_right"
    )
    provider_id: str | Any = Field(None, alias="providerId", union_mode="left_to_right")
    provider_variant_id: UUID | Any = Field(
        None, alias="providerVariantId", union_mode="left_to_right"
    )
    runtime: time | Any = Field(default=None, union_mode="left_to_right")
    section_navigation: str | Any = Field(
        None, alias="sectionNavigation", union_mode="left_to_right"
    )
    slug: str | Any = Field(default=None, union_mode="left_to_right")
    sort_title: str | Any = Field(None, alias="sortTitle", union_mode="left_to_right")
    subtitled: bool | Any = Field(default=None, union_mode="left_to_right")
    synopsis: str | Any = Field(default=None, union_mode="left_to_right")
    synopsis_brief: str | Any = Field(
        None, alias="synopsisBrief", union_mode="left_to_right"
    )
    synopsis_long: str | Any = Field(
        None, alias="synopsisLong", union_mode="left_to_right"
    )
    synopsis_short: str | Any = Field(
        None, alias="synopsisShort", union_mode="left_to_right"
    )
    target_audience: TargetAudience | Any = Field(
        None, alias="targetAudience", union_mode="left_to_right"
    )
    title: str | Any = Field(default=None, union_mode="left_to_right")
    title_long: str | Any = Field(None, alias="titleLong", union_mode="left_to_right")
    title_medium: str | Any = Field(
        None, alias="titleMedium", union_mode="left_to_right"
    )
    title_seo: str | Any = Field(None, alias="titleSeo", union_mode="left_to_right")
    year: int | Any = Field(default=None, union_mode="left_to_right")
    available_episode_count: int | Any = Field(
        None, alias="availableEpisodeCount", union_mode="left_to_right"
    )
    available_season_count: int | Any = Field(
        None, alias="availableSeasonCount", union_mode="left_to_right"
    )
    brands: list[str] | Any = Field(default=None, union_mode="left_to_right")
    gracenote_series_id: str | Any = Field(
        None, alias="gracenoteSeriesId", union_mode="left_to_right"
    )
    media_types: list[MediaType] | Any = Field(
        None, alias="mediaTypes", union_mode="left_to_right"
    )
    merlin_series_id: str | Any = Field(
        None, alias="merlinSeriesId", union_mode="left_to_right"
    )
    nbcu_series_id: str | Any = Field(
        None, alias="nbcuSeriesId", union_mode="left_to_right"
    )
    provider_series_id: str | Any = Field(
        None, alias="providerSeriesId", union_mode="left_to_right"
    )
    reverse_order: bool | Any = Field(
        None, alias="reverseOrder", union_mode="left_to_right"
    )
    series_native_id: str | Any = Field(
        None, alias="seriesNativeId", union_mode="left_to_right"
    )
    series_uuid: UUID | Any = Field(
        None, alias="seriesUuid", union_mode="left_to_right"
    )
    smart_call_to_action: str | Any = Field(
        None, alias="smartCallToAction", union_mode="left_to_right"
    )
    cwm: str | Any = Field(default=None, union_mode="left_to_right")
    alternative_date: list[AlternativeDateItem] | Any = Field(
        None, alias="alternativeDate", union_mode="left_to_right"
    )
    fan_critic_rating: list[FanCriticRatingItem] | Any = Field(
        None, alias="fanCriticRating", union_mode="left_to_right"
    )
    is_kids_content: bool | Any = Field(
        None, alias="isKidsContent", union_mode="left_to_right"
    )
    placement_tags: list[PlacementTag] | Any = Field(
        None, alias="placementTags", union_mode="left_to_right"
    )
    rating: str | Any = Field(default=None, union_mode="left_to_right")
    rating_percentage: int | Any = Field(
        None, alias="ratingPercentage", union_mode="left_to_right"
    )
    privacy_restrictions: list[str] | Any = Field(
        None, alias="privacyRestrictions", union_mode="left_to_right"
    )


class Datum(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    links: Links | Any = Field(default=None, union_mode="left_to_right")
    id: UUID | Any = Field(default=None, union_mode="left_to_right")
    type: str | Any = Field(default=None, union_mode="left_to_right")
    child_types: ChildTypes1 | Any = Field(
        None, alias="childTypes", union_mode="left_to_right"
    )
    attributes: Attributes1 | Any = Field(default=None, union_mode="left_to_right")


class Recs(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    data: list[Datum] | Any = Field(default=None, union_mode="left_to_right")


class ChildTypes2(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    images: Images | Any = Field(default=None, union_mode="left_to_right")


class Badging2(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    video_formats: list[VideoFormat] | Any = Field(
        None, alias="videoFormats", union_mode="left_to_right"
    )
    audio_tracks: list[str] | Any = Field(
        None, alias="audioTracks", union_mode="left_to_right"
    )


class DeviceAvailability4(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    format: str | Any = Field(default=None, union_mode="left_to_right")
    media_type: str | Any = Field(None, alias="mediaType", union_mode="left_to_right")
    offer_stage: str | Any = Field(None, alias="offerStage", union_mode="left_to_right")
    offer_start_ts: int | Any = Field(
        None, alias="offerStartTs", union_mode="left_to_right"
    )
    offer_end_ts: int | Any = Field(
        None, alias="offerEndTs", union_mode="left_to_right"
    )
    streamable: bool | Any = Field(default=None, union_mode="left_to_right")
    downloadable: bool | Any = Field(default=None, union_mode="left_to_right")
    content_segment: str | Any = Field(
        None, alias="contentSegment", union_mode="left_to_right"
    )
    video_format: str | Any = Field(
        None, alias="videoFormat", union_mode="left_to_right"
    )
    video_format_variant: str | Any = Field(
        None, alias="videoFormatVariant", union_mode="left_to_right"
    )
    colour_space: str | Any = Field(
        None, alias="colourSpace", union_mode="left_to_right"
    )


class DeviceAvailability5(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    available: bool | Any = Field(default=None, union_mode="left_to_right")


class AudioTracks2(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    eng: list[str] | Any = Field(default=None, union_mode="left_to_right")


class Availability2(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    available: bool | Any = Field(default=None, union_mode="left_to_right")
    media_type: str | Any = Field(None, alias="mediaType", union_mode="left_to_right")
    offer_stage: str | Any = Field(None, alias="offerStage", union_mode="left_to_right")
    offer_start_ts: int | Any = Field(
        None, alias="offerStartTs", union_mode="left_to_right"
    )
    offer_end_ts: int | Any = Field(
        None, alias="offerEndTs", union_mode="left_to_right"
    )
    streamable: bool | Any = Field(default=None, union_mode="left_to_right")
    downloadable: bool | Any = Field(default=None, union_mode="left_to_right")
    available_devices: list[AvailableDevice] | Any = Field(
        None, alias="availableDevices", union_mode="left_to_right"
    )
    extended_offer_start_ts: int | Any = Field(
        None, alias="extendedOfferStartTs", union_mode="left_to_right"
    )
    extended_offer_end_ts: int | Any = Field(
        None, alias="extendedOfferEndTs", union_mode="left_to_right"
    )
    content_segment: str | Any = Field(
        None, alias="contentSegment", union_mode="left_to_right"
    )
    video_format: str | Any = Field(
        None, alias="videoFormat", union_mode="left_to_right"
    )
    video_format_variant: str | Any = Field(
        None, alias="videoFormatVariant", union_mode="left_to_right"
    )
    colour_space: str | Any = Field(
        None, alias="colourSpace", union_mode="left_to_right"
    )
    restrictions: list[Restriction] | Any = Field(
        default=None, union_mode="left_to_right"
    )


class Hd2(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    audio_tracks: AudioTracks2 | Any = Field(
        None, alias="audioTracks", union_mode="left_to_right"
    )
    chapter_markers: list[Any] | Any = Field(
        None, alias="chapterMarkers", union_mode="left_to_right"
    )
    event_stage: str | Any = Field(None, alias="eventStage", union_mode="left_to_right")
    content_id: str | Any = Field(None, alias="contentId", union_mode="left_to_right")
    availability: Availability2 | Any = Field(default=None, union_mode="left_to_right")
    start_of_credits: int | Any = Field(
        None, alias="startOfCredits", union_mode="left_to_right"
    )


class Formats2(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    hd: Hd2 | Any = Field(None, alias="HD", union_mode="left_to_right")


class Hd3(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    content_id: str | Any = Field(None, alias="contentId", union_mode="left_to_right")


class Uhdsdr(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    content_id: str | Any = Field(None, alias="contentId", union_mode="left_to_right")


class Uhdhdr(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    content_id: str | Any = Field(None, alias="contentId", union_mode="left_to_right")


class Formats3(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    hd: Hd3 | Any = Field(None, alias="HD", union_mode="left_to_right")
    uhdsdr: Uhdsdr | Any = Field(None, alias="UHDSDR", union_mode="left_to_right")
    uhdhdr: Uhdhdr | Any = Field(None, alias="UHDHDR", union_mode="left_to_right")


class MainTitleInfoItem(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    node_id: UUID | Any = Field(None, alias="nodeId", union_mode="left_to_right")
    type: str | Any = Field(default=None, union_mode="left_to_right")
    programme_uuid: UUID | Any = Field(
        None, alias="programmeUuid", union_mode="left_to_right"
    )
    provider_variant_id: UUID | Any = Field(
        None, alias="providerVariantId", union_mode="left_to_right"
    )
    formats: Formats3 | Any = Field(default=None, union_mode="left_to_right")
    content_segments: list[str] | Any = Field(
        None, alias="contentSegments", union_mode="left_to_right"
    )


class Attributes2(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    free_wheel_content_id: str | Any = Field(
        None, alias="FreeWheelContentID", union_mode="left_to_right"
    )
    audio_described: bool | Any = Field(
        None, alias="audioDescribed", union_mode="left_to_right"
    )
    autoplay: bool | Any = Field(default=None, union_mode="left_to_right")
    badging: Badging2 | Any = Field(default=None, union_mode="left_to_right")
    channel: Channel | Any = Field(default=None, union_mode="left_to_right")
    chapters_enabled: bool | Any = Field(
        None, alias="chaptersEnabled", union_mode="left_to_right"
    )
    child_node_types: list[str] | Any = Field(
        None, alias="childNodeTypes", union_mode="left_to_right"
    )
    classification: list[str] | Any = Field(default=None, union_mode="left_to_right")
    closed_captioned: bool | Any = Field(
        None, alias="closedCaptioned", union_mode="left_to_right"
    )
    content_segments: list[str] | Any = Field(
        None, alias="contentSegments", union_mode="left_to_right"
    )
    created_date: int | Any = Field(
        None, alias="createdDate", union_mode="left_to_right"
    )
    device_availabilities: list[DeviceAvailability4] | Any = Field(
        None, alias="deviceAvailabilities", union_mode="left_to_right"
    )
    device_availability: DeviceAvailability5 | Any = Field(
        None, alias="deviceAvailability", union_mode="left_to_right"
    )
    duration_milliseconds: int | Any = Field(
        None, alias="durationMilliseconds", union_mode="left_to_right"
    )
    duration_minutes: int | Any = Field(
        None, alias="durationMinutes", union_mode="left_to_right"
    )
    duration_seconds: int | Any = Field(
        None, alias="durationSeconds", union_mode="left_to_right"
    )
    formats: Formats2 | Any = Field(default=None, union_mode="left_to_right")
    free_wheel_creative_id: str | Any = Field(
        None, alias="freeWheelCreativeId", union_mode="left_to_right"
    )
    genre_list: list[GenreListItem] | Any = Field(
        None, alias="genreList", union_mode="left_to_right"
    )
    genres: list[str] | Any = Field(default=None, union_mode="left_to_right")
    images: list[Image] | Any = Field(default=None, union_mode="left_to_right")
    main_title_info: list[MainTitleInfoItem] | Any = Field(
        None, alias="mainTitleInfo", union_mode="left_to_right"
    )
    merlin_id: str | Any = Field(None, alias="merlinId", union_mode="left_to_right")
    nbcu_id: str | Any = Field(None, alias="nbcuId", union_mode="left_to_right")
    ott_certificate: str | Any = Field(
        None, alias="ottCertificate", union_mode="left_to_right"
    )
    programme_uuid: UUID | Any = Field(
        None, alias="programmeUuid", union_mode="left_to_right"
    )
    provider_id: str | Any = Field(None, alias="providerId", union_mode="left_to_right")
    provider_variant_id: UUID | Any = Field(
        None, alias="providerVariantId", union_mode="left_to_right"
    )
    runtime: time | Any = Field(default=None, union_mode="left_to_right")
    slug: str | Any = Field(default=None, union_mode="left_to_right")
    synopsis_long: str | Any = Field(
        None, alias="synopsisLong", union_mode="left_to_right"
    )
    synopsis_short: str | Any = Field(
        None, alias="synopsisShort", union_mode="left_to_right"
    )
    target_audience: TargetAudience | Any = Field(
        None, alias="targetAudience", union_mode="left_to_right"
    )
    title: str | Any = Field(default=None, union_mode="left_to_right")
    title_long: str | Any = Field(None, alias="titleLong", union_mode="left_to_right")
    title_medium: str | Any = Field(
        None, alias="titleMedium", union_mode="left_to_right"
    )
    alternative_date: list[AlternativeDateItem] | Any = Field(
        None, alias="alternativeDate", union_mode="left_to_right"
    )
    cwm: str | Any = Field(default=None, union_mode="left_to_right")
    fan_critic_rating: list[FanCriticRatingItem] | Any = Field(
        None, alias="fanCriticRating", union_mode="left_to_right"
    )
    is_kids_content: bool | Any = Field(
        None, alias="isKidsContent", union_mode="left_to_right"
    )
    privacy_restrictions: list[str] | Any = Field(
        None, alias="privacyRestrictions", union_mode="left_to_right"
    )


class Datum1(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    links: Links | Any = Field(default=None, union_mode="left_to_right")
    id: UUID | Any = Field(default=None, union_mode="left_to_right")
    type: str | Any = Field(default=None, union_mode="left_to_right")
    child_types: ChildTypes2 | Any = Field(
        None, alias="childTypes", union_mode="left_to_right"
    )
    attributes: Attributes2 | Any = Field(default=None, union_mode="left_to_right")


class Trailers2(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    data: list[Datum1] | Any = Field(default=None, union_mode="left_to_right")


class Relationships(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    recs: Recs | Any = Field(default=None, union_mode="left_to_right")
    trailers: Trailers2 | Any = Field(default=None, union_mode="left_to_right")


class MovieModel(BaseModel):
    model_config = ConfigDict(extra="ignore", defer_build=True)
    links: Links | Any = Field(default=None, union_mode="left_to_right")
    id: UUID | Any = Field(default=None, union_mode="left_to_right")
    type: str | Any = Field(default=None, union_mode="left_to_right")
    child_types: ChildTypes | Any = Field(
        None, alias="childTypes", union_mode="left_to_right"
    )
    attributes: Attributes | Any = Field(default=None, union_mode="left_to_right")
    relationships: Relationships | Any = Field(default=None, union_mode="left_to_right")
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
