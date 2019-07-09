# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class FilterTrackPropertyType(str, Enum):

    unknown = "Unknown"  #: The unknown track property type.
    type = "Type"  #: The type.
    name = "Name"  #: The name.
    language = "Language"  #: The language.
    four_cc = "FourCC"  #: The fourCC.
    bitrate = "Bitrate"  #: The bitrate.


class FilterTrackPropertyCompareOperation(str, Enum):

    equal = "Equal"  #: The equal operation.
    not_equal = "NotEqual"  #: The not equal operation.


class MetricUnit(str, Enum):

    bytes = "Bytes"  #: The number of bytes.
    count = "Count"  #: The count.
    milliseconds = "Milliseconds"  #: The number of milliseconds.


class MetricAggregationType(str, Enum):

    average = "Average"  #: The average.
    count = "Count"  #: The count of a number of items, usually requests.
    total = "Total"  #: The sum.


class StorageAccountType(str, Enum):

    primary = "Primary"  #: The primary storage account for the Media Services account.
    secondary = "Secondary"  #: A secondary storage account for the Media Services account.


class AssetStorageEncryptionFormat(str, Enum):

    none = "None"  #: The Asset does not use client-side storage encryption (this is the only allowed value for new Assets).
    media_storage_client_encryption = "MediaStorageClientEncryption"  #: The Asset is encrypted with Media Services client-side encryption.


class AssetContainerPermission(str, Enum):

    read = "Read"  #: The SAS URL will allow read access to the container.
    read_write = "ReadWrite"  #: The SAS URL will allow read and write access to the container.
    read_write_delete = "ReadWriteDelete"  #: The SAS URL will allow read, write and delete access to the container.


class ContentKeyPolicyPlayReadyUnknownOutputPassingOption(str, Enum):

    unknown = "Unknown"  #: Represents a ContentKeyPolicyPlayReadyUnknownOutputPassingOption that is unavailable in current API version.
    not_allowed = "NotAllowed"  #: Passing the video portion of protected content to an Unknown Output is not allowed.
    allowed = "Allowed"  #: Passing the video portion of protected content to an Unknown Output is allowed.
    allowed_with_video_constriction = "AllowedWithVideoConstriction"  #: Passing the video portion of protected content to an Unknown Output is allowed but with constrained resolution.


class ContentKeyPolicyPlayReadyLicenseType(str, Enum):

    unknown = "Unknown"  #: Represents a ContentKeyPolicyPlayReadyLicenseType that is unavailable in current API version.
    non_persistent = "NonPersistent"  #: Non persistent license.
    persistent = "Persistent"  #: Persistent license. Allows offline playback.


class ContentKeyPolicyPlayReadyContentType(str, Enum):

    unknown = "Unknown"  #: Represents a ContentKeyPolicyPlayReadyContentType that is unavailable in current API version.
    unspecified = "Unspecified"  #: Unspecified content type.
    ultra_violet_download = "UltraVioletDownload"  #: Ultraviolet download content type.
    ultra_violet_streaming = "UltraVioletStreaming"  #: Ultraviolet streaming content type.


class ContentKeyPolicyRestrictionTokenType(str, Enum):

    unknown = "Unknown"  #: Represents a ContentKeyPolicyRestrictionTokenType that is unavailable in current API version.
    swt = "Swt"  #: Simple Web Token.
    jwt = "Jwt"  #: JSON Web Token.


class ContentKeyPolicyFairPlayRentalAndLeaseKeyType(str, Enum):

    unknown = "Unknown"  #: Represents a ContentKeyPolicyFairPlayRentalAndLeaseKeyType that is unavailable in current API version.
    undefined = "Undefined"  #: Key duration is not specified.
    persistent_unlimited = "PersistentUnlimited"  #: Content key can be persisted with an unlimited duration
    persistent_limited = "PersistentLimited"  #: Content key can be persisted and the valid duration is limited by the Rental Duration value


