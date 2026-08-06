from enum import StrEnum


class S3ErrorDetail(StrEnum):
    # Bucket errors
    NoSuchBucket = 'NoSuchBucket'
    BucketAlreadyExists = 'BucketAlreadyExists'
    BucketAlreadyOwnedByYou = 'BucketAlreadyOwnedByYou'
    BucketNotEmpty = 'BucketNotEmpty'
    InvalidBucketName = 'InvalidBucketName'

    # Key errors
    NoSuchKey = 'NoSuchKey'
    InvalidObjectName = 'InvalidObjectName'
    EntityTooLarge = 'EntityTooLarge'

    # Access errors
    AccessDenied = 'AccessDenied'
    InvalidAccessKeyId = 'InvalidAccessKeyId'
    SignatureDoesNotMatch = 'SignatureDoesNotMatch'
