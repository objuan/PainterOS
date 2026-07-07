from __future__ import annotations


class PainterOSError(Exception):
    """Base exception for PainterOS."""


class ServiceNotFoundError(PainterOSError):
    """Requested service does not exist."""


class DuplicateServiceError(PainterOSError):
    """Service already registered."""


class ConfigurationError(PainterOSError):
    """Configuration is invalid."""