class AacAudioProfile(str, Enum):

    aac_lc = "AacLc"  #: Specifies that the output audio is to be encoded into AAC Low Complexity profile (AAC-LC).
    he_aac_v1 = "HeAacV1"  #: Specifies that the output audio is to be encoded into HE-AAC v1 profile.
    he_aac_v2 = "HeAacV2"  #: Specifies that the output audio is to be encoded into HE-AAC v2 profile.


class AnalysisResolution(str, Enum):

    source_resolution = "SourceResolution"
    standard_definition = "StandardDefinition"


class StretchMode(str, Enum):

    none = "None"  #: Strictly respect the output resolution without considering the pixel aspect ratio or display aspect ratio of the input video.
    auto_size = "AutoSize"  #: Override the output resolution, and change it to match the display aspect ratio of the input, without padding. For example, if the input is 1920x1080 and the encoding preset asks for 1280x1280, then the value in the preset is overridden, and the output will be at 1280x720, which maintains the input aspect ratio of 16:9.
    auto_fit = "AutoFit"  #: Pad the output (with either letterbox or pillar box) to honor the output resolution, while ensuring that the active video region in the output has the same aspect ratio as the input. For example, if the input is 1920x1080 and the encoding preset asks for 1280x1280, then the output will be at 1280x1280, which contains an inner rectangle of 1280x720 at aspect ratio of 16:9, and pillar box regions 280 pixels wide at the left and right.


class DeinterlaceParity(str, Enum):

    auto = "Auto"  #: Automatically detect the order of fields
    top_field_first = "TopFieldFirst"  #: Apply top field first processing of input video.
    bottom_field_first = "BottomFieldFirst"  #: Apply bottom field first processing of input video.


class DeinterlaceMode(str, Enum):

    off = "Off"  #: Disables de-interlacing of the source video.
    auto_pixel_adaptive = "AutoPixelAdaptive"  #: Apply automatic pixel adaptive de-interlacing on each frame in the input video.


class Rotation(str, Enum):

    auto = "Auto"  #: Automatically detect and rotate as needed.
    none = "None"  #: Do not rotate the video.  If the output format supports it, any metadata about rotation is kept intact.
    rotate0 = "Rotate0"  #: Do not rotate the video but remove any metadata about the rotation.
    rotate90 = "Rotate90"  #: Rotate 90 degrees clockwise.
    rotate180 = "Rotate180"  #: Rotate 180 degrees clockwise.
    rotate270 = "Rotate270"  #: Rotate 270 degrees clockwise.


class H264VideoProfile(str, Enum):

    auto = "Auto"  #: Tells the encoder to automatically determine the appropriate H.264 profile.
    baseline = "Baseline"  #: Baseline profile
    main = "Main"  #: Main profile
    high = "High"  #: High profile.
    high422 = "High422"  #: High 4:2:2 profile.
    high444 = "High444"  #: High 4:4:4 predictive profile.


class EntropyMode(str, Enum):

    cabac = "Cabac"  #: Context Adaptive Binary Arithmetic Coder (CABAC) entropy encoding.
    cavlc = "Cavlc"  #: Context Adaptive Variable Length Coder (CAVLC) entropy encoding.


class H264Complexity(str, Enum):

    speed = "Speed"  #: Tells the encoder to use settings that are optimized for faster encoding. Quality is sacrificed to decrease encoding time.
    balanced = "Balanced"  #: Tells the encoder to use settings that achieve a balance between speed and quality.
    quality = "Quality"  #: Tells the encoder to use settings that are optimized to produce higher quality output at the expense of slower overall encode time.


class EncoderNamedPreset(str, Enum):

    h264_single_bitrate_sd = "H264SingleBitrateSD"  #: Produces an MP4 file where the video is encoded with H.264 codec at 2200 kbps and a picture height of 480 pixels, and the stereo audio is encoded with AAC-LC codec at 64 kbps.
    h264_single_bitrate720p = "H264SingleBitrate720p"  #: Produces an MP4 file where the video is encoded with H.264 codec at 4500 kbps and a picture height of 720 pixels, and the stereo audio is encoded with AAC-LC codec at 64 kbps.
    h264_single_bitrate1080p = "H264SingleBitrate1080p"  #: Produces an MP4 file where the video is encoded with H.264 codec at 6750 kbps and a picture height of 1080 pixels, and the stereo audio is encoded with AAC-LC codec at 64 kbps.
    adaptive_streaming = "AdaptiveStreaming"  #: Produces a set of GOP aligned MP4 files with H.264 video and stereo AAC audio. Auto-generates a bitrate ladder based on the input resolution and bitrate. The auto-generated preset will never exceed the input resolution and bitrate. For example, if the input is 720p at 3 Mbps, output will remain 720p at best, and will start at rates lower than 3 Mbps. The output will have video and audio in separate MP4 files, which is optimal for adaptive streaming.
    aac_good_quality_audio = "AACGoodQualityAudio"  #: Produces a single MP4 file containing only stereo audio encoded at 192 kbps.
    content_aware_encoding_experimental = "ContentAwareEncodingExperimental"  #: Exposes an experimental preset for content-aware encoding. Given any input content, the service attempts to automatically determine the optimal number of layers, appropriate bitrate and resolution settings for delivery by adaptive streaming. The underlying algorithms will continue to evolve over time. The output will contain MP4 files with video and audio interleaved.
    h264_multiple_bitrate1080p = "H264MultipleBitrate1080p"  #: Produces a set of 8 GOP-aligned MP4 files, ranging from 6000 kbps to 400 kbps, and stereo AAC audio. Resolution starts at 1080p and goes down to 360p.
    h264_multiple_bitrate720p = "H264MultipleBitrate720p"  #: Produces a set of 6 GOP-aligned MP4 files, ranging from 3400 kbps to 400 kbps, and stereo AAC audio. Resolution starts at 720p and goes down to 360p.
    h264_multiple_bitrate_sd = "H264MultipleBitrateSD"  #: Produces a set of 5 GOP-aligned MP4 files, ranging from 1600kbps to 400 kbps, and stereo AAC audio. Resolution starts at 480p and goes down to 360p.


class InsightsType(str, Enum):

    audio_insights_only = "AudioInsightsOnly"  #: Generate audio only insights. Ignore video even if present. Fails if no audio is present.
    video_insights_only = "VideoInsightsOnly"  #: Generate video only insights. Ignore audio if present. Fails if no video is present.
    all_insights = "AllInsights"  #: Generate both audio and video insights. Fails if either audio or video Insights fail.


class OnErrorType(str, Enum):

    stop_processing_job = "StopProcessingJob"  #: Tells the service that if this TransformOutput fails, then any other incomplete TransformOutputs can be stopped.
    continue_job = "ContinueJob"  #: Tells the service that if this TransformOutput fails, then allow any other TransformOutput to continue.


class Priority(str, Enum):

    low = "Low"  #: Used for TransformOutputs that can be generated after Normal and High priority TransformOutputs.
    normal = "Normal"  #: Used for TransformOutputs that can be generated at Normal priority.
    high = "High"  #: Used for TransformOutputs that should take precedence over others.


class JobErrorCode(str, Enum):

    service_error = "ServiceError"  #: Fatal service error, please contact support.
    service_transient_error = "ServiceTransientError"  #: Transient error, please retry, if retry is unsuccessful, please contact support.
    download_not_accessible = "DownloadNotAccessible"  #: While trying to download the input files, the files were not accessible, please check the availability of the source.
    download_transient_error = "DownloadTransientError"  #: While trying to download the input files, there was an issue during transfer (storage service, network errors), see details and check your source.
    upload_not_accessible = "UploadNotAccessible"  #: While trying to upload the output files, the destination was not reachable, please check the availability of the destination.
    upload_transient_error = "UploadTransientError"  #: While trying to upload the output files, there was an issue during transfer (storage service, network errors), see details and check your destination.
    configuration_unsupported = "ConfigurationUnsupported"  #: There was a problem with the combination of input files and the configuration settings applied, fix the configuration settings and retry with the same input, or change input to match the configuration.
    content_malformed = "ContentMalformed"  #: There was a problem with the input content (for example: zero byte files, or corrupt/non-decodable files), check the input files.
    content_unsupported = "ContentUnsupported"  #: There was a problem with the format of the input (not valid media file, or an unsupported file/codec), check the validity of the input files.


class JobErrorCategory(str, Enum):

    service = "Service"  #: The error is service related.
    download = "Download"  #: The error is download related.
    upload = "Upload"  #: The error is upload related.
    configuration = "Configuration"  #: The error is configuration related.
    content = "Content"  #: The error is related to data in the input files.


class JobRetry(str, Enum):

    do_not_retry = "DoNotRetry"  #: Issue needs to be investigated and then the job resubmitted with corrections or retried once the underlying issue has been corrected.
    may_retry = "MayRetry"  #: Issue may be resolved after waiting for a period of time and resubmitting the same Job.


class JobState(str, Enum):

    canceled = "Canceled"  #: The job was canceled. This is a final state for the job.
    canceling = "Canceling"  #: The job is in the process of being canceled. This is a transient state for the job.
    error = "Error"  #: The job has encountered an error. This is a final state for the job.
    finished = "Finished"  #: The job is finished. This is a final state for the job.
    processing = "Processing"  #: The job is processing. This is a transient state for the job.
    queued = "Queued"  #: The job is in a queued state, waiting for resources to become available. This is a transient state.
    scheduled = "Scheduled"  #: The job is being scheduled to run on an available resource. This is a transient state, between queued and processing states.


class TrackPropertyType(str, Enum):

    unknown = "Unknown"  #: Unknown track property
    four_cc = "FourCC"  #: Track FourCC


class TrackPropertyCompareOperation(str, Enum):

    unknown = "Unknown"  #: Unknown track property compare operation
    equal = "Equal"  #: Equal operation


class StreamingLocatorContentKeyType(str, Enum):

    common_encryption_cenc = "CommonEncryptionCenc"  #: Common Encryption using CENC
    common_encryption_cbcs = "CommonEncryptionCbcs"  #: Common Encryption using CBCS
    envelope_encryption = "EnvelopeEncryption"  #: Envelope Encryption


class StreamingPolicyStreamingProtocol(str, Enum):

    hls = "Hls"  #: HLS protocol
    dash = "Dash"  #: DASH protocol
    smooth_streaming = "SmoothStreaming"  #: SmoothStreaming protocol
    download = "Download"  #: Download protocol


class EncryptionScheme(str, Enum):

    no_encryption = "NoEncryption"  #: NoEncryption scheme
    envelope_encryption = "EnvelopeEncryption"  #: EnvelopeEncryption scheme
    common_encryption_cenc = "CommonEncryptionCenc"  #: CommonEncryptionCenc scheme
    common_encryption_cbcs = "CommonEncryptionCbcs"  #: CommonEncryptionCbcs scheme


class LiveOutputResourceState(str, Enum):

    creating = "Creating"
    running = "Running"
    deleting = "Deleting"


class LiveEventInputProtocol(str, Enum):

    fragmented_mp4 = "FragmentedMP4"
    rtmp = "RTMP"


class LiveEventEncodingType(str, Enum):

    none = "None"
    basic = "Basic"
    standard = "Standard"
    premium1080p = "Premium1080p"


class LiveEventResourceState(str, Enum):

    stopped = "Stopped"
    starting = "Starting"
    running = "Running"
    stopping = "Stopping"
    deleting = "Deleting"


class StreamOptionsFlag(str, Enum):

    default = "Default"
    low_latency = "LowLatency"


class StreamingEndpointResourceState(str, Enum):

    stopped = "Stopped"
    starting = "Starting"
    running = "Running"
    stopping = "Stopping"
    deleting = "Deleting"
    scaling = "Scaling"
